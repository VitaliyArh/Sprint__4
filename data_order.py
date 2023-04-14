from faker import Faker
from faker.generator import random

class UserData:
	fake = Faker("ru_RU")
	number_phone = random.randint(1000000000, 9999999999)

	# генерация данных первого пользователя
	firstname_first = fake.first_name_male()
	surname_first = fake.last_name_male()
	address_first = 'Москва, Лубянский проезд, 5'
	station_first = 'Лубянка'
	phone_first = f'7{number_phone}'
	date_first = '15.04.2023'
	indx_first = 3
	color_first = 'grey'
	comment_first = 'Комментарий заказчика о хорошем'

	# # генерация данных второго пользователя
	firstname_second = fake.first_name_female()
	surname_second = fake.last_name_female()
	address_second = 'Москва, Хорошёвское шоссе, 20с1'
	station_second = 'Беговая'
	phone_second = f'7{number_phone}'
	date_second = '16.04.2023'
	indx_second = 4
	color_second = 'black'
	comment_second = 'Комментарий заказчика об очень хорошем'
