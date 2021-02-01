@login
Feature: Registraion test
              As a user, I would like to log in to my account with my email and password.

        @valid
        Scenario: Login with valid credentials
            Given The Rehegoo page "https://app.rehegoostreaming.com" is displayed
             When I provide valid email "test_mail@test.com" and "Password123!"
              And I click on Sign In button
             Then Home page is present

        
        @invalid
        Scenario Outline: Login with invalid credentials
            Given The Rehegoo page "https://app.rehegoostreaming.com" is displayed
             When I provide invalid "<email>" and "<password>"
              And I click on Sign In button
             Then Error message should appear
        Examples:
                  | email        | password         |
                  | aaeerr@ww.pl | invalid_password |
                  | invali_mail@ | Password123!     |

        