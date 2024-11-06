from behave import given, when, then

@given('Log In')
def sign_in(context):
    context.app.sign_in_page.sign_in()