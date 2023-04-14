from selenium.webdriver.common.by import By

class LocatorScooterMain:
    Cookies = (By.CLASS_NAME, "App_CookieButton__3cvqF")                                  # локатор Куки
    Questions_About_Important = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")  # Вопросы о важном

    How_Much_Is_It = (By.ID, "accordion__heading-0")                  # Вопрос 1-ый "Сколько это стоит?"
    I_Want_Several_Scooters = (By.ID, "accordion__heading-1")         # Вопрос 2-ой "Хочу сразу несколько самокатов?"
    How_Is_Rental_Time_Calculated = (By.ID, "accordion__heading-2")   # Вопрос 3-ий "Как расчитывается время аренды?"
    Order_A_Scooter_Today = (By.ID, "accordion__heading-3")           # Вопрос 4-ый "Можно ли заказать самокат прямо на сегодня?"
    Scooter_To_Renew_Or_Return = (By.ID, "accordion__heading-4")      # Вопрос 5-ый "Можно ли продлить заказ или вернуть самокат раньше?"
    Do_You_Bring_Charger = (By.ID, "accordion__heading-5")            # Вопрос 6-ой "Вы привозите зарядку вместе с самокатом?"
    Can_I_Cancel_An_Order = (By.ID, "accordion__heading-6")           # Вопрос 7-ой "Можно ли отменить заказ?"
    I_Live_Outside_Bring = (By.ID, "accordion__heading-7")            # Вопрос 8-ой "Я жизу за МКАДом, привезёте?"

    MESSAGE_0 = (By.XPATH, '//div[@id="accordion__panel-0"]/p')       # Ответ на 1-ый вопрос
    MESSAGE_1 = (By.XPATH, '//div[@id="accordion__panel-1"]/p')       # Ответ на 2-ой вопрос
    MESSAGE_2 = (By.XPATH, '//div[@id="accordion__panel-2"]/p')       # Ответ на 3-ий вопрос
    MESSAGE_3 = (By.XPATH, '//div[@id="accordion__panel-3"]/p')       # Ответ на 4-ый вопрос
    MESSAGE_4 = (By.XPATH, '//div[@id="accordion__panel-4"]/p')       # Ответ на 5-ый вопрос
    MESSAGE_5 = (By.XPATH, '//div[@id="accordion__panel-5"]/p')       # Ответ на 6-ой вопрос
    MESSAGE_6 = (By.XPATH, '//div[@id="accordion__panel-6"]/p')       # Ответ на 7-ой вопрос
    MESSAGE_7 = (By.XPATH, '//div[@id="accordion__panel-7"]/p')       # Ответ на 8-ой вопрос

class Data:
    Answer_To_Question_0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    Answer_To_Question_1 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, ' \
                           'можете просто сделать несколько заказов — один за другим.'
    Answer_To_Question_2 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт ' \
                           'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли ' \
                           'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    Answer_To_Question_3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    Answer_To_Question_4 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    Answer_To_Question_5 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если ' \
                           'будете кататься без передышек и во сне. Зарядка не понадобится.'
    Answer_To_Question_6 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    Answer_To_Question_7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
