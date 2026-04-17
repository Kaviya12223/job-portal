import React, { useEffect, useState } from 'react';
import { NavLink, useParams } from 'react-router-dom';

export default function ApplyJobPage() {
  const { jobId } = useParams();
  const userId = localStorage.getItem("userId");
  const [job, setJob] = useState(null);
  const [message, setMessage] = useState(null);
  const [isPending, setIsPending] = useState(false);

  // Fetch job details when page loads
  useEffect(() => {
    async function fetchJob() {
      try {
        const res = await fetch(`http://127.0.0.1:8000/api/jobs/${jobId}/`);
        const data = await res.json();
        setJob(data);
      } catch (err) {
        console.error("Failed to load job details", err);
      }
    }
    fetchJob();
  }, [jobId]);

  // Apply action
  async function handleApply(e) {
    e.preventDefault();
    setIsPending(true);
    try {
      const res = await fetch('http://127.0.0.1:8000/apply', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ job: jobId, applicant: userId })
      });
      const data = await res.json();
      if (res.ok) {
        setMessage({ text: data.message, success: true });
      } else {
        setMessage({ text: data.message, success: false });
      }
    } catch (err) {
      setMessage({ text: "Failed to apply", success: false });
    }
    setIsPending(false);
  }

  return (
    <div className="min-h-screen bg-gray-50 text-gray-800 flex flex-col">
      <header className="border-b bg-white">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3">
          <h1 className="text-xl font-bold text-blue-700">JobPortal</h1>
          <nav className="hidden md:flex gap-6 text-sm font-medium text-gray-700">
            <NavLink to="/jobs" className="hover:text-blue-700">Jobs</NavLink>
            <NavLink to="/companies" className="hover:text-blue-700">Companies</NavLink>
            <NavLink to="/applications" className="hover:text-blue-700">My Applications</NavLink>
          </nav>
          <div className="flex items-center gap-4">
            <span className="text-sm text-gray-600">Hello, Logesh</span>
            <div className="flex h-8 w-8 items-center justify-center rounded-full bg-blue-700 text-sm font-semibold text-white">
              L
            </div>
          </div>
        </div>
      </header>

      <main className="min-h-[calc(100vh-140px)] px-4">
        <div className="max-w-7xl mx-auto pt-6">
          <NavLink
            to="/jobs"
            className="inline-flex items-center gap-2 mb-4 text-sm font-medium text-blue-600 hover:text-blue-700 hover:underline"
          >
            ← Back to Jobs
          </NavLink>
        </div>

        <div className="flex items-center justify-center py-10">
          <div className="w-full max-w-2xl rounded-lg border bg-white p-6">
            {job ? (
              <>
                <h2 className="text-2xl font-semibold text-gray-900">{job.title}</h2>
                <p className="mt-1 text-sm text-gray-600">{job.company} • {job.location}</p>
                <p className="mt-1 text-sm text-gray-600">Salary: {job.salary_range}</p>

                <div className="mt-4 text-gray-700 leading-relaxed">
                  <h3 className="font-semibold mb-2">About the job</h3>
                  <p>{job.about}</p>

                  <h3 className="font-semibold mt-4 mb-2">Responsibilities</h3>
                  <p>{job.responsibilities}</p>

                  <h3 className="font-semibold mt-4 mb-2">Must Have Skills</h3>
                  <p>{job.must_have_skills}</p>

                  <h3 className="font-semibold mt-4 mb-2">Good To Have Skills</h3>
                  <p>{job.good_to_have_skills}</p>

                  <h3 className="font-semibold mt-4 mb-2">Qualifications</h3>
                  <p>{job.qualifications}</p>

                  <h3 className="font-semibold mt-4 mb-2">Benefits</h3>
                  <p>{job.benefits}</p>
                </div>

                <form onSubmit={handleApply} className="mt-6 space-y-4">
                  <button
                    type="submit"
                    className="w-full rounded-lg bg-blue-700 py-2.5 font-semibold text-white hover:bg-blue-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
                  >
                    {isPending ? "Applying..." : "Apply Now"}
                  </button>
                  {message && (
                    <p className={`text-center text-sm ${message.success ? "text-green-600" : "text-red-600"}`}>
                      {message.text}
                    </p>
                  )}
                </form>
              </>
            ) : (
              <p>Loading job details...</p>
            )}
          </div>
        </div>
      </main>

      <footer className="border-t bg-white">
        <div className="mx-auto max-w-7xl px-4 py-6 text-center text-sm text-gray-500">
          © 2026 JobPortal.com | All rights reserved
        </div>
      </footer>
    </div>
  );
}
