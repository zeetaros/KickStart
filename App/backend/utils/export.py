import json
from bson import json_util

"""
this enables the save of ObjectId to JSON
"""

json_options = json_util.DEFAULT_JSON_OPTIONS.with_options(tz_aware=False, tzinfo=None)


def save_to_file(content, fpath):
    content_str = json_util.dumps(content)
    with open(fpath, "w") as f:
        f.write(content_str)


def load_from_file(fpath):
    with open(fpath, "r") as f:
        content_str = f.read()
    return json_util.loads(content_str, json_options=json_options)
