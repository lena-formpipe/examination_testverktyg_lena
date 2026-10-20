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


@when(u'jag lägger till en boktitel')
def step_impl(context):
    context.add_book_page.add_input_title.fill("Hunger games")


@when(u'jag lägger till ett författarnamn')
def step_impl(context):
    context.add_book_page.add_input_author.fill("Någon Annan")


@when(u'jag klickar på knappen Lägg till ny bok')
def step_impl(context):
    context.add_book_page.add_submit_button.click(timeout=500)


@then(u'inmatningsfälten ska vara tomma')
def step_impl(context):
    expect(context.add_book_page.add_input_title).to_have_text("")
    expect(context.add_book_page.add_input_author).to_have_text("")


@then(u'knappen Lägg till ny bok ska vara inaktiv')
def step_impl(context):
    expect(context.add_book_page.add_submit_button).to_be_disabled()


@then(u'boken ska läggas till i Katalogen')
def step_impl(context):
    context.base_page.catalog_button.click(timeout=500)
    # todo fixa med catalog
    context.added_book_catalog = context.page.get_by_test_id("star-Hunger games")
    expect(context.added_book_catalog).to_be_visible()
