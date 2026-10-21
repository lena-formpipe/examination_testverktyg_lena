class StatisticsPage:
    def __init__(self, page):
        self.page = page
        self.statistics_book_count = page.get_by_test_id("book-count")
        self.stars_count = page.get_by_test_id("stars-count")
