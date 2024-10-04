import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage

### Fixtures ### 
# Fixtures are used to set up the test environment before running the test and clean up after the test is done.

@pytest.fixture
def browser_context(playwright):
    # Launch browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context  # Provide the context to the test
    context.close()  # Clean up by closing context after test
    browser.close()  # Close the browser

@pytest.fixture
def navigate_to_youtube_home(browser_context):
    page = browser_context.new_page()  
    youtube = HomePage(page) 
    youtube.go_to_home_page()  # Navigate to the YouTube home page
    youtube.verify_loaded()  # Verify the page is loaded
    return page, youtube  # Return the page object for use in other tests


### Test Cases ###
# Test cases are the actual tests that are run to validate the functionality of the application.

def test_search_functionality(navigate_to_youtube_home):
    page, youtube = navigate_to_youtube_home  # Get the page and YouTube instance from the fixture
    search_query = "Playwright"  # Search query

    # # Perform a search on YouTube
    youtube.search(search_query)
    
    search_page = SearchPage(page)  # Create a SearchPage instance
    search_page.verify_loaded(search_query)  # Verify that the search results page has loaded
    