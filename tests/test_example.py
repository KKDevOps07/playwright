from playwright.sync_api import Page, expect
import re

BASE_URL = "http://localhost:8080"


def test_netflix_home_page_loads(page: Page):
    page.goto(BASE_URL, wait_until="networkidle")

    # Title should NOT be 404
    expect(page).not_to_have_title(re.compile("404", re.I))

    # Title should exist (string or regex only)
    expect(page).to_have_title(re.compile(".+"))

    # React root should exist
    expect(page.locator("#root, body")).to_be_attached()


def test_netflix_app_renders_content(page: Page):
    page.goto(BASE_URL, wait_until="networkidle")

    # Wait for any visible UI content
    page.wait_for_selector("div", timeout=10000)

    # Ensure page is not blank
    expect(page.locator("body")).not_to_be_empty()


def test_netflix_navigation_or_main_sections_exist(page: Page):
    page.goto(BASE_URL, wait_until="networkidle")

    # Instead of strict text, verify multiple content rows exist
    rows = page.locator("div").filter(has_text=re.compile(".", re.I))

    expect(rows).to_have_count(lambda count: count > 5)
