# Created by me361 at 4/4/2024



  Feature: Target Product Search

  Scenario Outline: Search for a product on Target website
    Given  navigate to the Target website
    When  search for "<product>"
    Then  should see the search results for "<product>"

    Examples:
      | product   |
      | headphones|
      | laptop    |
      | shoes     |
