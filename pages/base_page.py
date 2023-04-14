import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
	@allure.step('Инициализация драйвера и адреса сайта')
	def __init__(self, driver):
		self.driver = driver
		self.base_url = 'https://qa-scooter.praktikum-services.ru/'

	@allure.step('Переход на сайт')
	def go_to_site(self):
		return self.driver.get(self.base_url)

	@allure.step('Наличие элемента')
	def find_element(self, locator, time=10):
		return  WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find {locator}')

	@allure.step('Видимость элемента')
	def wait_element_visible(self, element, time = 10) :
		return WebDriverWait(self.driver, time).until(EC.visibility_of(element), message = f'Element is not visible {element}')

	@allure.step('Скролл до нужного пункта')
	def scroll_to(self, locator) :
		element = self.find_element(locator, time = 3)
		self.driver.execute_script("arguments[0].scrollIntoView();", element)
		return element

	@allure.step('Находим элемент по локатору, ждем его видимости и кликаем его')
	def click_element(self, locator) :
		element = self.find_element(locator)
		self.wait_element_visible(element).click()
		return element
