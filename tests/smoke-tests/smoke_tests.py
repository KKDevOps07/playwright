import re
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8080"


class TestNetflixSmoke:
    """
    Smoke tests for Netflix application.
    Purpose: Validate that the app is alive and core UI is usable.
    """

    def test_app_loads_successfully(self, page: Page):
        """
        Business check:
        - Application is reachable
        - No 404 / blank screen
        """
        page.goto(BASE_URL, wait_until="networkidle")

        expect(page).not_to_have_title(re.compile("404", re.I))
        expect(page.locator("body")).to_be_attached()


    def test_main_ui_is_rendered(self, page: Page):
        """
        Business check:
        - Frontend framework mounted
        - Some visible UI exists
        """
        page.goto(BASE_URL, wait_until="networkidle")

        # React / SPA root usually exists
        expect(page.locator("#root")).to_be_attached()

        # At least one visible element exists
        visible_elements = page.locator("div:visible")
        assert visible_elements.count() > 5


    def test_navigation_is_available(self, page: Page):
        """
        Business check:
        - User can see navigation
        - App is usable
        """
        page.goto(BASE_URL, wait_until="networkidle")

        nav = page.locator("nav, header")
        expect(nav.first).to_be_attached()


    def test_content_is_loaded(self, page: Page):
        """
        Business check:
        - Some content/cards are loaded
        - Backend + APIs are responding
        """
        page.goto(BASE_URL, wait_until="networkidle")

        # Look for any card-like structure
        cards = page.locator("img, video, section")
        assert cards.count() > 3
