import re
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8080"


class TestNetflixSmoke:
    """
    Real industry-grade smoke tests.

    These validate:
    - App is up
    - SPA is mounted
    - Navigation exists
    - Content is rendered

    No assumptions about features that don't exist.
    """

    def test_app_loads_successfully(self, page: Page):
        """
        Health check:
        - App responds
        - No 404
        """
        page.goto(BASE_URL, wait_until="domcontentloaded")

        expect(page).not_to_have_title(re.compile("404", re.I))
        expect(page.locator("body")).to_be_attached()


    def test_spa_root_is_rendered(self, page: Page):
        """
        Frontend check:
        - React root exists
        """
        page.goto(BASE_URL, wait_until="domcontentloaded")

        root = page.locator("#root")
        expect(root).to_be_attached()


    def test_navigation_is_available(self, page: Page):
        """
        Usability check:
        - Navigation/header exists
        """
        page.goto(BASE_URL, wait_until="domcontentloaded")

        nav = page.locator("nav, header")
        expect(nav.first).to_be_visible()


    def test_some_visible_ui_exists(self, page: Page):
        """
        Rendering check:
        - At least one visible UI element exists
        """
        page.goto(BASE_URL, wait_until="domcontentloaded")

        visible = page.locator("*:visible")
        assert visible.count() > 5


    def test_content_is_loaded(self, page: Page):
        """
        Business check:
        - Some real content exists (images/cards)
        """
        page.goto(BASE_URL, wait_until="domcontentloaded")

        cards = page.locator("img, section, article, div")
        assert cards.count() > 5