# Created by parad at 11/5/2024
Feature: Test Scenarios for Settings Page

  Scenario: User can see all buttons on Settings Page
    Given Open Reelly Page
    And Log In
    When Go to Settings
    Then Verify the right page opens
    And Verify there are 12 options for the settings
    And Verify "connect the company" button is available


#  1- Open the main page https://soft.reelly.io
#2- Log in to the page.
#3- Click on settings option.
#4- Verify the right page opens.
#5- Verify there are 12 options for the settings.
#6- Verify “connect the company” button is available.