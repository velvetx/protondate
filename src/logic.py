import re
import requests
from datetime import datetime


class Logic:
    def __init__(self, email):
        self.target_email = email
        self.url = 'https://api.protonmail.ch/pks/lookup?op=index&search='
        self.req_body = None
        self.timestamp = None

    def get_request_body(self):
        self.req_body = requests.get(self.url + self.target_email).text

    def get_regex(self):
        self.timestamp = int(re.findall(r'\d{10}', self.req_body)[0])

    def converts_timestamp(self):
        time = datetime.fromtimestamp(self.timestamp).time()
        date = datetime.fromtimestamp(self.timestamp).date().strftime("%d-%m-%Y")
        return time, date

    def execution(self):
        self.get_request_body()
        self.get_regex()
        return self.converts_timestamp()
