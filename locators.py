from selenium.webdriver.common.by import By


class UrbanRoutesLocators:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_for_a_taxi_button = (By.XPATH, '//button[@class="button round"]')
    comfort_tariff = (By.XPATH, '//img[@alt="Comfort"]')
    choose_comfort_tariff_button = (By.XPATH, '//button[@data-for="tariff-card-4"]')
    add_phone_number_button = (By.CSS_SELECTOR, '.np-button')
    add_phone_number_to_field = (By.ID, 'phone')
    add_phone_number_text = (By.XPATH, '//div[@class="np-text"]')
    add_number = (By.XPATH, '//div[@class="np-input"]/div')
    next_phone_number = (By.CLASS_NAME, "button.full")
    code_number = (By.ID, 'code')
    confirmation_code = (By.CSS_SELECTOR, '.section.active>form>.buttons>:nth-child(1)')
    next_button = (By.CLASS_NAME, 'button.full')
    payment_button = (By.XPATH, '//div[@class="pp-button filled"]')
    add_card = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_number = (By.ID, 'number')
    card_code = (By.XPATH, '//div[@class="card-code-input"]/input[@id="code"]')
    add_card_button = (By.XPATH, "//button[@type='submit' and contains(@class, 'button') and contains(@class, 'full') and text()='Agregar']")
    close_payment_method = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    text_in_payment_method = (By.CSS_SELECTOR, '.pp-value-text')
    driver_message_selector = (By.CSS_SELECTOR, 'label[for="comment"]')
    driver_message_text = (By.ID, 'comment')
    blanket_and_tissues_checkbox = (By.XPATH, '//div[@class="r-sw"]')
    blanket_and_tissues_state = (By.CSS_SELECTOR, ".switch-input")
    add_ice_cream = (By.CSS_SELECTOR, '.r-group-items>:nth-child(1)>div>.r-counter>div>.counter-plus')
    ice_cream_counter = (By.CSS_SELECTOR, 'div.counter div.counter-value')
    book_taxi_button = (By.CLASS_NAME, 'smart-button-wrapper')
    driver_search = (By.CLASS_NAME, 'order-header-title')





