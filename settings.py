from os import environ
from dotenv import load_dotenv
from create_files import *


class CannotReadFileException(Exception):
    pass


check_files()
load_dotenv('.env')
LOGIN = environ['LOGIN']
PASSWORD = environ['PASSWORD']
SEND_ID = environ['SEND_ID']
if LOGIN == '':
    raise CannotReadFileException("Add LOGIN in .env")
if PASSWORD == '':
    raise CannotReadFileException("Add PASSWORD in .env")
if SEND_ID == '':
    raise CannotReadFileException("Add SEND_ID in .env")
