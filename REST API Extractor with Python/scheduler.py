import schedule
import time
from script import run_stock_job

from datetime import datetime

def basic_job():
    print("Job started at:", datetime.now())

# schedule the jobs
schedule.every(1).minutes.do(basic_job)
schedule.every(1).minutes.do(run_stock_job)

# start execution
while True:
    schedule.run_pending()
    time.sleep(1)