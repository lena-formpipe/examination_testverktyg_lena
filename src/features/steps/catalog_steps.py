from behave import given, when, then
from playwright.sync_api import expect


@given(u'jag surfar till Läslistan')
def step_impl(context):
    context.base_page.navigate_base_page()


@then(u'ska information visas om boken {book_title}')
def step_impl(context, book_title):
    expect(context.page.get_by_test_id(f"star-{book_title}")).to_be_visible()


@then(u'knappen Katalog ska vara inaktiv')
def step_impl(context):
    expect(context.base_page.catalog_button).to_be_disabled()


@when(u'jag favoritmarkerar boken "{book_title}"')
def step_impl(context, book_title):
    expect(context.base_page.star_button(book_title)).to_have_class("star")
    # anropar funktion i base_page för att klicka på rätt bok
    context.base_page.favorite_book(book_title)


@then(u'boken "{book_title}" ska vara favoritmarkerad')
def step_impl(context, book_title):
    expect(context.base_page.star_button(book_title)).to_have_class("star selected")


@when(u'jag avmarkerar boken "{book_title}"')
def step_impl(context, book_title):
    expect(context.base_page.star_button(book_title)).to_have_class("star selected")
    # anropar funktion i base_page för att klicka på rätt bok
    context.base_page.favorite_book(book_title)


@then(u'ska boken "{book_title}" inte vara favoritmarkerad')
def step_impl(context, book_title):
    expect(context.base_page.star_button(book_title)).to_have_class("star")
