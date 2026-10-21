class CatalogPage:
    def __init__(self, page):
        self.page = page
        self.catalog_class = page.locator(".book")
