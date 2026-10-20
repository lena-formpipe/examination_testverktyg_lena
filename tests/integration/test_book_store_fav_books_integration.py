# US02
# Som en användare vill jag
# kunna favoritmarkera en enskild bok i katalogen
# så att jag enkelt ser vilka böcker som intresserar mig.
# Unittest eftersom mock används
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
# Unittest eftersom mock används
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







"""
# integrationstest för metod i annan klass anropas
def test_toggle_favorite__both_ways():
    bookstore = BookStore()

    book_id1 = 1
    titel1 = "Kul med Kula"
    author1 = "Kalle Kula"
    favourite1 = False
    expected_favourite1 = True

    book_id2 = 2
    titel2 = "Livet i Ankeborg"
    author2 = "Anna Anka"
    favourite2 = True
    expected_favourite2 = False

    # act
    bookstore.add_book(author1, titel1, favourite1)
    actual_favourite1 = bookstore.toggle_favorite(book_id1)
    print("favoriter enstaka")
    print(actual_favourite1)

    bookstore.add_book(author2, titel2, favourite2)
    actual_favourite2 = bookstore.toggle_favorite(book_id2)
    print(actual_favourite2)
    print("test_lista")
    print(bookstore._my_books.get_all_favourite_books())
    # print(actual_favourite1)
    # print(actual_favourite2)

    # assert
    assert expected_favourite1 == actual_favourite1
    assert expected_favourite2 == actual_favourite2


# behöver lägga till kontroll av favorit-listan anropas
def test_toggle_favorite__true_and_false(bookstore_two_books):

    # arrange
    # hitta boken med hjälp av dess position, plocka ut dess id
    bookstore = bookstore_two_books
    # book1 = bookstore._catalog[0]
    # book2 = bookstore._catalog[1]
    # book1_id = book1["book_id"]
    # book2_id = book2["book_id"]
    book1_id = bookstore._catalog[0]["book_id"]
    book2_id = bookstore._catalog[1]["book_id"]

    # vid tillägg har böcker favourite False
    # toggla book1 en gång => favourite True
    # toggla book2 två gånger => favourite False
    expected_favourite1 = True
    expected_favourite2 = False

    # act
    bookstore.toggle_favorite(book1_id)
    bookstore.toggle_favorite(book2_id)
    bookstore.toggle_favorite(book2_id)



    # assert
    assert expected_favourite1 == bookstore._catalog[0]["favourite"]
    assert expected_favourite2 == bookstore._catalog[1]["favourite"]
    # todo denna testar integrationen men kan göras snyggare?
    assert [bookstore._catalog[0]["title"]] == bookstore._my_books.get_all_favourite_books()


"""