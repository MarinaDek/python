from random import choice


def check_length_password(length):
    if length < 4:
        return False
    else:
        return True

def check_count_password(count):
    if count < 1:
        return False
    else:
        return True
        
def generate_password(length, chars):
    password = ''
    for i in range(length):
        c = choice(chars)
        password += c
    return password
    
def gen_passwords():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = ''
    while True:
        count_password = int(input('Количество паролей для генерации: '))
        if check_count_password(count_password) == True:
            break
        else:
            print('Кол-во паролей для генерации должно быть >= 1!')
            continue
        
    while True:
        length = int(input('Длину одного пароля: '))
        if check_length_password(length) == True:       
            break
        else:
            print('Введите длину больше или равно 4 символов!')
            continue
    
    incl_digit = input('Включать ли цифры 0123456789? Да/Нет')
    incl_lower_letter = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Да/Нет')
    incl_upper_letter = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
    incl_symbols = input('Включать ли символы !#$%&*+-=?@^_? Да/Нет')
    incl_ambiguous_symbols = input('Исключать ли неоднозначные символы "il1Lo0O"? Да/Нет')

    if incl_digit.lower() == 'да':
        chars += digits
    if incl_lower_letter.lower() == 'да':
        chars += lowercase_letters
    if incl_upper_letter.lower() == 'да':
        chars += uppercase_letters
    if incl_symbols.lower() == 'да':
        chars += punctuation
    if incl_ambiguous_symbols.lower() == 'да':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    
    for _ in range(count_password):
        print(generate_password(length, chars))
        
gen_passwords()