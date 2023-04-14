import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.scooter_order_locator import FirstPage, SecondPage, ModalWindow, Logo

class ScooterOrderPage(BasePage):
	@allure.step('Заполняем первую страницу формы заказа')
	def fill_first_form(self, name, surname, addres, station, phone) :
		self.driver.find_element(*FirstPage.NAME).send_keys(name)
		self.driver.find_element(*FirstPage.SURNAME).send_keys(surname)
		self.driver.find_element(*FirstPage.ADDRES).send_keys(addres)
		self.driver.find_element(*FirstPage.STATION).click()
		self.driver.find_element(*FirstPage.STATION).send_keys(station)
		self.driver.find_element(*FirstPage.CLICK_STATION).click()
		self.driver.find_element(*FirstPage.PHONE).send_keys(phone)

	@allure.step('После заполнения первой формы, нажимаем кнопку "Далее"')
	def fill_first_form_button_next(self) :
		self.driver.find_element(*FirstPage.BUTTON_NEXT).click()

	@allure.step('Заполняем вторую страницу формы заказа')
	def fill_second_form(self, date, index, color, comment) :
		self.driver.find_element(*SecondPage.DATE).click()
		self.driver.find_element(*SecondPage.DATE).send_keys(date)
		self.driver.find_element(*SecondPage.DROPDOWN).click()
		self.driver.find_elements(*SecondPage.DROPDOWN_OPTION)[index].click()
		self.driver.find_element(By.ID, color).click()
		self.driver.find_element(*SecondPage.COMMENT).send_keys(comment)

	@allure.step('После заполнения второй формы, нажимаем кнопку "Далее"')
	def fill_second_form_button_next(self) :
		self.driver.find_element(*SecondPage.BUTTON_NEXT).click()

	@allure.step('В первом модальном окне нажимаем кнопку "Да"')
	def button_yes_confirmation_window(self) :
		self.driver.find_element(*ModalWindow.BUTTON_WINDOW).click()

	@allure.step('Во втором модальном окне проверям сообщение об успешном создании заказа')
	def order_window(self) :
		text = self.driver.find_element(*ModalWindow.TITLE_WINDOW).text
		return text

	@allure.step('В модальном окне нажимаем кнопку "Проверить заказ"')
	def button_check_status_modal_window(self) :
		self.driver.find_element(*ModalWindow.BUTTON_CHECK_STATUS).click()

	@allure.step('Переключаемся во вкладку Yandex')
	def go_to_yandex(self, driver, time=10):
		current_handle = driver.current_window_handle
		self.click_element(Logo.LOGO_YANDEX)
		all_handles = driver.window_handles
		for handle in all_handles:
			if handle != current_handle:
				driver.switch_to.window(handle)
		return WebDriverWait(self.driver,time).until(EC.url_to_be("https://dzen.ru/?yredirect=true"))
