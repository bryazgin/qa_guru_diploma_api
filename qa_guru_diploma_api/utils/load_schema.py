import json
import os


def load_schema(filepath):
    with open(os.path.dirname(os.path.dirname(__file__)) + 'qa_guru_diploma_api/json_schemas/' + filepath) as file:
        schema = json.load(file)
        return schema
