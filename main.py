from job_search import search_jobs
from formatter import is_fresher, format_jobs_html
from emailer import send_email
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()

def run_job():
    queries = [
        "Python Developer fresher jobs India",
        "Python Developer internship India",
        "Data Analyst fresher jobs India",
        "Data Analyst internship India"
    ]

    all_jobs = []

    for q in queries:
        results = search_jobs(q)
        for r in results:
            text = r["title"] + r.get("snippet", "")
            if is_fresher(text):
                all_jobs.append({
                    "title": r["title"],
                    "link": r["link"],
                    "company": r.get("displayLink")
                })

    content = format_jobs_html(all_jobs)

    subject = f"Daily Python & Data Analytics Fresher Job Updates – {date.today()}"

    if content:
        send_email(subject, content, is_html=True)
    else:
        send_email(subject, "No new fresher opportunities found today. Will recheck tomorrow at 12 PM.")

if __name__ == "__main__":
    run_job()
