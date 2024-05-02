Feature: Verify product name and image on Target search results page

  Scenario: Verify product name and image for each product on search results page
    Given 'I navigate to the Target product page'
    When 'I loop through each color option'
    Then 'I should see that each color option is selected'
