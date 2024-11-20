from behave import given, when, then

@given('Open Reelly Page')
def target_page(context):
    context.app.main_page.open_main()

@when('Go to Settings')
def go_to_settings(context):
    context.app.main_page.go_to_settings()

@when('Go to Settings on mobile')
def go_to_settings_mobile(context):
    context.app.main_page.go_to_settings_mobile()

@when('Go to Main menu on mobile')
def go_to_main_menu_mobile(context):
    context.app.main_page.go_to_main_menu_mobile()