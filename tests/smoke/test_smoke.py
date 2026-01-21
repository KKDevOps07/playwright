import re
from playwright.sync_api import Page, expect
import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

class TestNetflixSmoke:

    def start_trace(self, page: Page, trace_name: str):
        # Start tracing
        page.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        return trace_name

    def stop_trace(self, page: Page, trace_name: str):
        # Stop tracing
        os.makedirs("traces", exist_ok=True)
        page.context.tracing.stop(path=f"traces/{trace_name}.zip")

    def test_app_loads_successfully(self, page: Page):
        trace_name = self.start_trace(page, "test_app_loads_successfully")
        page.goto(BASE_URL, wait_until="domcontentloaded")
        expect(page).not_to_have_title(re.compile("404", re.I))
        expect(page.locator("body")).to_be_attached()
        self.stop_trace(page, trace_name)

    def test_spa_root_is_rendered(self, page: Page):
        trace_name = self.start_trace(page, "test_spa_root_is_rendered")
        page.goto(BASE_URL, wait_until="domcontentloaded")
        expect(page.locator("#root")).to_be_attached()
        self.stop_trace(page, trace_name)

    def test_navigation_is_available(self, page: Page):
        trace_name = self.start_trace(page, "test_navigation_is_available")
        page.goto(BASE_URL, wait_until="domcontentloaded")
        expect(page.locator("nav, header").first).to_be_visible()
        self.stop_trace(page, trace_name)

    def test_some_visible_ui_exists(self, page: Page):
        trace_name = self.start_trace(page, "test_some_visible_ui_exists")
        page.goto(BASE_URL, wait_until="domcontentloaded")
        assert page.locator("*:visible").count() > 5
        self.stop_trace(page, trace_name)

    def test_content_is_loaded(self, page: Page):
        trace_name = self.start_trace(page, "test_content_is_loaded")
        page.goto(BASE_URL, wait_until="domcontentloaded")
        assert page.locator("img, section, article, div").count() > 5
        self.stop_trace(page, trace_name)
