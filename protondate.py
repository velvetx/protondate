import sys
import requests
import re
from datetime import datetime


class ProtonDate:
    def __init__(self):
        self.target_email = sys.argv[1]
        self.api_url = 'https://api.protonmail.ch/pks/lookup?op=index&search='
        self.req_body = None
        self.timestamp = None
        self.time, self.date = None, None
        self.execute()

    def get_request_body(self):
        self.req_body = requests.get(self.api_url + self.target_email).text

    def find_timestamp(self):
        self.timestamp = int(re.findall(r'\d{10}', self.req_body)[0])

    def convert_timestamp(self):
        self.time = datetime.fromtimestamp(self.timestamp).time()
        self.date = datetime.fromtimestamp(self.timestamp).date().strftime("%d-%m-%Y")

    def execute(self):
        try:
            self.get_request_body()
            self.find_timestamp()
            self.convert_timestamp()
            print(f'Email: {self.target_email}\nTime of creation: {self.time}\nDate of creation: {self.date}')
        except IndexError:
            print('Bad email.')
        except KeyboardInterrupt:
            pass
        sys.exit(0)


if __name__ == '__main__':
    ProtonDate()
