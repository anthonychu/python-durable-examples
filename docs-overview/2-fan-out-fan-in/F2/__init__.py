import json
import logging


def main(val: str) -> str:
    return json.dumps(len(val))
