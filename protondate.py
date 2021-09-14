import sys
import requests
import re
from datetime import datetime


class ProtonDate:
    def __init__(self):
        try:
            self.target_email = sys.argv[1]
            time, date = self.convert_timestamp()
            print(f'Email: {self.target_email}\nTime of creation: {time}\nDate of creation: {date}')
            sys.exit(0)
        except IndexError:
            print('Bad email.')

    def get_api_request(self):
        return requests.get('https://api.protonmail.ch/pks/lookup?op=index&search=' + self.target_email).text

    def convert_timestamp(self):
        timestamp = int(re.search(r'\d{10}', self.get_api_request()).group())
        return datetime.fromtimestamp(timestamp).time(), datetime.fromtimestamp(timestamp).date().strftime("%d-%m-%Y")


if __name__ == '__main__':
    ProtonDate()
