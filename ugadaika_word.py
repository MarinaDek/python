from random import *

word_list = []
with open('C://Users/MarinaDekteva/Downloads/russian_nouns/russian_nouns.txt', encoding='utf8') as file:
    for line in file:
        word_list.append(line.strip())


def get_word():
    word = choice(word_list)
    return word.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def check_input(word):
    return word.isalpha()


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print('У вас есть 6 попыток')
    print(display_hangman(tries))
    print(word_completion)

    while tries > 0:
        word_input = input().upper()

        if check_input(word_input) == False:
            print('Введите только символ(ы), являющиеся буквами!')
            continue

        if word_input in guessed_letters or word_input in guessed_words:
            print('Введенный(ое) символ/слово уже вводили!')
            continue

        if len(word_input) == 1:
            guessed_letters.append(word_input)
            if word_input in word:
                for i in range(len(word)):
                    if word[i] == word_input:
                        word_completion = word_completion[:i] + word[i] + word_completion[i + 1:]
                if word_completion != word:
                    print(word_completion)
                    continue
            else:
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
                continue
        else:
            guessed_words.append(word_input)
            if word_input == word:
                word_completion = word
            else:
                tries -= 1
                print(display_hangman(tries))
                print(word_completion)
                continue

        if word_completion == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            print(word_completion)
            break

    if tries == 0:
        print(display_hangman(tries))
        print('Вы проиграли!')
        print(f'Загаданное слово {word}')


def main():
    while True:
        word = get_word()
        play(word)
        is_return_game = input('Желаете сыграть ещё раз? д(Да)/н(Нет) ').lower()
        if is_return_game != 'д':
            print('До новых встреч!')
            break
        else:
            continue

main()