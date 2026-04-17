from django.contrib.auth.models import User
from backend.models import Job   # absolute import since demo_data.py is in root

# Ensure you have a user to assign as job creator
user, _ = User.objects.get_or_create(
    username="admin",
    defaults={"email": "admin@example.com"}
)

# AI / ML Engineer
Job.objects.create(
    title="AI / ML Engineer",
    company="Zoom",
    location="Bengaluru",
    salary_range="15-20 LPA",
    created_by=user,
    about="""What You Can Expect

This role uniquely requires the intersection of time-series forecasting expertise and modern LLM capabilities, specifically applied to workforce management challenges.

Join our Workforce Engagement Management (WEM) team to solve real-world challenges at scale using cutting-edge ML techniques. You'll play a key role in building GenAI-powered forecasting, scheduling, and adherence solutions.""",
    responsibilities="""- Design and optimize AI/ML algorithms for WEM use cases
- Leverage time-series analysis and optimization frameworks (e.g., CP-SAT) for forecasting and scheduling
- Engineer and tune LLM prompts and workflows to enhance scheduling and forecasting insights
- Build and optimize infrastructure for distributed model training across multi-node, multi-GPU clusters
- Collaborate with teams for seamless integration of AI/ML features into production systems""",
    must_have_skills="Python, Pandas, NumPy, TensorFlow/PyTorch, Time-series forecasting",
    good_to_have_skills="LangChain, CrewAI, LlamaIndex, OR-Tools, Cloud deployment",
    qualifications="""Bachelor’s/Master’s/PhD in Computer Science, Artificial Intelligence, Machine Learning, or related field
4–6 years of hands-on experience in AI/ML engineering roles
Experience with LLMs, fine-tuning, prompt engineering""",
    benefits="""Hybrid work model
Health insurance and wellness programs
Career growth opportunities
Certification sponsorships"""
)

# Frontend Engineer
Job.objects.create(
    title="Frontend Engineer",
    company="Google",
    location="Hyderabad",
    salary_range="10-14 LPA",
    created_by=user,
    about="""What You Can Expect

Join our frontend engineering team to build scalable, responsive web applications that power millions of users worldwide. You'll work with modern frameworks and design systems to deliver seamless user experiences.""",
    responsibilities="""- Develop and maintain web applications using React and Next.js
- Collaborate with designers and backend engineers
- Ensure cross-browser compatibility and accessibility
- Optimize performance and scalability of frontend code""",
    must_have_skills="React, JavaScript, CSS, HTML",
    good_to_have_skills="Next.js, Tailwind, TypeScript, GraphQL",
    qualifications="""Bachelor’s in Computer Science or related field
2–4 years of frontend development experience
Strong understanding of responsive design and accessibility""",
    benefits="""Flexible hours
Learning budget
Team outings
Health insurance"""
)

# DevOps Engineer
Job.objects.create(
    title="DevOps Engineer",
    company="Meta",
    location="Pune",
    salary_range="12-16 LPA",
    created_by=user,
    about="""What You Can Expect

Work on CI/CD pipelines, container orchestration, and cloud deployments at scale. You'll be part of a team ensuring reliable, automated infrastructure for global applications.""",
    responsibilities="""- Automate infrastructure provisioning with Terraform
- Maintain CI/CD pipelines with Jenkins/GitHub Actions
- Monitor and optimize cloud deployments
- Collaborate with developers to improve release cycles""",
    must_have_skills="Docker, Kubernetes, CI/CD, Terraform",
    good_to_have_skills="AWS, Prometheus, Grafana, Ansible",
    qualifications="""Bachelor’s in Computer Science or related field
3–5 years of DevOps experience
Experience with cloud-native deployments""",
    benefits="""Remote work options
Certification sponsorship
Health insurance
Career growth opportunities"""
)

# Data Scientist
Job.objects.create(
    title="Data Scientist",
    company="Amazon",
    location="Delhi",
    salary_range="15-20 LPA",
    created_by=user,
    about="""What You Can Expect

Work on ML models, data pipelines, and analytics dashboards to drive insights across large-scale datasets. Collaborate with product and engineering teams to deliver data-driven solutions.""",
    responsibilities="""- Build predictive models and deploy them to production
- Design and maintain ETL pipelines
- Collaborate with product teams to deliver insights
- Conduct experiments and A/B testing""",
    must_have_skills="Python, SQL, Machine Learning, Statistics",
    good_to_have_skills="TensorFlow, PyTorch, Spark, AWS",
    qualifications="""Bachelor’s/Master’s in Computer Science, Statistics, or related field
2–5 years of data science experience
Strong background in ML and statistical modeling""",
    benefits="""Research budget
Flexible work
Health insurance
Learning opportunities"""
)

# UI/UX Designer
Job.objects.create(
    title="UI/UX Designer",
    company="Adobe",
    location="Kolkata",
    salary_range="5-8 LPA",
    created_by=user,
    about="""What You Can Expect

Design intuitive interfaces and improve user experience for creative tools used by millions worldwide. You'll work closely with product managers and engineers to deliver user-centered designs.""",
    responsibilities="""- Create wireframes, prototypes, and design systems
- Conduct user research and usability testing
- Collaborate with developers to implement designs
- Ensure accessibility and design consistency""",
    must_have_skills="Figma, Adobe XD, User Research",
    good_to_have_skills="HTML/CSS, Motion Design, Sketch",
    qualifications="""Bachelor’s in Design, HCI, or related field
2–4 years of UI/UX design experience
Portfolio demonstrating user-centered design""",
    benefits="""Creative workspace
Design conferences
Team outings
Health insurance"""
)

# Cybersecurity Analyst
Job.objects.create(
    title="Cybersecurity Analyst",
    company="Microsoft",
    location="Bangalore",
    salary_range="10-14 LPA",
    created_by=user,
    about="""What You Can Expect

Monitor systems, detect threats, and implement security protocols to protect enterprise applications and data. You'll be part of a global security operations team.""",
    responsibilities="""- Perform vulnerability assessments and penetration testing
- Monitor SIEM dashboards and respond to incidents
- Develop and enforce security policies
- Collaborate with IT teams to secure infrastructure""",
    must_have_skills="Network Security, SIEM Tools, Incident Response",
    good_to_have_skills="Cloud Security, Ethical Hacking, Python",
    qualifications="""Bachelor’s in Information Security or related field
2–5 years of cybersecurity experience
Certifications like CEH, CISSP preferred""",
    benefits="""Certification sponsorship
Health insurance
Remote work options
Career growth opportunities"""
)

# Software Engineer
Job.objects.create(
    title="Software Engineer",
    company="Netflix",
    location="Mumbai",
    salary_range="12-18 LPA",
    created_by=user,
    about="""What You Can Expect

Work on backend systems powering streaming services for millions of users. You'll design scalable APIs, optimize performance, and collaborate across teams to deliver world-class software.""",
    responsibilities="""- Design and implement backend services and APIs
- Optimize database queries and system performance
- Collaborate with frontend and DevOps teams
- Participate in code reviews and architecture discussions""",
    must_have_skills="Java, Python, SQL, REST APIs",
    good_to_have_skills="Microservices, AWS, Kafka, Docker",
    qualifications="""Bachelor’s in Computer Science or related field
2–5 years of software engineering experience
Strong knowledge of distributed systems""",
    benefits="""Hybrid work model
Health insurance
Learning budget
Career growth opportunities"""
)
