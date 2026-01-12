# Created by kingcapo at 1/12/26
Feature: Tests for cart

  Scenario: User can ensure that cart is empty
    Given Open Target main page
    When Click on Cart
    Then Cart is empty
    # Enter steps here