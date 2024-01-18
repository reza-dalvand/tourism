from datetime import datetime, timedelta
from random import randint


def generate_otp_code():
    otp_code = randint(1000, 9999)
    return otp_code


def check_expire_otp(user):
    now = datetime.now()
    expire_time = user.otp_create_time + timedelta(seconds=125)
    if now > expire_time:
        return False
    return True
