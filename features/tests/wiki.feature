Feature: Wikipedia Org page

Scenario: User can search Python on Wiki page
    Given Open Wikipedia org
    And Input Python into search field
    Then Verify Python is on the results