import requests, os
from dotenv import load_dotenv

load_dotenv()

class AOCInput:
    def __init__(self, year, day, actual=True):
        self.year = year
        self.day = day
        self.url = f'https://adventofcode.com/{year}/day/{day}/input'
        self.actual = actual

    def lines(self):
        if not self.actual:
            with open('../input', 'r') as f:
                for line in f:
                    yield line.strip()
        else:
            cookie = os.getenv("AOC_COOKIE")
            if not cookie:
                raise EnvironmentError("AOC_COOKIE not set in environment or .env")
            response = requests.get(self.url, headers={'Cookie': f'session={cookie}'})
            if response.status_code != 200:
                raise ConnectionError('Something went wrong getting input.')

            for line in response.iter_lines(decode_unicode=True):
                yield line.strip()