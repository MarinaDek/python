from random import choice

answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений',
           'Определённо да', 'Можешь быть уверен в этом', 
           'Мне кажется - да', 'Вероятнее всего',
           'Хорошие перспективы', 'Знаки говорят - да', 'Да',
           'Пока неясно, попробуй снова', 'Спроси позже', 
           'Лучше не рассказывать', 'Сейчас нельзя предсказать',
           'Сконцентрируйся и спроси опять', 'Даже не думай', 
           'Мой ответ - нет', 'По моим данным - нет', 
           'Перспективы не очень хорошие', 'Весьма сомнительно']  

def return_check(return_game):
    if return_game == 'Y':
        return True
    else:
        return False
        
def game_magic_ball():
    while True:
        question = input('Введите свой вопрос: ')
        answer_output = choice(answers)
        print(answer_output)
        return_game = input('Хотите ли задать еще один вопрос? Y/N: ')
        if return_check(return_game) == True:
            continue
        else:
            print('Возвращайся если возникнут вопросы!')
            break


print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как Вас зовут? ')
print(f'Привет, { name }!')
game_magic_ball()