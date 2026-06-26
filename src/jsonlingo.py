import json
import argparse
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class JsonSchema:
    keys: Dict[str, type]

def load_json_schema(file_path: str) -> JsonSchema:
    with open(file_path, 'r') as file:
        data = json.load(file)
    keys = {key: type(value) for key, value in data.items()}
    return JsonSchema(keys)

def validate_json_file(file_path: str, schema: JsonSchema) -> bool:
    with open(file_path, 'r') as file:
        data = json.load(file)
    for key, value_type in schema.keys.items():
        if key not in data:
            print(f"Key '{key}' missing in {file_path}")
            return False
        if not isinstance(data[key], value_type):
            print(f"Type mismatch for key '{key}' in {file_path}: expected {value_type.__name__}, got {type(data[key]).__name__}")
            return False
    return True

def main():
    parser = argparse.ArgumentParser(description='Validate JSON files against a schema')
    parser.add_argument('schema_file', help='Path to the source JSON schema file')
    parser.add_argument('translation_file', help='Path to the translated JSON file')
    args = parser.parse_args()
    schema = load_json_schema(args.schema_file)
    if not validate_json_file(args.translation_file, schema):
        exit(1)

if __name__ == '__main__':
    main()
