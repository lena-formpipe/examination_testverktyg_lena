from behave import when, then
from playwright.sync_api import expect


@when(u'jag klickar på knappen statistik')
def step_impl(context):
    context.base_page.statistics_button.click(timeout=5000)


@then(u'ska information om statistik visas')
def step_impl(context):
    expect(context.statistics_page.statistics_book_count).to_be_visible()


@then(u'ska statistik om favoritmarkeringar visas')
def step_impl(context):
    expect(context.statistics_page.stars_count).to_be_visible()


@then(u'ska knappen statistik ska vara inaktiv')
def step_impl(context):
    expect(context.base_page.statistics_button).to_be_disabled()
