import datetime
from unittest.mock import patch
from fortunecookiecravaggio.fortune import fortune_of_the_day

def test_fortune_of_the_day_returns_expected():
    fortune = fortune_of_the_day()
    assert isinstance(fortune, str), "Expected a string fortune"
    # Test that the fortune is not empty:
    assert fortune.strip(), "Expected a non-empty fortune string"

def test_fortune_of_the_day_consistent_for_same_date():
    # We'll choose a specific date to mock
    test_date = datetime.date(2025, 3, 15)
    
    with patch("fortunecookiecravaggio.fortune.date") as mock_date:
        # Mock date.today() -> test_date
        mock_date.today.return_value = test_date
        mock_date.return_value.toordinal.return_value = test_date.toordinal()
        
        # Call the function multiple times, should be the same fortune
        fortune1 = fortune_of_the_day()
        fortune2 = fortune_of_the_day()
    
    assert fortune1 == fortune2, "Expected the same fortune for the same date"


def test_fortune_of_the_day_different_for_different_dates():
    test_date_1 = datetime.date(2025, 3, 15)
    test_date_2 = datetime.date(2025, 3, 16)
    
    with patch("fortunecookiecravaggio.fortune.date") as mock_date:
        # Mock first date
        mock_date.today.return_value = test_date_1
        mock_date.return_value.toordinal.return_value = test_date_1.toordinal()
        fortune_day_1 = fortune_of_the_day()
    
    with patch("fortunecookiecravaggio.fortune.date") as mock_date:
        # Mock second date
        mock_date.today.return_value = test_date_2
        mock_date.return_value.toordinal.return_value = test_date_2.toordinal()
        fortune_day_2 = fortune_of_the_day()

    assert fortune_day_1 != fortune_day_2, (
        "Expected different fortunes for different dates, but got the same"
    )
