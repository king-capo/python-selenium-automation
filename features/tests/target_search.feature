# Created by kingcapo at 1/12/26
Feature: Tests for search

  Scenario: User can search for a product
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown


  Scenario: User can search for a product
    Given Open Target main page
    When Search for mug
    Then Search results for mug are shown