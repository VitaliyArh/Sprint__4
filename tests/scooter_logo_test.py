import allure
from pages.scooter_logo_page import LogoYandex
from locators.scooter_order_locator import LocatorScooterOrder, Logo

class TestLogo:

	@allure.title('Переход при клике по лого "Самокат"')
	def test_transition_clicking_on_scooter_logo(self, driver) :
		scooter_logo = LogoYandex(driver)
		scooter_logo.go_to_site()
		scooter_logo.click_element(LocatorScooterOrder.COOKIES)
		scooter_logo.click_element(LocatorScooterOrder.BUTTON_ORDER_HEADER)
		scooter_logo.click_element(Logo.LOGO_SCOOTER)
		assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

	@allure.title('Переход при клике по лого "Яндекс"')
	def test_transition_clicking_on_yandex_logo(self, driver) :
		scooter_logo = LogoYandex(driver)
		scooter_logo.go_to_site()
		scooter_logo.click_element(LocatorScooterOrder.COOKIES)
		scooter_logo.go_to_yandex(driver)
		url_yandex = driver.current_url
		assert url_yandex == "https://dzen.ru/?yredirect=true"
