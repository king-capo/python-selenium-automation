# Created by kingcapo at 1/13/26
Feature: Tests for add to cart

  Scenario Outline: User can add a products to cart
    Given Open Target main page
    When Search for <product>
    And Add <product> to cart
    Then Verify <expected_product> is in cart

    Examples:
  |product  |expected_product |
  |tea      |tea              |
  |mug      |mug              |
