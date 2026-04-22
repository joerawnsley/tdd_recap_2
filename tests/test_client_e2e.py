from app import app
import db

test_app = app.test_client()

mock_duties = [
    {"identifier": 1,
     "description": "Script and Code"},
    {"identifier": 2,
     "description": "Deploy Continuously"},
]

def get_home_page(mocker):    
    mocker.patch("db.get_duties", return_value=mock_duties)
    response = test_app.get("/")
    return response


def test_home_page_has_page_content(mocker):
    assert "title" in get_home_page(mocker).text

def test_home_page_contains_duty_1_description(mocker):
    assert "Script and code" in get_home_page(mocker).text
    
def test_page_is_populated_with_duties_from_db(mocker):
    assert get_home_page(mocker).text.count("li") > 1
    assert "Script and code" in get_home_page(mocker).text