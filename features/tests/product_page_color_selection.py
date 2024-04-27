Feature: Verify color selection on product page

  Scenario: Verify color selection for each color option
    Given 'I navigate to the Target product page
    When I loop through each color option
    Then I should see that each color option is selected
