class MyBooksPage:
    def __init__(self, page):
        self.page = page
        self.book_list = page.get_by_test_id("book-list")
