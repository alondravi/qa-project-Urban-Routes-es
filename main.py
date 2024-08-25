import data
from selenium import webdriver
from methods import UrbanRoutesPage



class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_comfort_tariff()
        assert routes_page.verify_comfort_tariff_is_selected() is True

    def test_phone_number_verification(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.complete_phone_verification()
        assert routes_page.get_phone_number() == data.phone_number

    def test_add_payment_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_payment_card(data.card_number, data.card_code)
        assert routes_page.verify_payment_method_added() is True

    def test_write_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.write_message_for_driver(data.message_for_driver)
        assert routes_page.get_message_for_driver() == data.message_for_driver

    def test_select_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_blanket_and_tissues()
        assert routes_page.check_blanket_and_tissues_is_selected() is True

    def test_ice_cream_order(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_two_ice_creams()
        assert routes_page.verify_ice_cream_order()

    def test_book_a_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_book_a_taxi()
        assert routes_page.get_taxi_search_status() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
