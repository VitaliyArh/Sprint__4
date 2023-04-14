import allure
from data_order import UserData
from pages.scooter_order_page import ScooterOrderPage
from locators.scooter_order_locator import LocatorScooterOrder, Logo


class TestOrder():
	@allure.description('Кнопка Заказать в шапке. Флоу позитивного сценария')
	def test_scooter_order_in_hat(self, driver):
		scooter_order_in_hat = ScooterOrderPage(driver)
		scooter_order_in_hat.go_to_site()
		scooter_order_in_hat.click_element(LocatorScooterOrder.COOKIES)
		scooter_order_in_hat.click_element(LocatorScooterOrder.BUTTON_ORDER_HEADER)
		scooter_order_in_hat.fill_first_form(name = UserData.firstname_first, surname = UserData.surname_first,
									  addres = UserData.address_first, station = UserData.station_first,
									  phone = UserData.phone_first)

		scooter_order_in_hat.fill_first_form_button_next()
		scooter_order_in_hat.fill_second_form(date = UserData.date_first, index = UserData.indx_first,
									   color = UserData.color_first, comment = UserData.comment_first)
		scooter_order_in_hat.fill_second_form_button_next()
		scooter_order_in_hat.button_yes_confirmation_window()
		title = scooter_order_in_hat.order_window()
		scooter_order_in_hat.button_check_status_modal_window()
		assert 'Заказ оформлен' in title

		scooter_order_in_hat.click_element(Logo.LOGO_SCOOTER)
		assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

		scooter_order_in_hat.go_to_yandex(driver)
		url_yandex = driver.current_url
		assert url_yandex == "https://dzen.ru/?yredirect=true"

	@allure.description('Кнопка Заказать в теле. Флоу позитивного сценария')
	def test_scooter_order_in_middle(self, driver):
		scooter_order_in_middle = ScooterOrderPage(driver)
		scooter_order_in_middle.go_to_site()
		scooter_order_in_middle.click_element(LocatorScooterOrder.COOKIES)
		scooter_order_in_middle.scroll_to(LocatorScooterOrder.BUTTON_ORDER_BODY)
		scooter_order_in_middle.click_element(LocatorScooterOrder.BUTTON_ORDER_BODY)
		scooter_order_in_middle.fill_first_form(name = UserData.firstname_second, surname = UserData.surname_second,
									  addres = UserData.address_second, station = UserData.station_second,
									  phone = UserData.phone_second)
		scooter_order_in_middle.fill_first_form_button_next()
		scooter_order_in_middle.fill_second_form(date = UserData.date_second, index = UserData.indx_second,
									   color = UserData.color_second, comment = UserData.comment_second)
		scooter_order_in_middle.fill_second_form_button_next()
		scooter_order_in_middle.button_yes_confirmation_window()
		title = scooter_order_in_middle.order_window()
		scooter_order_in_middle.button_check_status_modal_window()
		assert 'Заказ оформлен' in title

		scooter_order_in_middle.click_element(Logo.LOGO_SCOOTER)
		assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

		scooter_order_in_middle.go_to_yandex(driver)
		url_yandex = driver.current_url
		assert url_yandex == "https://dzen.ru/?yredirect=true"
