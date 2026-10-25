from behave import given, when, then
from playwright.sync_api import expect


@given(u'jag har navigerat till vyn Lägg till bok')
def step_impl(context):
    context.base_page.navigate_base_page()
    context.base_page.add_book_button.click(timeout=500)

    expect(context.add_book_page.add_input_title).to_be_visible()
    expect(context.add_book_page.add_input_author).to_be_visible()
    expect(context.add_book_page.add_submit_button).to_be_disabled()
    expect(context.base_page.add_book_button).to_be_disabled()


@when(u'jag lägger till boktitel {book_title}')
def step_impl(context, book_title):
    context.add_book_page.add_input_title.fill(book_title)


@when(u'jag lägger till författarnamn {author}')
def step_impl(context, author):
    context.add_book_page.add_input_author.fill(author)


@when(u'jag klickar på knappen Lägg till ny bok')
def step_impl(context):
    context.add_book_page.add_submit_button.click(timeout=5000)


@then(u'inmatningsfälten ska vara tomma')
def step_impl(context):
    expect(context.add_book_page.add_input_title).to_have_text("")
    expect(context.add_book_page.add_input_author).to_have_text("")


@then(u'knappen Lägg till ny bok ska vara inaktiv')
def step_impl(context):
    expect(context.add_book_page.add_submit_button).to_be_disabled()


@then(u'boken {book_title} ska ligga i Katalogen')
def step_impl(context, book_title):
    context.base_page.catalog_button.click(timeout=5000)
    context.added_book_catalog = context.page.get_by_test_id(f"star-{book_title}")
    expect(context.added_book_catalog).to_be_visible()


@when(u'jag klickar på knappen Lägg till bok')
def step_impl(context):
    context.base_page.add_book_button.click(timeout=5000)


@then(u'ska information om att lägga till bok visas')
def step_impl(context):
    expect(context.add_book_page.add_input_title).to_be_visible()
    expect(context.add_book_page.add_input_author).to_be_visible()


@then(u'knappen Lägg till bok ska vara inaktiv')
def step_impl(context):
    expect(context.base_page.add_book_button).to_be_disabled()
