# локальная область видимости переменнных

# number = 1
#
#
# def increment(a):
#     print(a)
#     a += 1
#     print(a)
#
#
# increment(number)
#
# print(number)


# глобальная область видимости переменнных
# number = 1
#
#
# def increment(a):
#     global result
#     result = a + 1
#     print(a)
#
#
# increment(number)
#
# print(number)
# print(result)


#глобальная область видимости переменнных

def top_func():
    start = 0

    def inner_func():
        nonlocal start
        start += 1

    inner_func()
    print(start)


top_func()
