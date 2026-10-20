# Backend
# Läslistan behöver Python-kod som hanterar listan med böcker.
# Du kan se exempel på lista här (JavaScript, denna används av webbsidan).
# Du får lägga till fler klasser och metoder om du behöver
# men dessa ska finnas i din src-mapp.
#
# 2. fav_books.py → klassen FavoriteBooks ska ha följande metoder:
#   a.	add(book)
#   b.	remove(book)

class FavoriteBooks:
    def __init__(self):
        self._favorite_books = []


    def add(self, book):
        # när favorit markeras anropas add
        # kontroll att inte lägga till en bok som redan finns
        if book not in self._favorite_books:
            self._favorite_books.append(book)
        return


    def remove(self, book):
        # när favorit avmarkeras anropas remove
        # kontroll att inte ta bort en bok som inte finns
        if book in self._favorite_books:
            self._favorite_books.remove(book)
        return

    # vi kommer behöva kunna lista alla favoriter
    def get_all_favorite_books(self):
        return self._favorite_books
