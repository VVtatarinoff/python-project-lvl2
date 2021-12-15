import json


def generate_json(comparison):
    if not comparison:
        return ""
    return json.dumps(comparison, sort_keys=True, indent=4)
