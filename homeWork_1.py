vowels = set('аеёиоуыэюя')

def count_syllables(phrase):
    phrase_lower = phrase.lower()

    return sum(c in vowels for c in phrase_lower)

def check_rhythm(poem):
    phrases = poem.split()
    syllable_counts = [count_syllables(phrases) for phrase in phrases]
    if len(set(syllable_counts)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

        poem = input().strip()
    check_rhythm(poem)


vowels = set('аеёиоуыэюя')


def count_syllables(phrase):
    return sum(c in vowels for c in phrase.lower())


def check_rhythm(poem):
    phrases = poem.split()
    syllable_counts = [count_syllables(phrase) for phrase in phrases]

    if len(set(syllable_counts)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")


# Определяем набор гласных букв русского языка
# vowels = set('аеёиоуыэюя')


# # Функция для подсчета числа слогов (количества гласных) в строке
# def count_syllables(phrase):
#     # Преобразуем строку в нижний регистр, чтобы избежать проблем с регистрами
#     phrase_lower = phrase.lower()
#
#     # Используем генератор списка для подсчёта гласных
#     # Суммируем 1 за каждый символ, который является гласной буквой
#     return sum(c in vowels for c in phrase_lower)
#
#
# # Основная функция для проверки ритма стихотворения
# def check_rhythm(poem):
#     # Разделяем стихотворение на отдельные фразы
#     phrases = poem.split()
#
#     # Создаем список чисел слогов для каждой фразы
#     syllable_counts = [count_syllables(phrase) for phrase in phrases]
#
#     # Проверяем, все ли элементы списка одинаковы
#     # Если все элементы уникальны, значит ритм соблюден
#     if len(set(syllable_counts)) == 1:
#         print("Парам пам-пам")  # Ритм правильный
#     else:
#         print("Пам парам")  # Ритм нарушен
#
#
# # Считывание строки с клавиатуры
# poem = input().strip()
# check_rhythm(poem)