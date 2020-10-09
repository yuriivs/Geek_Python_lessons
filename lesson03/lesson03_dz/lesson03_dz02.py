#  Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#  имя, фамилия, год рождения, город проживания, email, телефон.
#  Функция должна принимать параметры как именованные аргументы.
#  Реализовать вывод данных о пользователе одной строкой.

def user_list(name, surname, year_birth, city, email, phone):
    print(f"{name}", f"{surname}, ", f"{year_birth} года рождения,",
          f"проживает в городе {city}, ", f"email: {email}, ", f"телефон: {phone}")


user_list(
    name="Юрий", surname="Васильчук", year_birth=1980,
    city="Kyiv", email="y.vasylchuk@gmail.com", phone=380980080802
)
