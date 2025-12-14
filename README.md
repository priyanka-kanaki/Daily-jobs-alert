# Daily Job Alert

A Python automation project that **searches for fresher jobs and internships** in Data Analytics and Python development and **sends daily email alerts**. The project runs automatically every day at 12 PM IST using **GitHub Actions**.

---

## Features

- Searches for jobs and internships from platforms like **LinkedIn, Indeed, Naukri, Internshala, Wellfound**.
- Filters for **fresher roles** or experience “0–1 years”.
- Collects:
  - Job Title
  - Company Name
  - Location
  - Experience required
  - Job Type
  - Posted date
  - Direct Apply Link
- Sends a **daily email summary** with Python and Data Analytics job sections.
- Fully automated via **GitHub Actions**, no manual intervention needed.

---



## 🛠 Requirements

- Python 3.10+
- GitHub account for Actions
- Gmail account (with **App Password**) for sending emails
- Google API Key for Custom Search

---




## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/priyanka-kanaki/daily-jobs-alert.git
cd daily-jobs-alert
```


2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```



## 🔑 Setup

**1. GitHub Secrets**

Go to your repo → Settings → Secrets → Actions and add:

| Secret Name      | Secret Value                          |
|-----------------|---------------------------------------|
| EMAIL            | Your Gmail address                     |
| PASSWORD         | Gmail App Password (16 chars)         |
| GOOGLE_API_KEY   | Google API Key for Custom Search      |
| GOOGLE_CSE_ID    | Custom Search Engine ID               |

Do not store secrets directly in the repo or .env file.



**2. Workflow**

The GitHub Actions workflow runs daily at 12 PM IST and triggers the Python script automatically.
You can also run it manually via Actions → Run workflow.



## ▶️ Usage

To test locally:
```bash
python main.py
```



The script will fetch the latest fresher jobs and send an email to the configured Gmail account.

**🔒 Security**

- All sensitive credentials are stored in GitHub Secrets, never in the repo.
- .env and venv/ are ignored in .gitignore.



**⚠️ Notes**

- Gmail App Password is required because Google blocks normal password login from scripts.
- Make sure your Google API Key and CSE ID are valid and restricted to your project.
- Workflow runs automatically every day, but you can trigger it manually if needed.
