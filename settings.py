from os import environ
from dotenv import load_dotenv

load_dotenv('.env')
LOGIN = environ['LOGIN']
PASSWORD = environ['PASSWORD']
SEND_ID = environ['SEND_ID']
