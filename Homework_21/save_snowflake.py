import json


def save_snowflake(Snowflake, size, shapes, shape):
    snowflake = Snowflake(size, shapes[shape])
    with open('snowflake.json', 'w', encoding='utf-8') as f:
        json.dump(snowflake.add_snowflake(), f, indent=4, ensure_ascii=False)