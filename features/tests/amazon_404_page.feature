Feature: Test for 404 page

  Scenario: User is able to navigate to amazon blog from
   Given Open Amazon product QDIU3RMG600 page
    And Store original window
   When Click on a dog image
    And Switch to a new window
   Then Verify blog is opened
    And Close blog
    And Return to original window