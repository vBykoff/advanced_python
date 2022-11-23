"""Json parser"""
import json


def keyword_handler(keyword):
    """Default function for parse_json"""
    return keyword


def parse_json(json_str: str, required_fields=None,
               keywords=None, keyword_callback=keyword_handler):
    """Find keywords in required fields in json string
    and execute keyword_callback for each of them"""
    if keyword_callback is None:
        keyword_callback=keyword_handler
    result = []
    json_doc = json.loads(json_str)
    for field in json_doc:
        if field in required_fields:
            for key in json_doc[field].split():
                if key in keywords:
                    key = keyword_callback(key)
                    result.append(key)
    return result


if __name__ == "__main__":

    parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
               required_fields=["key1"], keywords=["word2"])
