import os
from dotenv import load_dotenv

load_dotenv()

SOCIAL_AUTH_SUAP_KEY = os.getenv('SOCIAL_AUTH_SUAP_KEY')
SOCIAL_AUTH_SUAP_SECRET = os.getenv('SOCIAL_AUTH_SUAP_SECRET')