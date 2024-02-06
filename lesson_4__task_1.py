""" Урок 4, завдання 1
Вивчіть основні стандартні винятки, які перераховані в цьому уроці.
"""

# Стандартні класи винятків:
# o Базові:
# ▪ BaseException – базовий клас для всіх винятків.
# ▪ Exception – клас-спадкоємець BaseException, базовий клас для всіх стандартних
# винятків, які не вказують на обов'язкове завершення програми, та всіх
# користувацьких винятків.
# ▪ StandardError (Python 2) – базовий клас для всіх вбудованих винятків, окрім
# StopIteration, GeneratorExit, KeyboardInterrupt та SystemExit.
# ▪ ArithmeticError – базовий клас для всіх винятків, які пов'язані з арифметичними
# операціями.
# ▪ BufferError – базовий клас для винятків, які пов'язані з операціями над буфером
# ▪ LookupError – базовий клас для винятків, які пов'язані з неправильним ключем
# або індексом колекції.
# ▪ EnvironmentError (Python 2) – базовий клас для винятків, які пов'язаних із
# помилками, що відбуваються поза інтерпретатором Python. У Python 3 його
# роль виконує OSError.
# o Деякі з конкретних стандартних винятків:
# ▪ AssertionError – провал умови оператора assert.
# ▪ AttributeError – помилка звернення до атрибута.
# ▪ FloatingPointError – помилка операції над числами з плавальною точкою.
# ▪ ImportError – помилка імпортування модуля або імені з модуля.
# ▪ IndexError – неправильний індекс послідовності (наприклад, списку).
# ▪ KeyboardInterrupt – завершення програми шляхом натискання Ctrl+C консолі.
# ▪ MemoryError – нестача пам'яті.
# ▪ NameError – ім'я не знайдено.
# ▪ NotImplementedError – дія не реалізована. Призначений, серед іншого, для
# створення абстрактних методів.
# ▪ OSError – системна помилка.
# ▪ OverflowError – результат арифметичної операції надто великий, щоб бути
# представлений.
# ▪ RuntimeError – загальна помилка часу виконання, яка не входить до жодної
# категорії.
# ▪ SyntaxError – помилка синтаксису.
# ▪ IndentationError – підклас SyntaxError – неправильний відступ.
# ▪ TabError – підклас IndentationError – змішане використання символів табуляції
# та пробілів.
# ▪ SystemError – некритична внутрішня помилка інтерпретатора. Під час
# виникнення цього винятку варто залишити звіт про помилку на сайті
# https://bugs.python.org/
# ▪ SystemExit – виняток, що генерується функцією sys.exit(). Слугує для завершення
# роботи програми.
# ▪ TypeError – помилка невідповідності типів даних.
# ▪ UnboundLocalError – підклас NameError – звернення до ненаявної локальної
# змінної.
# ▪ ValueError – генерується, коли функції чи операції передано об'єкт коректного
# типу, але з некоректним значенням, причому цю ситуацію не можна описати
# точнішим винятком, як-от IndexError.
# ▪ ZeroDivisionError – ділення на нуль
