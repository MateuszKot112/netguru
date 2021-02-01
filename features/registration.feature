@register
Feature: Registraion test
              As a new user, I would like to register an account.
        
        @valid
        Scenario Outline: Register a user with valid data
            Given The Rehegoo page "https://app.rehegoostreaming.com" is displayed
             When I click on Create Account button
              And I provide valid data "<name>", "<last_name>", "<password>"
              And I choose customer type Individual
              And I click on Continue button
             Then I should see "A verification link has been sent to your email account!" info
        Examples: Valid data
                  | name   | last_name | password     |
                  | Johhny | Bravo     | Password123! |
        

        @invalid
        Scenario Outline: Register a user with valid data
            Given The Rehegoo page "https://app.rehegoostreaming.com" is displayed
             When I click on Create Account button
              And I provide invalid data "<name>", "<last_name>", "<email>", "<password>"
              And I choose customer type Individual
              And I click on Continue button
             Then I should see error message
        Examples: Valid data
                  | name   | last_name | email                | password     |
                  | Johhny | Bravo     | test_mail@test.com   | Password123! |
                  | Johhny | Bravo     | invalid_mail@        | Password123! |
                  | Johhny | Bravo     | valid_mail@gmail.com | pass         |
                  