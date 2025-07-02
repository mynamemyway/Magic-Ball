# Magic Ball🎱
from random import choice

def is_answer():
    positive_phrases = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']
    somepositive_phrases = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
    neutral_phrases = ['Пока неясно', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять']
    negative_phrases = ['Попробуй снова', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    cat = choice([positive_phrases, somepositive_phrases, neutral_phrases, negative_phrases])
    return f'{MB_PREFIX} {choice(cat)}'

MB_PREFIX = 'Magic Ball 🎱:'
while True:
    print(f'{MB_PREFIX} ask me')
    ask = input('Your question: ')
    print(is_answer())
    print()