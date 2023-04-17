import allure
from pages.scooter_main_page import ScooterMainPage
from locators.scooter_main_locator import LocatorScooterMain, Data

class TestQuestionsMain:
    @allure.title('Вопрос - Сколько это стоит')
    def test_check_element_how_much_is_it(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMain.How_Much_Is_It)
        actual_text = scooter_main.get_element_text(LocatorScooterMain.MESSAGE_0)
        expected_text = Data.Answer_To_Question_0
        assert actual_text == expected_text

    @allure.title('Вопрос - Хочу сразу несколько самокатов')
    def test_i_want_several_scooters(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMain.I_Want_Several_Scooters)
        actual_text = scooter_main.get_element_text(LocatorScooterMain.MESSAGE_1)
        expected_text = Data.Answer_To_Question_1
        assert actual_text == expected_text

    @allure.title('Вопрос - Как расчитывается время аренды?')
    def test_how_is_rental_time_calculated(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMain.How_Is_Rental_Time_Calculated)
        actual_text = scooter_main.get_element_text(LocatorScooterMain.MESSAGE_2)
        expected_text = Data.Answer_To_Question_2
        assert actual_text == expected_text

    @allure.title('Вопрос - Можно ли заказать самокат прямо на сегодня?')
    def test_order_a_scooter_today(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMain.Order_A_Scooter_Today)
        actual_text = scooter_main.get_element_text(LocatorScooterMain.MESSAGE_3)
        expected_text = Data.Answer_To_Question_3
        assert actual_text == expected_text

    @allure.title('Вопрос - Можно ли продлить заказ или вернуть самокат раньше?')
    def test_scooter_to_renew_or_return(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMain.Scooter_To_Renew_Or_Return)
        actual_text = scooter_main.get_element_text(LocatorScooterMain.MESSAGE_4)
        expected_text = Data.Answer_To_Question_4
        assert actual_text == expected_text

    @allure.title('Вопрос - Вы привозите зарядку вместе с самокатом?')
    def test_do_you_bring_charger(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMain.Do_You_Bring_Charger)
        actual_text = scooter_main.get_element_text(LocatorScooterMain.MESSAGE_5)
        expected_text = Data.Answer_To_Question_5
        assert actual_text == expected_text

    @allure.title('Вопрос - Можно ли отменить заказ?')
    def test_can_i_cancel_an_order(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMain.Can_I_Cancel_An_Order)
        actual_text = scooter_main.get_element_text(LocatorScooterMain.MESSAGE_6)
        expected_text = Data.Answer_To_Question_6
        assert actual_text == expected_text

    @allure.title('Вопрос - Я жизу за МКАДом, привезёте?')
    def test_i_live_outside_bring(self, driver):
        scooter_main = ScooterMainPage(driver)
        scooter_main.goto_important_questions()
        scooter_main.click_element(LocatorScooterMain.I_Live_Outside_Bring)
        actual_text = scooter_main.get_element_text(LocatorScooterMain.MESSAGE_7)
        expected_text = Data.Answer_To_Question_7
        assert actual_text == expected_text
