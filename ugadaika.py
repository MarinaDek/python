from random import randint

def is_valid(number, right):
    if number.isdigit() and int(right) >= int(number) >= 1:
         return True
    else:
        return False
        
def play_game(num, right_border):
    attemp = 0
    while True:
        number = input(f'Введите число от 1 до { right_border }: ')
        attemp += 1
        
        if is_valid(number, right_border) == True:
            number = int(number)
        else:
            print(f'А может быть все-таки введем целое число от 1 до { right_border }? ')
            continue
        
        if number < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        elif number > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        else:
            print('Вы угадали, поздравляем!Вы угадали с', str(attemp) , 'раза !')
            break
        
def return_game():
    number = input('Хотите сыграть ещё раз? Y/N')
    if number == 'Y':
        return True
    else:
        return False

print('Добро пожаловать в числовую угадайку')
while True:
    right_border = int(input('Укажите крайнее значение для диапазона угадывания: '))
    num = randint(1, right_border)
    play_game(num, right_border)
    if return_game() == True:
        continue
    else:
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')   