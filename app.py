from flask import Flask, request, render_template
from random import choice

MB_PREFIX = 'Magic Ball 🎱'

def is_answer():
    positive_phrases = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']
    somepositive_phrases = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
    neutral_phrases = ['Пока неясно', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять']
    negative_phrases = ['Попробуй снова', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    cat = choice([positive_phrases, somepositive_phrases, neutral_phrases, negative_phrases])
    return f'{MB_PREFIX} {choice(cat)}'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', prefix=MB_PREFIX)

@app.route('/ask', methods=['POST'])
def handle_ask():
    user_question = request.form.get('question', '')
    answer_text = is_answer()
    return render_template('index.html', prefix=MB_PREFIX, question=user_question, answer=answer_text)

if __name__ == '__main__':
    app.run(debug=True)