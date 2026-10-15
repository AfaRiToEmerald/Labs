import random

print("======= Добро пожаловать в игру «Угадай число»! =======")
print("     Компьютер загадал целое число от 1 до 100.")
print("           Для выхода из игры введите 0.")
print("=======================================================")

secret_number: int = random.randint(1, 100)                                           #загадывание числа

attempts: int = 0                                                                     #счетчик попыток
is_guessed: bool = False                                                              #успешное угадывание

while not is_guessed:
    try:
        user_input = input("Введите ваше число (или 0 для выхода): ")
        user_number: int = int(user_input)
    except ValueError:
        print("Ошибка: Пожалуйста, введите именно целое число!")
        continue                                                                      #проверка на дурака с откатом

    if user_number == 0:
        print(f"\nВы вышли из игры. Компьютер загадал число: {secret_number}")
        break  