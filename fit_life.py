# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding='utf-8')


# Блок констант
NDIGITS_OF_ROUND = 1
WATER_NORM_PER_KG_IN_ML = 30
NUMBER_OF_ML_IN_L = 1000

# 1. Знакомство
print('Здравствуйте!\nЯ ваш Фитнес-трекер!')
user_name = input('Введите ваше имя здесь: ')
while True:
    try:
        user_age = int(input('Введите ваш возраст сюда: '))
        break
    except ValueError:
        print('Возможно, вы ввели не целое число. Попробуйте ещё раз.')

# 2. Сбор данных
while True:
    try:
        user_weight = float(input('Введите ваш вес(в кг) сюда: '))
        break
    except ValueError:
        print('Возможно, вы ввели не число. Попробуйте ещё раз.')
while True:
    try:
        user_height = float(input('Введите ваш рост(в метрах) сюда: '))
        break
    except ValueError:
        print('Возможно, вы ввели не число. Попробуйте ещё раз.')


# 3. Логика расчетов
# Функция расчёта индекс массы тела
def calculate_bmi(weight_kg, height_m):
    """Вычисляет индекс массы тела (BMI) по весу в кг и росту в метрах.
    Возвращает: float — значение BMI.
    """
    return round(weight_kg / (height_m ** 2), NDIGITS_OF_ROUND)


# Функция расчёта нормы воды
def water_needed_calculation(weight_kg):
    """Вычисляет норму воды по весу в кг и норме в 30 мл на кг.
    Возвращает: float — значение нормы в литрах.
    """
    return (weight_kg * WATER_NORM_PER_KG_IN_ML) / NUMBER_OF_ML_IN_L


# Вызовы функций для расчёта необходимых данных трекера
bmi_result = calculate_bmi(user_weight, user_height)
water_needed_result = water_needed_calculation(user_weight)

# 4. Вывод красивого результата
print(f'Ура! {user_name}, данные получены!')
print('Итог получился таким: \n'
      f'Ваше имя: {user_name} \n'
      f'Ваш возраст: {user_age} (г.) \n'
      f'Ваш ИМТ: {bmi_result} (у.е.) \n'
      f'Ваша норма воды: {water_needed_result} (л. в день)')
print("Расчет окончен. Будьте здоровы!")
