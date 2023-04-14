import allure
from pages.base_page import BasePage
from locators.scooter_main_locator import LocatorScooterMain

class ScooterMainPage(BasePage):
    @allure.step('По локатору ищет элемент, ждет его видимости и получаем его текст.')
    def get_element_text(self, locator):
        element = self.find_element(locator)
        return self.wait_element_visible(element).text

    @allure.step('Переход на сайт, клик на Куки, локатор текста Вопросы о важном')
    def goto_important_questions(self):
        self.go_to_site()
        self.click_element(LocatorScooterMain.Cookies)
        self.scroll_to(LocatorScooterMain.Questions_About_Important)
