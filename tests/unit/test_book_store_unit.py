# US04:
# Som en användare vill jag
# kunna lägga till en bok i katalogen
# så att katalogen över böcker kan kompletteras med fler böcker.
import pytest


@pytest.mark.unit
def test_add_book(bookstore_empty, book1):
    # arrange
    bookstore = bookstore_empty
    titel1, author1 = book1
    book1_id = 1
    expected_book1 = {
        "book_id": book1_id, "author": author1, "title": titel1, "favourite": False
    }

    # act
    bookstore.add_book(author1, titel1)
    actual_book1 = bookstore.get_book_by_title(titel1)

    # assert
    assert expected_book1 == actual_book1


# US02
# Som en användare vill jag
# kunna favoritmarkera en enskild bok i katalogen
# så att jag enkelt ser vilka böcker som intresserar mig.
# Unittest eftersom mock används
@pytest.mark.unit
def test_toggle_favorite__mock_favorite_true(bookstore_one_book_with_mocker_favorite):
    # arrange
    bookstore, favorites = bookstore_one_book_with_mocker_favorite
    book_index = 0
    book = bookstore._catalog[book_index]
    book_id = book["book_id"]

    # toggle book1 en gång => favourite True
    expected_favourite1 = True

    # act
    bookstore.toggle_favorite(book_id)

    # assert
    assert expected_favourite1 == book["favourite"]
    assert favorites.add.call_count == 1
    assert favorites.remove.call_count == 0
    favorites.add.assert_called_with(book["title"])


# US03
# Som en användare vill jag
# kunna avmarkera en bok som favorit i katalogen
# så att jag kan ta bort böcker när mitt intresse förändras.
# Unittest eftersom mock används
@pytest.mark.unit
def test_toggle_favorite__mock_favorite_false(bookstore_one_book_with_mocker_favorite):
    # arrange
    bookstore, favorites = bookstore_one_book_with_mocker_favorite
    book_index = 0
    book = bookstore._catalog[book_index]
    book_id = book["book_id"]
    # toggle book två gånger => favourite False
    expected_favourite1 = False

    # act
    bookstore.toggle_favorite(book_id)
    bookstore.toggle_favorite(book_id)

    # assert
    assert expected_favourite1 == book["favourite"]
    assert favorites.add.call_count == 1
    assert favorites.remove.call_count == 1
    favorites.add.assert_called_with(book["title"])
    favorites.remove.assert_called_with(book["title"])
