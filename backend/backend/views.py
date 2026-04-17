from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Application, Job
from .serializers import ApplicationSerializer, JobsSerializer, RegisterSerializer

# -------------------------------
# Function-based API views
# -------------------------------

@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello from Django API"})

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User Registered Successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def basic_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        return Response({
            "user_id": user.id,
            "username": user.username,
            "message": "Login successful"
        }, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def job_list(request):
    jobs = Job.objects.all()
    serializer = JobsSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def apply_job(request):
    serializer = ApplicationSerializer(data=request.data)
    job_id = request.data.get("job")
    applicant_id = request.data.get("applicant")

    # Prevent duplicate applications
    if Application.objects.filter(job_id=job_id, applicant_id=applicant_id).exists():
        return Response({"message": "You already have applied!"}, status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Application Submitted"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -------------------------------
# Class-based DRF viewsets
# -------------------------------

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-posted_on')
    serializer_class = JobsSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all().order_by('-applied_on')
    serializer_class = ApplicationSerializer
