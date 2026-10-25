from behave import when, then
from playwright.sync_api import expect


@when(u'jag klickar på knappen Mina böcker')
def step_impl(context):
    context.base_page.favorites_button.click()


@then(u'ska information om Mina böcker visa tom lista')
def step_impl(context):
    # när inga böcker finns favoritmarkerade
    # så syns inte listan men den finns att räkna
    expect(context.my_books_page.book_list).to_have_count(1)
    expect(context.my_books_page.book_list).not_to_be_visible()


@then(u'knappen Mina böcker ska vara inaktiv')
def step_impl(context):
    expect(context.base_page.favorites_button).to_be_disabled()


@then(u'boken "{book_title}" ska finnas på sidan Mina böcker')
def step_impl(context, book_title):
    context.base_page.favorites_button.click()
    expect(context.my_books_page.fav_book(book_title)).to_be_visible()
