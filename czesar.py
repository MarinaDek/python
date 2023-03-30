direction = int(input('Выберите функцию - шифрование(0) или дешифровани(1): '))
language = input('Выберите язык - русский(ru) или английский(en): ')
step = int(input('Введите шаг сдвига: '))
text = input('Введите текст: ')
text_output = ''


def validate_direction(direction):
    if direction != 0 and direction != 1:
        return False
    else:
        return True


def validate_language(language):
    if language != 'en' and language != 'ru':
        return False
    else:
        return True


while True:
    if validate_direction(direction):
        break
    else:
        print('Введите функцию 0-Шифрование или 1-Дешифрование')
        continue

while True:
    if validate_language(language):
        break
    else:
        print("Введите язык 'ru' или 'en'!")
        continue

if direction == 1:
    step = - step

for c in text:
    if not c.isalpha():
        text_output += c
    else:
        if language == 'ru':
            if c.isupper() == True:
                n = (ord(c) + step)
                if n < 1040:
                    n = 1071 - (1039 - n)
                text_output += chr(n)
            else:
                n = (ord(c) + step)
                if n < 1072:
                    n = 1103 - (1071 - n)
                text_output += chr(n)
        else:
            if c.isupper() == True:
                n = (ord(c) + step)
                if n < 65:
                    n = 90 - (64 - n)
                text_output += chr(n)
            else:
                n = (ord(c) + step)
                if n < 97:
                    n = 122 - (96 - n)
                text_output += chr(n)
print(text_output)
