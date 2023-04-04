# import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


def english_to_french(englishtext):
    try:
        auth = IAMAuthenticator(apikey)
        lananuage_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=auth)
        lananuage_translator.set_service_url(url)
        french_text = lananuage_translator.translate(text=englishtext, model_id="en-fr") \
            .get_result()["translations"][0]["translation"]

        return french_text

    except:
        return None


def french_to_english(frenchtext):
    try:
        auth = IAMAuthenticator(apikey)
        lananuage_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=auth)
        lananuage_translator.set_service_url(url)
        english_text = lananuage_translator.translate(text=frenchtext, model_id="fr-en") \
            .get_result()["translations"][0]["translation"]

        return english_text
    except:
        return None
