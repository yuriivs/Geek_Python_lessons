text = input("Введите набор слов через пробел").split()
print(text)


def int_func(text):
    res = []

    for word in text:
        res.append(word.capitalize())

    return ' '.join(res)


print(int_func(text))
