from behave import given, when, then
from playwright.sync_api import expect


@when(u'jag klickar på knappen Mina böcker')
def step_impl(context):
    context.base_page.favorites_button.click(timeout=5000)


@then(u'ska information om Mina böcker visa tom lista')
def step_impl(context):
    # när inga böcker finns favoritmarkerade
    # så syns inte listan m en den finns att räkna
    expect(context.my_books_page.book_list).to_have_count(1)
    # todo hur göra när det FINNS böcker
    expect(context.my_books_page.book_list).not_to_be_visible()


@then(u'knappen Mina böcker ska vara inaktiv')
def step_impl(context):
    expect(context.base_page.favorites_button).to_be_disabled()


@when(u'jag klickar på knappen Statistik')
def step_impl(context):
    context.base_page.statistics_button.click(timeout=5000)


@then(u'ska information om Statistik visas')
def step_impl(context):
    expect(context.statistics_page.statistics_book_count).to_be_visible()
    expect(context.statistics_page.stars_count).to_be_visible()


@then(u'knappen Statistik ska vara inaktiv')
def step_impl(context):
    expect(context.base_page.statistics_button).to_be_disabled()


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


@then(u'ska information om Katalog visas')
def step_impl(context):
    # todo hur hantera att det kan vara vilken bo som helst?
    # todo ska jag favoritmarkera en egen tillagd bok?
    context.first_book_catalog = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    expect(context.first_book_catalog).to_be_visible()


@then(u'knappen Katalog ska vara inaktiv')
def step_impl(context):
    expect(context.base_page.catalog_button).to_be_disabled()
