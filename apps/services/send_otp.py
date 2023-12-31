import logging

from kavenegar import *

from config.env import env

logger = logging.getLogger("main")


def send_sms(receptor, message):
    try:
        api = KavenegarAPI(env("API_KEY"))
        params = {
            "sender": "",  # optional
            "receptor": receptor,  # multiple mobile number, split by comma
            "message": message,
        }
        response = api.verify_lookup(params)
        logger.info(response)
    except APIException as e:
        logger.exception(e)
    except HTTPException as e:
        logger.exception(e)
