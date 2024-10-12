import os
from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash

db_path = os.path.join(os.path.dirname(__file__), '../database/users.db')
db = SqliteDatabase(db_path)


class Users(Model):
    username = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db


def create_context(title):
    return {
        "title": title,
    }


def register_user(username, email, password):
    try:
        # Перевірка, чи існує користувач
        user, created = Users.get_or_create(username=username, defaults={
            'email': email,
            'password': generate_password_hash(password)  # Хешування пароля
        })

        if created:
            return True  # Успішна реєстрація
        else:
            raise ValueError("User already exists with the provided username.")

    except Exception as e:
        # Логування помилки (можна використовувати бібліотеку logging)
        print(f"Error registering user: {e}")
        raise e  # Можна також повернути більш зрозуміле повідомлення або передати його далі


def login_user(email, password):
    try:
        # Отримати користувача з бази даних
        user = Users.get(Users.email == email)

        # Перевірка пароля з хешем
        if check_password_hash(user.password, password):
            return True  # Успішний вхід
        else:
            return False  # Неправильний пароль

    except Users.DoesNotExist:
        # Якщо користувача не знайдено
        return False

    except Exception as e:
        # Логування помилки
        print(f"Error logging in: {e}")
        raise e  # Можна повертати більш зрозумілу помилку, якщо потрібно
