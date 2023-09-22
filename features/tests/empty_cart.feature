Feature: Amazon Empty Cart tests

 Scenario: User can see empty cart
   Given Open amazon main page
   When Click on cart button
#   Then Verify page opens
   Then Verify user can see Your Amazon cart is empty