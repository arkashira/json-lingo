import json
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class TranslationResult:
    translated_json: Dict[str, Any]
    accuracy: float

class JsonLingo:
    def __init__(self, language_map: Dict[str, Dict[str, str]]):
        self.language_map = language_map

    def translate(self, json_data: Dict[str, Any], source_language: str, target_language: str) -> TranslationResult:
        translated_json = self._translate_json(json_data, source_language, target_language)
        accuracy = self._calculate_accuracy(json_data, translated_json)
        return TranslationResult(translated_json, accuracy)

    def _translate_json(self, json_data: Dict[str, Any], source_language: str, target_language: str) -> Dict[str, Any]:
        translated_json = {}
        for key, value in json_data.items():
            if isinstance(value, str):
                translated_json[key] = self._translate_text(value, source_language, target_language)
            elif isinstance(value, dict):
                translated_json[key] = self._translate_json(value, source_language, target_language)
            else:
                translated_json[key] = value
        return translated_json

    def _translate_text(self, text: str, source_language: str, target_language: str) -> str:
        # Simple translation logic for demonstration purposes
        if source_language == 'en' and target_language == 'es':
            return text.replace('hello', 'hola')
        elif source_language == 'es' and target_language == 'en':
            return text.replace('hola', 'hello')
        else:
            raise ValueError('Unsupported language pair')

    def _calculate_accuracy(self, original_json: Dict[str, Any], translated_json: Dict[str, Any]) -> float:
        # Simple accuracy calculation for demonstration purposes
        accurate_keys = 0
        for key, value in original_json.items():
            if isinstance(value, str):
                if translated_json[key] == self._translate_text(value, 'en', 'es'):
                    accurate_keys += 1
            elif isinstance(value, dict):
                accurate_keys += self._calculate_accuracy(value, translated_json[key])
        return accurate_keys / len(original_json)

def load_json_file(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(file_path: str, json_data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)
