import time
import requests
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

def test_homepage_load_time():
    start = time.time()
    requests.get(BASE_URL)
    duration = time.time() - start
    assert duration < 2
