import json
from jsonlingo import load_json_schema, validate_json_file
import pytest
import tempfile
import os

def test_load_json_schema():
    with tempfile.NamedTemporaryFile(mode='w') as tmp:
        json.dump({'a': 1, 'b': '2'}, tmp)
        tmp.flush()
        schema = load_json_schema(tmp.name)
        assert schema.keys == {'a': int, 'b': str}

def test_validate_json_file_valid():
    with tempfile.NamedTemporaryFile(mode='w') as schema_tmp, tempfile.NamedTemporaryFile(mode='w') as translation_tmp:
        json.dump({'a': 1, 'b': '2'}, schema_tmp)
        json.dump({'a': 2, 'b': '3'}, translation_tmp)
        schema_tmp.flush()
        translation_tmp.flush()
        assert validate_json_file(translation_tmp.name, load_json_schema(schema_tmp.name))

def test_validate_json_file_missing_key():
    with tempfile.NamedTemporaryFile(mode='w') as schema_tmp, tempfile.NamedTemporaryFile(mode='w') as translation_tmp:
        json.dump({'a': 1, 'b': '2'}, schema_tmp)
        json.dump({'a': 2}, translation_tmp)
        schema_tmp.flush()
        translation_tmp.flush()
        assert not validate_json_file(translation_tmp.name, load_json_schema(schema_tmp.name))

def test_validate_json_file_type_mismatch():
    with tempfile.NamedTemporaryFile(mode='w') as schema_tmp, tempfile.NamedTemporaryFile(mode='w') as translation_tmp:
        json.dump({'a': 1, 'b': '2'}, schema_tmp)
        json.dump({'a': '2', 'b': '3'}, translation_tmp)
        schema_tmp.flush()
        translation_tmp.flush()
        assert not validate_json_file(translation_tmp.name, load_json_schema(schema_tmp.name))

def test_main_valid(capsys):
    with tempfile.NamedTemporaryFile(mode='w') as schema_tmp, tempfile.NamedTemporaryFile(mode='w') as translation_tmp:
        json.dump({'a': 1, 'b': '2'}, schema_tmp)
        json.dump({'a': 2, 'b': '3'}, translation_tmp)
        schema_tmp.flush()
        translation_tmp.flush()
        import sys
        sys.argv = ['jsonlingo', schema_tmp.name, translation_tmp.name]
        from jsonlingo import main
        main()
        captured = capsys.readouterr()
        assert captured.out == ''

def test_main_invalid(capsys):
    with tempfile.NamedTemporaryFile(mode='w') as schema_tmp, tempfile.NamedTemporaryFile(mode='w') as translation_tmp:
        json.dump({'a': 1, 'b': '2'}, schema_tmp)
        json.dump({'a': '2', 'b': '3'}, translation_tmp)
        schema_tmp.flush()
        translation_tmp.flush()
        import sys
        sys.argv = ['jsonlingo', schema_tmp.name, translation_tmp.name]
        from jsonlingo import main
        with pytest.raises(SystemExit):
            main()
        captured = capsys.readouterr()
        assert 'Type mismatch' in captured.out
