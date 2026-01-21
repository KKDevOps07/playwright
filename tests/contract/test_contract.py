import requests
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

def test_html_contract():
    r = requests.get(BASE_URL)
    html = r.text.lower()

    assert "<html" in html
    assert "<body" in html
