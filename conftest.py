import pytest
from selenium import webdriver

@pytest.fixture
def driver():
	driver = webdriver.Firefox()
	yield driver
	driver.quit()


'''''Пишем фикстуру в которой
  - определяем вебдрайвер для нужного браузера        ---- driver = webdriver.Chrome()
  - перегружаем функцию для отработки следующего теста --- yield  driver
  - выгружаем драйвер '''''

# @pytest.fixture(scope = 'function')
# def cookie_scrool(driver):
# 	driver.find_element(By.CLASS_NAME, "App_CookieButton__3cvqF").click()  # клик по "КУКИ"
# 	element = driver.find_element(By.XPATH, "//div[contains(text(),'Вопросы о важном')]")
# 	driver.execute_script("arguments[0].scrollIntoView();", element)    # скрол до текста "Вопросы о важном"
# 	return driver