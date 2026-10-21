class BasePage:
    def __init__(self, page):
        self.page = page
        self.favorites_button = page.get_by_test_id("favorites")
        self.statistics_button = page.get_by_test_id("statistics")
        self.add_book_button = page.get_by_test_id("add-book")
        self.catalog_button = page.get_by_test_id("catalog")

    def navigate_base_page(self):
        self.page.goto(
            "https://tap-vt26-testautomatisering.github.io/exam/",
            timeout=30000)
