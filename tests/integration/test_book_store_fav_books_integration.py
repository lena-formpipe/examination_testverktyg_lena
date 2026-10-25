import pytest


# Testet klassificeras som ett integrationstest eftersom
# det testar samspelet mellan klasserna BookStore och FavoriteBooks.
# När toggle_favorite() anropas ändrar BookStore bokens favoritstatus
# och anropar samtidigt FavoriteBooks för att lägga till bokens titel i favoritlistan.
# Testet verifierar att både bokens status ändras och att titeln registreras i favoritlistan.
# Eftersom båda klasserna används i sina faktiska implementationer testas deras integration.
# ---------------------------------------------------------------------
# US02
# Som en användare vill jag
# kunna favoritmarkera en enskild bok i katalogen
# så att jag enkelt ser vilka böcker som intresserar mig.
@pytest.mark.integration
def test_toggle_favorite__true(bookstore_one_book):
    # arrange
    bookstore = bookstore_one_book
    book_index = 0
    book = bookstore._catalog[book_index]
    book_id = book["book_id"]
    book_title = book["title"]
    # toggle book1 en gång => favourite ska vara True

    # act
    bookstore.toggle_favorite(book_id)
    favorite_books = bookstore._my_books.get_all_favorite_books()

    # assert
    assert book["favourite"] is True
    assert book_title in favorite_books


# US03
# Som en användare vill jag
# kunna avmarkera en bok som favorit i katalogen
# så att jag kan ta bort böcker när mitt intresse förändras.
@pytest.mark.integration
def test_toggle_favorite__false(bookstore_one_book):
    # arrange
    bookstore = bookstore_one_book
    book_index = 0
    book = bookstore._catalog[book_index]
    book_id = book["book_id"]
    book_title = book["title"]
    # toggle book två gånger => favourite ska vara False

    # act
    bookstore.toggle_favorite(book_id)
    bookstore.toggle_favorite(book_id)
    favorite_books = bookstore._my_books.get_all_favorite_books()

    # assert
    assert book["favourite"] is False
    assert book_title not in favorite_books
