from app import app
import webbrowser
from pathlib import Path
import json

with open('mock_data/duties.json') as duties:
    mock_duties = json.load(duties)

test_app = app.test_client()



def get_home_page(mocker):    
    mocker.patch("db.get_duties", return_value=mock_duties)
    response = test_app.get("/")
    return response

def test_display_home_page(mocker):
    html_content = get_home_page(mocker).text
    output_dir = Path("test_output")
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / "home_page_preview.html"
    file_path.write_text(html_content)
    webbrowser.open(f"file://{file_path.absolute()}")
    assert file_path.exists()

def test_home_page_has_page_content(mocker):
    assert "title" in get_home_page(mocker).text

def test_home_page_contains_duty_1_description(mocker):
    assert "Script and code" in get_home_page(mocker).text
    
def test_page_is_populated_with_duties_from_db(mocker):
    assert get_home_page(mocker).text.count("li") > 1
    assert "Script and code" in get_home_page(mocker).text
