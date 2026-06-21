from json_lingo import JsonLingo, load_json_file, save_json_file
import pytest

def test_translate_json():
    language_map = {'en': {'hello': 'hola'}, 'es': {'hola': 'hello'}}
    json_lingo = JsonLingo(language_map)
    json_data = {'greeting': 'hello', 'nested': {'message': 'hello'}}
    translated_json = json_lingo.translate(json_data, 'en', 'es').translated_json
    assert translated_json == {'greeting': 'hola', 'nested': {'message': 'hola'}}

def test_translate_text():
    language_map = {'en': {'hello': 'hola'}, 'es': {'hola': 'hello'}}
    json_lingo = JsonLingo(language_map)
    translated_text = json_lingo._translate_text('hello', 'en', 'es')
    assert translated_text == 'hola'

def test_calculate_accuracy():
    language_map = {'en': {'hello': 'hola'}, 'es': {'hola': 'hello'}}
    json_lingo = JsonLingo(language_map)
    original_json = {'greeting': 'hello', 'nested': {'message': 'hello'}}
    translated_json = json_lingo.translate(original_json, 'en', 'es').translated_json
    accuracy = json_lingo._calculate_accuracy(original_json, translated_json)
    assert accuracy == 1.0

def test_load_json_file():
    json_data = {'key': 'value'}
    with open('test.json', 'w') as file:
        import json
        json.dump(json_data, file)
    loaded_json = load_json_file('test.json')
    assert loaded_json == json_data

def test_save_json_file():
    json_data = {'key': 'value'}
    save_json_file('test.json', json_data)
    with open('test.json', 'r') as file:
        import json
        loaded_json = json.load(file)
    assert loaded_json == json_data
