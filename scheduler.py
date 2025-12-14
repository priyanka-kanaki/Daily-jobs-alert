from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_job  # import the function

scheduler = BlockingScheduler(timezone="Asia/Kolkata")
scheduler.add_job(run_job, 'cron', hour=12, minute=0)  # now it’s a callable
scheduler.start()
