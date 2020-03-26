import logging
import json


def main(val: str) -> str:
    values = ['one', 'two', 'three', 'four', 'five']
    return json.dumps(values)
