
import inspect
import main

def test_check_function_exists():
    assert hasattr(main, "check_fields")

def test_password_masked():
    source = inspect.getsource(main)
    assert 'show="*"' in source or "show='*'" in source

def test_submit_button_present():
    source = inspect.getsource(main)
    assert "Button" in source

def test_entries_present():
    source = inspect.getsource(main)
    assert source.count("Entry") >= 3
