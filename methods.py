import helpers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from data import phone_number
from locators import UrbanRoutesLocators
from selenium.webdriver.support import expected_conditions


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        self.wait.until(expected_conditions.visibility_of_element_located(UrbanRoutesLocators.from_field))
        self.driver.find_element(*UrbanRoutesLocators.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(expected_conditions.visibility_of_element_located(UrbanRoutesLocators.to_field))
        self.driver.find_element(*UrbanRoutesLocators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*UrbanRoutesLocators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*UrbanRoutesLocators.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_ask_for_a_taxi_button(self):
        self.driver.find_element(*UrbanRoutesLocators.ask_for_a_taxi_button).click()

    def click_comfort_tariff(self):
        self.driver.find_element(*UrbanRoutesLocators.comfort_tariff).click()

    def verify_comfort_tariff_is_selected(self):
        return self.driver.find_element(*UrbanRoutesLocators.choose_comfort_tariff_button).is_displayed()

    def select_comfort_tariff(self):
        self.click_ask_for_a_taxi_button()
        self.click_comfort_tariff()
        self.verify_comfort_tariff_is_selected()

    def click_add_phone_number(self):
        self.driver.find_element(*UrbanRoutesLocators.add_phone_number_button).click()

    def open_phone_number_input(self):
        self.driver.find_element(*UrbanRoutesLocators.add_number).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*UrbanRoutesLocators.add_phone_number_to_field).send_keys(phone_number)

    def confirm_phone_number(self):
        self.driver.find_element(*UrbanRoutesLocators.next_phone_number).click()

    def enter_confirmation_code(self):
        self.driver.find_element(*UrbanRoutesLocators.code_number).send_keys(helpers.retrieve_phone_code(self.driver))

    def confirm_code_phone_number(self):
        self.driver.find_element(*UrbanRoutesLocators.confirmation_code).click()

    def get_phone_number(self):
        return self.driver.find_element(*UrbanRoutesLocators.add_phone_number_text).text

    def complete_phone_verification(self):
        self.click_add_phone_number()
        self.open_phone_number_input()
        self.enter_phone_number(phone_number)
        self.confirm_phone_number()
        self.enter_confirmation_code()
        self.confirm_code_phone_number()

    def open_payment_method(self):
        self.driver.find_element(*UrbanRoutesLocators.payment_button).click()

    def add_card(self):
        self.driver.find_element(*UrbanRoutesLocators.add_card).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*UrbanRoutesLocators.card_number).send_keys(card_number)

    def enter_card_code(self, card_code):
        self.driver.find_element(*UrbanRoutesLocators.card_code).send_keys(card_code)

    def submit_card(self):
        self.driver.find_element(*UrbanRoutesLocators.card_code).send_keys(Keys.TAB)
        self.driver.find_element(*UrbanRoutesLocators.add_card_button).click()

    def close_payment_window(self):
        self.driver.find_element(*UrbanRoutesLocators.close_payment_method).click()

    def add_payment_card(self, card_number, card_code):
        self.open_payment_method()
        self.add_card()
        self.enter_card_number(card_number)
        self.enter_card_code(card_code)
        self.submit_card()
        self.close_payment_window()

    def verify_payment_method_added(self):
        payment_text_element = self.driver.find_element(*UrbanRoutesLocators.text_in_payment_method)
        return payment_text_element.text == 'Tarjeta'

    def click_message_for_driver(self):
        self.driver.find_element(*UrbanRoutesLocators.driver_message_selector).click()

    def write_message_for_driver(self, message_for_driver):
        self.driver.find_element(*UrbanRoutesLocators.driver_message_text).send_keys(message_for_driver)

    def set_message_for_driver(self, message):
        self.click_message_for_driver()
        self.write_message_for_driver(message)
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element_value(UrbanRoutesLocators.driver_message_text, message))

    def get_message_for_driver(self):
        return self.driver.find_element(*UrbanRoutesLocators.driver_message_text).get_property('value')

    def select_blanket_and_tissues(self):
        checkbox_element = self.driver.find_element(*UrbanRoutesLocators.blanket_and_tissues_checkbox)
        if not checkbox_element.is_selected():
            checkbox_element.click()

    def check_blanket_and_tissues_is_selected(self):
        checkbox_element = self.driver.find_element(*UrbanRoutesLocators.blanket_and_tissues_state)
        return checkbox_element.is_selected()

    def add_two_ice_creams(self):
        self.driver.find_element(*UrbanRoutesLocators.add_ice_cream).click()
        self.driver.find_element(*UrbanRoutesLocators.add_ice_cream).click()

    def verify_ice_cream_order(self):
        ice_cream_count = self.driver.find_element(*UrbanRoutesLocators.ice_cream_counter).text
        return ice_cream_count == "2"

    def click_on_book_a_taxi(self):
        self.driver.find_element(*UrbanRoutesLocators.book_taxi_button).click()

    def get_taxi_search_status(self):
        self.wait.until(expected_conditions.visibility_of_element_located(UrbanRoutesLocators.driver_search))
        text_search_status = self.driver.find_element(*UrbanRoutesLocators.driver_search)
        return text_search_status.text == "Buscar automóvil"












