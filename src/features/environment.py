from playwright.sync_api import sync_playwright
from pages.base_page import BasePage
from pages.add_book_page import AddBookPage
from pages.catalog_page import CatalogPage
from pages.my_books_page import MyBooksPage
from pages.statistics_page import StatisticsPage


# Runs before any scenarios
def before_all(context):
    # Start Playwright and the browser - close it in after_all
    context.playwright = sync_playwright().start()
    context.browser_type = context.playwright.chromium
    # todo ändra till headless = true innan inlämning
    context.browser = context.browser_type.launch(headless=True)


# Runs at the start of each scenario
def before_scenario(context, scenario):
    # The scenario fixture is created from a feature file,
    # we don't typically need it for anything.
    # Open a new page, to prevent cookies to leak between tests.
    # Set default timeout to something appropriate.
    # Close the page in after_scenario.
    context.page = context.browser.new_page()
    context.page.set_default_timeout(100)
    context.base_url = "https://tap-vt26-testautomatisering.github.io/exam/"
    # skapa page objekt för varje scenario
    context.base_page = BasePage(context.page)
    context.add_book_page = AddBookPage(context.page)
    context.my_books_page = MyBooksPage(context.page)
    context.statistics_page = StatisticsPage(context.page)
    context.catalog_page = CatalogPage(context.page)


# Runs directly after each scenario - clean up to avoid memory leaks
def after_scenario(context, scenario):
    if context.page:
        context.page.close()


# Runs after all scenarios have finished - clean up
def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
