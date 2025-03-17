import pytest
import hashlib
from fortunecookiecravaggio.fortune import get_fortune, load_fortunes

fortunes = [
    "Keep your eye out for someone special.",
    "You are very talented in many ways.",
    "A stranger, is a friend you have not spoken to yet.",
    "A new voyage will fill your life with untold memories.",
    "You will travel to many exotic places in your lifetime.",
    "Your ability for accomplishment will follow with success.",
    "Nothing astonishes men so much as common sense and plain dealing.",
    "Its amazing how much good you can do if you dont care who gets the credit.",
    "Everyone agrees. You are the best.",
    "LIFE CONSIST NOT IN HOLDING GOOD CARDS, BUT IN PLAYING THOSE YOU HOLD WELL.",
    "Jealousy doesn't open doors, it closes them!",
    "It's better to be alone sometimes.",
    "When fear hurts you, conquer it and defeat it!",
    "Let the deeds speak."
]

@pytest.fixture
def test_fortunes(tmp_path):
    #Creates a temporary mock fortunes file for testing.
    file_path = tmp_path / "test_fortunes.txt"
    file_path.write_text("\n".join(fortunes), encoding="utf-8")
    return str(file_path)

def test_get_fortune_valid_input(test_fortunes):
    #Test if get_fortune returns a valid fortune from the file.
    user_input = "test"
    fortune = get_fortune(user_input, test_fortunes)
    assert fortune in fortunes, "Returned fortune should be from the predefined list"

def test_get_fortune_file_not_found():
    #Test if get_fortune handles a missing file gracefully.
    error_message = get_fortune("randominput", "non_existent_file.txt")
    assert error_message == "Error: Fortune file not found. Please create a 'fortunes.txt' file.", \
        "Should return an error message when the file is missing"

def test_get_fortune_different_inputs(test_fortunes):
    #Test if different inputs generate different fortunes (most of the time).
    fortune1 = get_fortune("inputone", test_fortunes)
    fortune2 = get_fortune("inputtwo", test_fortunes)
    assert fortune1 != fortune2 or len(fortunes) == 1, \
        "Different inputs should usually produce different fortunes unless the list is very small"

def test_get_fortune_same_input(test_fortunes):
    #Test if different inputs generate different fortunes (most of the time).
    fortune1 = get_fortune("sameinput", test_fortunes)
    fortune2 = get_fortune("sameinput", test_fortunes)
    assert fortune1 == fortune2, "Same input should produce the same fortune"
