# Created by kingcapo at 1/12/26
Feature: Tests for cart

  Scenario: User can ensure that cart is empty
    Given Open Target main page
    When Click on Cart
    Then Cart is empty
    # Enter steps here


  Scenario: User can add products to cart
    Given Open Target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Click on Add to Cart button on sidebar
    And Click on Cart
    Then Verify cart has {amount} item(s)
    And Verify product in cart is correct

