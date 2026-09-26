# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Знакомство
# TODO: Спроси у пользователя имя
#  и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани
#  в переменную user_age (не забудь преобразовать в число)
print('Здравствуйте!\nЯ ваш Фитнес-трекер!')
user_name = input('Введите ваше имя здесь: ')
user_age = int(input('Введите ваш возраст сюда: '))

# 2. Сбор данных
# TODO: Запроси вес (в кг)
#  и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75)
#  и сохрани в user_height (тип float)
user_weight = float(input('Введите ваш вес(в кг) сюда: '))
user_height = float(input('Введите ваш рост(в метрах) сюда: '))


# 3. Логика расчетов
# TODO: Рассчитай bmi (Индекс массы тела)
def calculate_bmi(weight_kg, height_m):
    """Вычисляет индекс массы тела (BMI) по весу в кг и росту в метрах.
    Возвращает: float — значение BMI.
    """
    return round(weight_kg / (height_m ** 2), 1)


# TODO: Рассчитай water_needed
def water_needed_calculation(weight_kg):
    """Вычисляет норму воды по весу в кг и норме в 30 мл на кг.
    Возвращает: float — значение нормы в литрах.
    """
    water_needed_l = (weight_kg * 30) / 1000
    return water_needed_l


bmi_result = calculate_bmi(user_weight, user_height)
water_needed_result = water_needed_calculation(user_weight)

# 4. Вывод красивого результата
# TODO: Используй f-строку,
#  чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст,
#  ИМТ (округленный до 1 знака) и норму воды.
print(f'Ура! {user_name}, данные получены!')
print('Итог получился таким: \n'
      f'Ваше имя: {user_name} \n'
      f'Ваш возраст: {user_age} (г.) \n'
      f'Ваш ИМТ: {bmi_result} (у.е.) \n'
      f'Ваша норма воды: {water_needed_result} (л. в день)')
print("Расчет окончен. Будьте здоровы!")
