import allure
from data_order import UserData
from pages.scooter_order_page import ScooterOrderPage
from locators.scooter_order_locator import LocatorScooterOrder

class TestOrder():
	@allure.description('Кнопка Заказать в шапке. Флоу позитивного сценария')
	def test_scooter_order_in_hat(self, driver):
		scooter_order_in_hat = ScooterOrderPage(driver)
		scooter_order_in_hat.go_to_site()
		scooter_order_in_hat.click_element(LocatorScooterOrder.COOKIES)
		scooter_order_in_hat.click_element(LocatorScooterOrder.BUTTON_ORDER_HEADER)
		scooter_order_in_hat.fill_first_form(name = UserData.firstname_male, surname = UserData.surname_male,
									  addres = UserData.address_male, station = UserData.station_male,
									  phone = UserData.phone_male)

		scooter_order_in_hat.fill_first_form_button_next()
		scooter_order_in_hat.fill_second_form(date = UserData.date_male, index = UserData.indx_male,
									   color = UserData.color_male, comment = UserData.comment_male)
		scooter_order_in_hat.fill_second_form_button_next()
		scooter_order_in_hat.button_yes_confirmation_window()
		title = scooter_order_in_hat.order_window()
		scooter_order_in_hat.button_check_status_modal_window()
		assert 'Заказ оформлен' in title

	@allure.description('Кнопка Заказать в теле. Флоу позитивного сценария')
	def test_scooter_order_in_middle(self, driver):
		scooter_order_in_middle = ScooterOrderPage(driver)
		scooter_order_in_middle.go_to_site()
		scooter_order_in_middle.click_element(LocatorScooterOrder.COOKIES)
		scooter_order_in_middle.scroll_to(LocatorScooterOrder.BUTTON_ORDER_BODY)
		scooter_order_in_middle.click_element(LocatorScooterOrder.BUTTON_ORDER_BODY)
		scooter_order_in_middle.fill_first_form(name = UserData.firstname_female, surname = UserData.surname_female,
									  addres = UserData.address_female, station = UserData.station_female,
									  phone = UserData.phone_female)
		scooter_order_in_middle.fill_first_form_button_next()
		scooter_order_in_middle.fill_second_form(date = UserData.date_female, index = UserData.indx_female,
									   color = UserData.color_female, comment = UserData.comment_female)
		scooter_order_in_middle.fill_second_form_button_next()
		scooter_order_in_middle.button_yes_confirmation_window()
		title = scooter_order_in_middle.order_window()
		scooter_order_in_middle.button_check_status_modal_window()
		assert 'Заказ оформлен' in title
