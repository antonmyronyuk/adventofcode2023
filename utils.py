import os

import requests
from dotenv import load_dotenv

load_dotenv()


def read_input(day: int, year: int = 2023) -> str:
    response = requests.get(
        url=f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": os.getenv("SESSION")}
    )
    response.raise_for_status()
    return response.text
