from behave import given, when, then
from config.config import ProjectConfiguration

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@given('I\'m on the login page')
def step_impl(context):
    context.nav.get(f"{ProjectConfiguration.BASE_URL}/login")
    context.login_page = LoginPage(context.nav)


@given('have valid credentials')
def step_impl(context):
    context.user = "test@yopmail.com"
    context.pwd = "asd"


@when('I set those credentials')
def step_impl(context):
    context.login_page.fill_login_form(context.user, context.pwd)


@when('ask to Log in')
def step_impl(context):
    context.login_page.submit_login_form()
    context.home_page = HomePage(context.nav)


@then('Home page is displayed')
def step_impl(context):
    assert context.home_page.get_page_title() == "Seu Barriga - Home"
