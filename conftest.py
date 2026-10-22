import pytest
from src.fav_books import FavoriteBooks
from src.book_store import BookStore


@pytest.fixture
def book1():
    titel1 = "Kul med Kula"
    author1 = "Kalle Kula"
    return titel1, author1


@pytest.fixture
def book2():
    titel2 = "Livet i Ankeborg"
    author2 = "Anna Anka"
    return titel2, author2

"""
@pytest.fixture
def bookstore():
    bookstore = BookStore()
    favorites = bookstore.get_list_of_my_books()
    return bookstore, favorites
"""

@pytest.fixture
def bookstore_empty():
    return BookStore()

"""
@pytest.fixture
def bookstore_two_books(bookstore_empty, book1, book2):
    bookstore = bookstore_empty
    titel1, author1 = book1
    titel2, author2 = book2
    bookstore.add_book(author1, titel1)
    bookstore.add_book(author2, titel2)
    return bookstore, titel1, titel2
"""

"""
@pytest.fixture
def bookstore_two_books_with_mocker_favorite_books(mocker, book1, book2):
    favorites = mocker.Mock(spec=FavoriteBooks)
    bookstore = BookStore(favorites)
    titel1, author1 = book1
    titel2, author2 = book2
    bookstore.add_book(author1, titel1)
    bookstore.add_book(author2, titel2)
    return bookstore, favorites
"""

@pytest.fixture
def bookstore_one_book_with_mocker_favorite(mocker, book1):
    favorites = mocker.Mock(spec=FavoriteBooks)
    bookstore = BookStore(favorites)
    titel1, author1 = book1
    bookstore.add_book(author1, titel1)
    return bookstore, favorites


@pytest.fixture
def bookstore_one_book(book1):
    titel1, author1 = book1
    bookstore = BookStore()
    bookstore.add_book(author1, titel1)
    return bookstore


@pytest.fixture
def favorite_book_list_empty():
    favorite_book_list = FavoriteBooks()
    return favorite_book_list


@pytest.fixture
def favorite_book_list_two_books(favorite_book_list_empty, book1, book2):
    favorite_book_list = favorite_book_list_empty
    titel1, author1 = book1
    titel2, author2 = book2
    favorite_book_list.add(titel1)
    favorite_book_list.add(titel2)
    return favorite_book_list, titel1, titel2
