from faker import Faker
from faker.generator import random

class UserData:
	fake = Faker("ru_RU")
	number_phone = random.randint(1000000000, 9999999999)

	# генерация данных первого пользователя
	firstname_male = fake.first_name_male()
	surname_male = fake.last_name_male()
	address_male = 'Москва, Лубянский проезд, 5'
	station_male = 'Лубянка'
	phone_male = f'7{number_phone}'
	date_male = '15.04.2023'
	indx_male = 3
	color_male = 'grey'
	comment_male = 'Комментарий заказчика о хорошем'

	# # генерация данных второго пользователя
	firstname_female = fake.first_name_female()
	surname_female = fake.last_name_female()
	address_female = 'Москва, Хорошёвское шоссе, 20с1'
	station_female = 'Беговая'
	phone_female = f'7{number_phone}'
	date_female = '16.04.2023'
	indx_female = 4
	color_female = 'black'
	comment_female = 'Комментарий заказчика об очень хорошем'
