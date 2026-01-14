# Created by kingcapo at 1/12/26
Feature: Tests for search

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <product>
    Then Search results for <expected_product> are shown


 # Scenario: User can search for a product
  #  Given Open Target main page
   # When Search for mug
    #Then Search results for mug are shown
Examples:
  |product  |expected_product |
  |tea      |tea              |
  |mug      |mug              |