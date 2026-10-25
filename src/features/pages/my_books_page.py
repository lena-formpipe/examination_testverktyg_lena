class MyBooksPage:

    def __init__(self, page):
        self.page = page
        self.book_list = page.get_by_test_id("book-list")
        # self.book1_my_book = page.get_by_test_id(f"fav-{BasePage.BOOK1_TITLE}")

    def fav_book(self, book_title: str):
        return self.page.get_by_test_id(f"fav-{book_title}")
