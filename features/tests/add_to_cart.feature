# Created by kingcapo at 1/13/26
Feature: Tests for add to cart

  Scenario: User can add a products to cart
    Given Open Target main page
    When Search for tea
    Then Add tea to cart

  |product  |expected_product |
  |tea      |tea              |
  |mug      |mug              |
