import os
import logging


from browser import Browser
from steps.Searches import get_weather_data


def before_all(context):
    # note: the log level itself is set within behave.ini
    # setup logging
    context.config.setup_logging()

    # get our bespoke test settings from behave.ini for this set of scenarios
    cwd = os.getcwd()
    ini_file = os.path.join(cwd, 'behave.ini')

    if not os.path.isfile(ini_file):
        raise RuntimeError('behave.ini - config file not found at path:', cwd)

    userdata = context.config.userdata

    # add browser setting to our context so we can use it later
    context.browser_setting = userdata.get('our_browser')
    logging.info('Browser configured in behave.ini is: %s',
                 context.browser_setting)


def before_scenario(context, scenario):

    # all our scenarios are browser based so always start the chosen browser
    # instantiate our Browser according to above browser_setting
    context.browser = Browser(context.browser_setting)

    context.browser.visit('/')

    # get the page data before we do anything
    context.page_data_before_action = get_weather_data(context)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        logging.info("Scenario FAILED: %s", context.scenario.name)
        # TODO: Add logic to capture screenshot

    # close after scenario to keep scenarios independent/tidy
    context.browser.close()
