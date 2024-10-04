from playwright.sync_api import Page

class HomePage:
    home_url = "https://www.youtube.com"

    # Home Page locators 
    logo = "a#logo"
    search_input = "input#search"
    search_button = "button#search-icon-legacy"

    def __init__(self, page: Page):
        self.page = page

    def go_to_home_page(self):
        self.page.goto(HomePage.home_url)
        
    def verify_loaded(self):
        self.page.wait_for_selector(HomePage.logo)  # Wait for the YouTube logo to load
        assert HomePage.home_url in self.page.url  # Verify the URL is the YouTube home page
        assert "YouTube" in self.page.content()  # Verify the page title contains "YouTube"

    def search(self, search_query: str):
        self.page.fill(HomePage.search_input, search_query)
        self.page.dblclick(HomePage.search_button)
    