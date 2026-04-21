from app import list_duties

def test_list_duties():
    duty_1_text = list_duties([1])
    assert "Duty 1" in duty_1_text