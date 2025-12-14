def is_fresher(text):
    keywords = ["fresher", "intern", "0-1", "entry"]
    return any(k in text.lower() for k in keywords)

def format_jobs_html(jobs):
    if not jobs:
        return None

    python_jobs = [j for j in jobs if "python" in j['title'].lower()]
    data_jobs = [j for j in jobs if "data" in j['title'].lower() or "analytics" in j['title'].lower()]

    html = "<html><body>"
    html += "<h2>Daily Fresher Job Alert</h2>"

    if python_jobs:
        html += "<h3>Python Developer Roles</h3><ul>"
        for job in python_jobs:
            html += f"<li><b>{job['title']}</b> at {job['company']}<br>"
            html += f"<a href='{job['link']}'>Apply Here</a></li><br>"
        html += "</ul>"

    if data_jobs:
        html += "<h3>Data Analytics / Data Analyst Roles</h3><ul>"
        for job in data_jobs:
            html += f"<li><b>{job['title']}</b> at {job['company']}<br>"
            html += f"<a href='{job['link']}'>Apply Here</a></li><br>"
        html += "</ul>"

    html += "</body></html>"
    return html
