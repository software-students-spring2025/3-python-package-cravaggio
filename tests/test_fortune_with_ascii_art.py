import pytest
from src.fortunecookiecravaggio.fortune import fortune_with_ascii_art

def test_fortune_returns_string():
    """Test that fortune_with_ascii_art() returns a string."""
    result = fortune_with_ascii_art()
    assert isinstance(result, str), "Output should be a string"

def test_fortune_contains_fortune_text():
    """Test that output contains '🍀 Fortune:' followed by a message."""
    result = fortune_with_ascii_art()
    assert "🍀 Fortune:" in result, "Output should contain the fortune header"

def test_fortune_contains_ascii_art():
    """Test that the output contains multiple lines (ASCII art + fortune)."""
    result = fortune_with_ascii_art()
    lines = result.split("\n")
    assert len(lines) > 2, "Output should have ASCII art with multiple lines"
