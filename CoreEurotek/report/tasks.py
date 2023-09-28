from celery import shared_task
from report.auth.otp import generate_otp
import time


@shared_task
def get_otp_code() -> str:
    otp_code = generate_otp()
    time.sleep(3)
    return otp_code
