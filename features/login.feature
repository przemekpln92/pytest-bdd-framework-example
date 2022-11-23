Feature: Login
  Login page scenario

  Scenario Outline: Login With Correct Credentials
    Given Login page
    When  I type <username> <password> and click login
    Then  I should be logged in

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |
