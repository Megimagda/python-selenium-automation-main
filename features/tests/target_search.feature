# Created by me361 at 4/4/2024

Feature: Verify "Your cart is empty" on target.com

  Scenario Verify "Your cart is empty" message
    Given open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

