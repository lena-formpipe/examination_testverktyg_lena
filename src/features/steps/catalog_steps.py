from behave import given, when, then
from playwright.sync_api import expect
from src.features.pages.base_page import BasePage
# reguljära uttryck == regex
import re


@given(u'jag surfar till Läslistan')
def step_impl(context):
    base_page = BasePage(context.page)
    context.base_page = base_page
    base_page.navigate_base_page()


@then(u'ska information om Katalog visas')
def step_impl(context):
    # todo hur hantera att det kan vara vilken bo som helst?
    # todo ska jag favoritmarkera en egen tillagd bok?
    context.first_book_catalog = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    expect(context.first_book_catalog).to_be_visible()
    expect(context.catalog_page.catalog_class.get_by_text(
        re.compile("Ormar på ett plan"))).to_be_visible()


@then(u'knappen Katalog ska vara inaktiv')
def step_impl(context):
    expect(context.base_page.catalog_button).to_be_disabled()


@when(u'jag favoritmarkerar boken "Ormar på ett plan: En Python-berättelse"')
def step_impl(context):
    context.first_book_button = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    expect(context.first_book_button).to_have_class("star")
    context.first_book_button.click(timeout=5000)


@then(u'boken "Ormar på ett plan: En Python-berättelse" ska vara favoritmarkerad')
def step_impl(context):
    expect(context.first_book_button).to_have_class("star selected")
