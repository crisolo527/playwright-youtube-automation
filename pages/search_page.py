from playwright.sync_api import Page

class SearchPage:
    # Search page locators
    search_contents = "a#video-title"
    
    def __init__(self, page: Page):
        self.page = page

    def verify_loaded(self, search_query):
        # Wait for a specific element that indicates the search results are loaded
        self.page.wait_for_selector(SearchPage.search_contents) 
        assert self.page.is_visible(SearchPage.search_contents), "Search results are not visible."
        assert search_query in self.page.url, f"Search failed for query: {search_query}"
        
        