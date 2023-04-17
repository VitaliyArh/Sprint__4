from selenium.webdriver.common.by import By

class LocatorScooterOrder:
    COOKIES = (By.CLASS_NAME, "App_CookieButton__3cvqF")                          # Клик по кнопке "КУКИ"
    BUTTON_ORDER_HEADER = (By.XPATH, "//button[@class='Button_Button__ra12g']")   # кнопка Заказать в Шапке
    BUTTON_ORDER_BODY = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # кнопка Заказать в середине

class FirstPage:
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRES = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    CLICK_STATION = (By.CLASS_NAME, "select-search__select")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

class SecondPage:
    DATE = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
    DATE_SELECTED = [By.CLASS_NAME, 'react-datepicker__day--selected']
    DROPDOWN = (By.XPATH, ".//*[@class='Dropdown-arrow']")
    DROPDOWN_OPTION = (By.XPATH, ".//*[@class='Dropdown-menu']/div")
    COMMENT = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    BUTTON_NEXT = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

class ModalWindow:
    BUTTON_WINDOW = (By.XPATH, "//button[text()='Да']")                         # кнопка Да в окне Хотите оформить заказ
    BUTTON_CHECK_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")    # кнопка Посмотреть статус в окне Заказ оформлен
    TITLE_WINDOW = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")                  # заголовок Заказ оформлен

class Logo:
    LOGO_SCOOTER = (By.XPATH, ".//*[@alt='Scooter']")                           # логотип Самокат
    LOGO_YANDEX = (By.XPATH, ".//img[@alt='Yandex']")                           # логотип Яндекс
