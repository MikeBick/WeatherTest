@wip
Feature: Daily forecast should summarise the 3 hour data
* Most dominant (or current) condition
* Most dominant (or current) wind speed and direction
* Aggregate rainfall
* Minimum and maximum temperatures

Given I have collected the 3 hourly data for Stirling
When I compare this to the summarised data
Then the summary icon shows the correct (most dominant) weather type - aggregating the 3 hour data

Given I have collected the 3 hourly data for Stirling
When I compare this to the summarised data
Then the summary wind details shows the correct (most dominant) wind details - aggregating the 3 hour data

Given I have collected the 3 hourly data for Stirling
When I compare this to the summarised data
Then the summary rainfall details shows the correct (calculated) rainfall details - aggregating the 3 hour data

Given I have collected the 3 hourly data for Stirling
When I compare this to the summarised data
Then the temperature details shows the correct (Minimum and maximum) temperature details - aggregating the 3 hour data