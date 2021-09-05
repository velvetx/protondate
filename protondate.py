import sys
from src import logic


class Program:
    def __init__(self):
        self.target_email = sys.argv[1]
        self.result = None
        self.execution()

    def get_result(self):
        self.result = logic.Logic(self.target_email).execution()

    def get_output(self):
        print(f'Email: {self.target_email}\nTime of creation: {self.result[0]}\nDate of creation: {self.result[1]}')

    def execution(self):
        try:
            self.get_result()
            self.get_output()
        except IndexError:
            print('Bad email.')
        except KeyboardInterrupt:
            pass
        sys.exit(0)


if __name__ == '__main__':
    Program()
