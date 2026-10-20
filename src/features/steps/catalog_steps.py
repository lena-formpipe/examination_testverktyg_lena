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

    # utan page object
    # context.page.goto(context.base_url, timeout=30000)


@when(u'jag favoritmarkerar boken "Ormar på ett plan: En Python-berättelse"')
def step_impl(context):
    context.first_book_button = context.page.get_by_test_id(
        "star-Ormar på ett plan: En Python-berättelse"
    )
    expect(context.first_book_button).to_have_class("star")
    context.first_book_button.click()


@then(u'boken "Ormar på ett plan: En Python-berättelse" ska vara favoritmarkerad')
def step_impl(context):
    expect(context.first_book_button).to_have_class("star selected")

