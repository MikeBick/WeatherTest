from behave import *
from selenium.webdriver.common.keys import Keys
import logging
from should_dsl import should, should_not
from hamcrest import equal_to


def get_weather_data(context):
    """
    retrieve all the "data-test" elements from page
    :param context:
    :return: values or False if unable to retrieve
    """
    retrieved_data = False

    retrieved_data = context.browser.get_all_data_test_elements_to_dict()
    logging.debug(retrieved_data)
    return retrieved_data


@step(u'I enter the city as {city_name}')
def step_impl(context, city_name):
    logging.info("Attempting to enter City: %s", city_name)

    our_text_field = context.browser.wait_for_element_by_id("city")

    if not our_text_field:
        logging.warning("FAILED to find City text box")
        raise AssertionError
    our_text_field.clear()
    our_text_field.send_keys(city_name)

    # Add the field to context so that we can use it in later steps
    context.city_text_box = our_text_field


@step(u'I confirm my selection')
def step_impl(context):
    elem = context.city_text_box
    elem.send_keys(Keys.ENTER)
    logging.info("Entered city")


@step(u'the webpage updates the weather forecast data')
def step_impl(context):

    # get all the data-test items from the page
    page_data = get_weather_data(context)

    try:
        page_data | should_not | equal_to(context.page_data_before_action)
    except AssertionError as(e):
        logging.warning(str(e))
        logging.info(page_data)
        logging.info(context.page_data_before_action)


@step(u"I am informed that there has been an 'Error retrieving the forecast'")
def error_text(context):
    # TODO : make this a generic function we can call from multiple steps
    raise NotImplementedError


@step(u'I have selected to view a forecast for {city}')
def get_to_hourly_view(context, city):
    context.execute_steps(u"""
                Given I enter the city as {city_name}
                When I confirm my selection
                Then the webpage updates the weather forecast data
        """.format(city_name=city))


@when(u'I select {day} to view detailed data for that day')
def step_impl(context, day):
    # find the button for that day and click it
    retrieved_item =\
        context.browser.find_specific_data_element_with_xpath_like(day)

    if not retrieved_item:
        logging.warning("Could not find item to click for"
                        " specified day: %s", day)
        raise AssertionError

    retrieved_item.click()


@then(u'I can view forecasts for each three hour period of the day')
def step_impl(context):
    # check we have forecasts and that the time periods show gaps of 3

    # get all the data-test items from the page
    page_data = get_weather_data(context)

    if page_data == context.page_data_before_action:
        logging.warning("Page does not seem to have updated")
        raise AssertionError

    # TODO : add logic to loop through each time period and check the intervals
    logging.info("Test for time interval data not yet implemented")

    # if this was not just an exercise then make it fail for now.
    # raise NotImplementedError
