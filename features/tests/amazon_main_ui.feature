Feature: Tests for main page UI

  Scenario:User can see language options
    Given Open amazon main page
    When Hover over language options
    Then Verify Spanish option present

  Scenario: User sees all footer links
    Given Open amazon main page
    Then Verify there are 32 links