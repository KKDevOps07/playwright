import requests
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

def test_homepage_status():
    r = requests.get(BASE_URL)
    assert r.status_code == 200

def test_homepage_not_empty():
    r = requests.get(BASE_URL)
    assert len(r.text) > 100
