import logging

from kavenegar import *

from apps.utils.generate_otp import generate_otp_code
from config.env import env

logger = logging.getLogger("main")


def save_and_return_otp(user):
    otp_code = generate_otp_code()
    user.otp = otp_code
    user.save()
    return otp_code


def send_otp_code(receptor):
    try:
        otp_code = save_and_return_otp(receptor)
        api = KavenegarAPI(env("API_KEY"))
        params = {
            "sender": "",  # optional
            "receptor": receptor.mobile,  # multiple mobile number, split by comma
            "message": f"your code: {otp_code}",
        }
        response = api.verify_lookup(params)
        logger.info(response)
    except APIException as e:
        logger.exception(e)
    except HTTPException as e:
        logger.exception(e)
