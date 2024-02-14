""" Урок 10, завдання 3
Користувач вводить з клавіатури пропозицію. Написати функцію, яка друкуватиме на екран останні 3
символи кожного слова.
"""

import re

# text = input("Enter text: ")
text = """Користувач вводить з клавіатури пропозицію. Написати функцію, яка друкуватиме на екран останні 3
символи кожного слова."""
words = re.findall(r'\b\w+\b', text.lower())
for word in words:
    print(f'{word}: {word[-3:]}')