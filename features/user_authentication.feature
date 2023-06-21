Feature: User Authentication

  Scenario: Successful authentication
    Given I'm on the login page
    And have valid credentials
    When I set those credentials
    And ask to Log in
    Then Home page is displayed