from settings import *
from VkRequest import VkRequest

words_list = ['Нервы', 'Джизус', 'Пошлая Молли']

vkr = VkRequest(login=LOGIN, password=PASSWORD, domain='vdksell', words=words_list, notification_id=SEND_ID, delay=900)
vkr.start_bot()
