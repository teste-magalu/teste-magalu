from jsonschema import Draft4Validator
from datetime import datetime

def validate(data, schema):
    validator = Draft4Validator(schema)
    errors = [error.message for error in validator.iter_errors(data)]
    if errors:
        return False
    return True

def clean_dict(data):
    for key, value in data.items():
        if isinstance(value, dict):
            clean_dict(value)
        else:
            newvalue = value.strip()
            data[key] = newvalue
