import os
import pytest
from fortunecookiecravaggio.fortune import custom_fortune

# This fixture overrides the file path so that fortunes.txt is created in a temporary directory.
@pytest.fixture(autouse=True)
def isolated_fortunes_file(tmp_path, monkeypatch):
    # Override os.path.join used in the fortune module so that it returns a path in tmp_path.
    monkeypatch.setattr(
        "fortunecookiecravaggio.fortune.os.path.join",
        lambda a, b: str(tmp_path / b)
    )
    file_path = tmp_path / "fortunes.txt"
    # Ensure the file does not exist initially.
    if file_path.exists():
        file_path.unlink()
    return file_path

def test_custom_fortune_valid(isolated_fortunes_file):
    # Test that a valid fortune message is returned and appended to the file.
    message = "This is a test fortune."
    result = custom_fortune(message)
    # The function should return the stripped message.
    assert result == message.strip()
    
    # Verify that the message has been written to the temporary fortunes.txt file.
    with open(isolated_fortunes_file, "r", encoding="utf-8") as f:
        content = f.read()
    # The file should contain the message followed by a newline.
    assert message in content

def test_custom_fortune_empty_message(isolated_fortunes_file):
    # Test that passing an empty (or whitespace-only) message raises a ValueError.
    with pytest.raises(ValueError):
        custom_fortune("   ")

'''
command: pytest
export PYTHONPATH=./src
python3 -m pytest --maxfail=1 --disable-warnings -q
'''