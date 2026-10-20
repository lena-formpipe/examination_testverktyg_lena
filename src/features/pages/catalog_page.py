import re


class CatalogPage:
    def __init__(self, page):
        self.page = page
        # todo hitta något unikt, h2 finns på varje sida
        # self.welcome_text = page.get_by_role("heading").get_by_text(re.compile("Välkommen", re.IGNORECASE))
        self.catalog_class = page.locator(
            ".book")