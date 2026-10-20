class AddBookPage:
    def __init__(self, page):
        self.page = page
        self.add_input_title = page.get_by_test_id("add-input-title")
        self.add_input_author = page.get_by_test_id("add-input-author")
        self.add_submit_button = page.get_by_test_id("add-submit")

