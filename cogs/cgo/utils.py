import json
import random

def get_random_cgo_quote() -> str:
    with open("data.json", "r") as file:
        quotes = json.load(file)

    return random.choice(quotes)
