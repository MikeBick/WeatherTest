Feature: Enter city name, get 5 day weather forecast

Background: the application is running and on the home page.

  Scenario Outline: Type a valid city name and get a forecast
    Given I enter the city as <city_name>
    When I confirm my selection
    Then the webpage updates the weather forecast data
    Examples:
    |city_name|
    | Edinburgh |
    | Glasgow |

	@wip
    Scenario:  Type an invalid city name and get a helpful error
    Given I enter the city as Glasssgow
    When I confirm my selection
    Then I am informed that there has been an 'Error retrieving the forecast'

