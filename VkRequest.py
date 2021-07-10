import datetime
from typing import Union
from time import sleep

from vk_messages import MessagesAPI
from vk_messages.utils import get_random
import vk_api


class VkRequest:
    def __init__(self, login, password, domain: str, words: Union[list, set], notification_id, delay):
        self.login = login
        self.password = password
        self.domain = domain
        self.words = words
        self.delay = delay
        self.notification_id = notification_id
        self.messages = MessagesAPI(login=self.login,
                                    password=self.password,
                                    two_factor=False,
                                    cookies_save_path='sessions/')
        self.vk_session = vk_api.VkApi(self.login, self.password)
        self.vk_session.auth()
        self.check_post_id = []
        self.vk = self.vk_session.get_api()
        self.last_post = None
        self.last_post_text = None
        self.last_post_id = None
        self.update_data()
        self.check_words()

    def get_last_post(self):
        return self.vk.wall.get(domain=self.domain, count=1)

    def get_last_post_text(self):
        return self.last_post['items'][0]['text']

    def get_last_post_id(self):
        return self.last_post['items'][0]['id']

    def update_data(self):
        self.last_post = self.get_last_post()
        self.last_post_text = self.get_last_post_text()
        self.last_post_id = self.get_last_post_id()

    def check_words(self):
        for word in self.words:
            if self.last_post_id in self.check_post_id:
                continue
            else:
                if word.lower() in self.last_post_text.lower():
                    self.send_alarm(word)
                    sleep(1)
        self.check_post_id.append(self.last_post_id)

    def get_last_post_signer_id(self):
        try:
            return self.last_post['items'][0]['signer_id']
        except KeyError:
            return

    def get_time(self):
        return datetime.datetime.fromtimestamp(self.last_post['items'][0]['date'])

    def send_alarm(self, word):
        message_to_send = f'В группе vk.com/{self.domain} в {self.get_time()} была опубликована запись ' \
                          f'содержащая слово "{word.lower()}"'
        self.messages.method(name='messages.send',
                                  peer_id=self.notification_id,
                                  message=message_to_send,
                                  random_id=get_random()
                             )

    def start_bot(self):
        while True:
            sleep(self.delay)
            self.update_data()
            print(f'Получены новые данные в {datetime.datetime.now().strftime("<%d-%m-%Y %H:%M:%S> ")}')
            self.check_words()