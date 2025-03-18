
import datetime 
from unittest.mock import patch 
from fortunecookiecravaggio.fortune import fortune_of_the_day

def test_fortune_of_the_day_returns_expected():
    fortune = fortune_of_the_day()
    assert isinstance(fortune, str), "Expected a string fortune"
    # test the fortune is not empty:
    assert fortune.strip(), "Expected a non-empty fortune string"

def test_fortune_of_the_day_consistent_for_same_date():
    # We'll choose a specific date to mock
    test_date = datetime.date(2025, 3, 15)
    
    with patch("fortunecookiecravaggio.fortune.date") as mock_date:
        # Mock date.today() -> test_date
        mock_date.today.return_value = test_date
        mock_date.today.return_value.toordinal.return_value = test_date.toordinal()
        
        # Call the function multiple times, should be the same fortune
        fortune1 = fortune_of_the_day()
        fortune2 = fortune_of_the_day()
    
    assert fortune1 == fortune2, "Expected the same fortune for the same date"