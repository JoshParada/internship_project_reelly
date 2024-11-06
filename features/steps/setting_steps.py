from behave import given, when, then

@then('Verify the right page opens')
def verify_settings_url(context):
    context.app.settings_page.verify_settings_url()

@then('Verify there are {n} options for the settings')
def verify_cells(context, n):
    context.app.settings_page.verify_options_count(n)

@then('Verify "connect the company" button is available')
def verify_settings(context):
    context.app.settings_page.verify_connect_the_company()