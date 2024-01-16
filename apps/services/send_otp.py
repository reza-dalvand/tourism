import logging

from kavenegar import *

from config.env import env

logger = logging.getLogger("main")


def send_sms(receptor, otp):
    try:
        api = KavenegarAPI(env("API_KEY"))
        params = {
            "sender": "",  # optional
            "receptor": receptor,  # multiple mobile number, split by comma
            "message": f"your code: {otp}",
        }
        response = api.verify_lookup(params)
        print(response)
        logger.info(response)
    except APIException as e:
        logger.exception(e)
    except HTTPException as e:
        logger.exception(e)
