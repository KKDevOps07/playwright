import requests
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

def test_no_server_errors():
    r = requests.get(BASE_URL)
    assert r.status_code < 500
