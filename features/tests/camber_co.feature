Feature: User can access camber page

  Scenario: User can open career page on camber homepage
    Given Open camber creative homepage
    And User can click the top right menu button
    When User selects careers from the menu
    Then Verify careers page opens
