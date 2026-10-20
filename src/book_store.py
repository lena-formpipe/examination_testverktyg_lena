from src.fav_books import FavoriteBooks

# Backend
# Läslistan behöver Python-kod som hanterar listan med böcker.
# Du kan se exempel på lista här (JavaScript, denna används av webbsidan).
# Du får lägga till fler klasser och metoder om du behöver
# men dessa ska finnas i din src-mapp.
#
# 1. book_store.py → klassen BookStore ska ha följande metoder:
#   a.	addBook(author, title)
#   b.	toggleFavorite(book_id)


class BookStore:
    # favorites gör det möjligt att mocka kopplingen till FavoriteBooks
    # genom dependency injection
    def __init__(self, favorites = None):
        self._catalog = []
        self._my_books = favorites if favorites is not None else FavoriteBooks()
        self._next_book_id = 1


    # ny bok läggs till med favorite = false
    def add_book(self, author: str, title: str, favorite: bool = False):
        self._catalog.append({
            "book_id": self._next_book_id, "author": author,
            "title": title, "favourite": favorite
        })
        # stega upp till nästa book-id
        self._next_book_id += 1
        return

    # todo Returnera book_id från add_book.
    #  todo Då slipper testerna gissa att första boken har id 1.
    # todo ändra till id, inte titel, i favoritlistan.
    # todo Två böcker med samma titel (t.ex. olika utgåvor) skulle krocka.
    #  Då avmarkerar du fel bok eller får bara en post.
    def toggle_favorite(self, book_id):
        for book in self._catalog:
            # kontrollera att bok finns med detta id
            if book["book_id"] == book_id:
                book_title = book["title"]
                # om favorite är True, ändra till False
                if book["favourite"]:
                    book["favourite"] = False
                    self._my_books.remove(book_title)
                # om favorite inte är True, ändra till true
                elif not book["favourite"]:
                    book["favourite"] = True
                    self._my_books.add(book_title)
                return book["favourite"]
        return None


    # todo kan tas bort?
    def get_book_by_index(self, index):
        if 0 <= index < len(self._catalog):
            return self._catalog[index]
        return None


    # todo kan tas bort?
    def get_book_by_title(self, title):
        for book in self._catalog:
            if book["title"] == title:
                return book
        return None


    def get_list_of_my_books(self):
        favorites = self._my_books
        return favorites
