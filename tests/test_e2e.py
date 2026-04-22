import re
from playwright.sync_api import Page, expect

aws_url = "https://jcyv6udbtr.eu-west-2.awsapprunner.com/"

def xtest_returns_status_200(page: Page):
    response = page.request.get("http://127.0.0.1:5000")
    expect(response).to_be_ok()

def xtest_deployed_app_returns_status_200(page: Page):
    response = page.request.get(aws_url)
    expect(response).to_be_ok()