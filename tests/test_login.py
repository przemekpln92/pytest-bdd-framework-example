from pytest_bdd import scenarios, given, when, then, parsers
from page_objects.login_page import Login
from page_objects.products_page import Products


scenarios("../features/login.feature")

@given(parsers.parse("Login page"), target_fixture="login_page")
def open_login_page(init_driver):
    page = Login(init_driver)
    page.go_to_login_page()
    return page

@when(parsers.parse("I type {username} {password} and click login"))
def log_in(login_page, username, password):
    login_page.fill_form_and_log_in(username, password)

@then("I should be logged in")
def verify_login(init_driver):
    title = Products(init_driver).get_title()
    assert "PRODUCTS" == title




