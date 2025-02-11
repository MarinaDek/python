import sqlite3

# Функция для создания базы данных и таблицы
def create_database():
    with sqlite3.connect('registration.db') as db:
        cur = db.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users_data (
                UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                Login TEXT NOT NULL UNIQUE,
                Password TEXT NOT NULL,
                Code TEXT NOT NULL
            );
        """)
        db.commit()
        print("Таблица users_data создана или уже существует.")

# Функция для проверки уникальности логина (без учета регистра)
def is_login_unique(login):
    with sqlite3.connect('registration.db') as db:
        cur = db.cursor()
        cur.execute("SELECT Login FROM users_data WHERE LOWER(Login) = LOWER(?);", (login,))
        return cur.fetchone() is None

# Функция для регистрации нового пользователя
def register_user():
    with sqlite3.connect('registration.db') as db:
        cur = db.cursor()
        while True:
            login = input("Введите логин: ").strip()
            if not login:
                print("Логин не может быть пустым.")
                continue
            if not is_login_unique(login):
                print("Такой логин уже существует. Пожалуйста, выберите другой.")
                continue
            break

        while True:
            password = input("Введите пароль: ").strip()
            if not password:
                print("Пароль не может быть пустым.")
                continue
            break

        while True:
            code = input("Введите код восстановления (4 цифры): ").strip()
            if not (code.isdigit() and len(code) == 4):
                print("Код восстановления должен состоять из 4 цифр.")
                continue
            break

        cur.execute("INSERT INTO users_data (Login, Password, Code) VALUES (?, ?, ?);", 
                    (login, password, code))
        db.commit()
        print(f"Пользователь {login} успешно зарегистрирован.")

# Функция для авторизации пользователя
def authenticate_user():
    with sqlite3.connect('registration.db') as db:
        cur = db.cursor()
        login = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()

        cur.execute("SELECT * FROM users_data WHERE LOWER(Login) = LOWER(?) AND Password = ?;", 
                    (login, password))
        user = cur.fetchone()
        if user:
            print("Авторизация успешна!")
        else:
            print("Неверный логин или пароль.")

# Функция для восстановления пароля
def recover_password():
    with sqlite3.connect('registration.db') as db:
        cur = db.cursor()
        login = input("Введите логин: ").strip()
        code = input("Введите код восстановления (4 цифры): ").strip()

        cur.execute("SELECT * FROM users_data WHERE LOWER(Login) = LOWER(?) AND Code = ?;", 
                    (login, code))
        user = cur.fetchone()
        if not user:
            print("Неверный логин или код восстановления.")
            return

        new_password = input("Введите новый пароль: ").strip()
        if not new_password:
            print("Пароль не может быть пустым.")
            return

        cur.execute("UPDATE users_data SET Password = ? WHERE LOWER(Login) = LOWER(?);", 
                    (new_password, login))
        db.commit()
        print("Пароль успешно изменен.")

# Основная функция для взаимодействия с пользователем
def main():
    create_database()
    while True:
        print("\nВыберите действие:")
        print("1. Регистрация нового пользователя")
        print("2. Авторизация в системе")
        print("3. Восстановление пароля")
        print("4. Выход")
        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            register_user()
        elif choice == '2':
            authenticate_user()
        elif choice == '3':
            recover_password()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

if __name__ == "__main__":
    main()
