def test_add__add_favorite(favorite_book_list_empty, book1, book2):
    # arrange
    favorite_book_list = favorite_book_list_empty
    title1, author1 = book1
    title2, author2 = book2
    expected_list = [title1, title2]

    # act
    favorite_book_list.add(title1)
    favorite_book_list.add(title2)
    actual_list = favorite_book_list.get_all_favorite_books()

    # assert
    assert expected_list == actual_list


def test_remove__remove_favorite(favorite_book_list_two_books):
    # arrange
    # ta bort book2
    # expected list blir enbart book1
    favorite_book_list, titel1, titel2 = favorite_book_list_two_books
    expected_list = [titel1]

    # act
    favorite_book_list.remove(titel2)

    # assert
    assert expected_list == favorite_book_list.get_all_favorite_books()