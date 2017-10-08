from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,\
    WebDriverException
import logging
logging.basicConfig(level=logging.INFO)


class Browser(object):

    base_url = 'http://localhost:3000//'

    def __init__(self, chosen_browser):

        #  default to Chrome unless user has configured otherwise
        if chosen_browser.lower() == 'firefox':
            self.driver = webdriver.Firefox()  # TODO: implement this
            logging.info('Started Browser according to configured choice -'
                         ' Firefox')
        elif chosen_browser.lower() == 'internetexplorer':
            self.driver = webdriver.Ie()   # TODO: implement this
            logging.info('Started Browser according to configured choice - IE')
        else:
            self.driver = webdriver.Chrome()
            logging.info('Started Browser according to configured choice - '
                         'Chrome - default if not specified.')

        self.driver.implicitly_wait(2)
        self.driver.set_window_size(1920, 1080)  # Set to known dimensions
        # self.driver.maximize_window()

    def close(self):
        """
        Close the browser window that the driver has focus of
        """
        self.driver.close()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def wait_for_element_by_id(self, selector):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, selector)))

        return element

    def get_all_data_test_elements_to_dict(self):
        """
        :return: dict of all data-test items , text value
        """

        elem_dict = {}

        for elem in self.driver.find_elements(By.XPATH, './/span[@data-test]'):

            # if there is data then add it to our dict
            if elem.text:
                # logging.info(elem.text)
                dict_key = elem.get_attribute("data-test")
                elem_dict[dict_key] = elem.text

        return elem_dict

    def find_specific_data_element_with_xpath_like(self, text):
        """
        find all the data-test elements and then filter by the one we want
        based on its text

        return: the element or False

        TODO: consider if using the data-test="day-1" would be more reliable
        """
        for elem in self.driver.find_elements_by_xpath('.//span[@data-test]'):

            if elem.text and (elem.text in text):
                logging.info("Found element by matching text with %s"
                             " - got: %s", text, elem.text)
                return elem
        return False

    def quit(self):
        """
        close all browser windows and safely end session
        """
        self.driver.quit()

    def find_by_id(self, selector):
        """
        find a single element in the DOM
        """
        try:
            our_object = self.driver.find_element_by_id(selector)
        except (NoSuchElementException, WebDriverException) as (e):
            logging.warning("Failed to find object by ID: %s", str(e))
            raise

        return our_object
