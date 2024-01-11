import json


def get_shape():
    with open('snowflake shape.json', encoding='utf-8') as file:
        shapes = json.load(file)
        return shapes['shapes']