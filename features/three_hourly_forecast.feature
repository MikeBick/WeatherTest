Feature: Selecting an individual day shows 3 hourly forecast
* User wishes to get more detailed data for a particular day in one city.

    Scenario Outline:
    Given I have selected to view a forecast for Stirling
    When I select <day> to view detailed data for that day
    Then I can view forecasts for each three hour period of the day
#	And these hourly forecasts will start from the current time?   TODO: confirm expected behaviour with Product owner - application starts at 1300 for Tuesday, 0100 for all other days

    Examples:
	| day |
	| Tuesday |
	| Wednesday|
