from database.models import User

from database import get_db


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users

# Получить определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return 'Такого id пользователя нету(('

# Добавить пользователя(регистрация)
def add_new_user_db(name, surname, phone_number, city, password):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return 'Такой номер телефона уже зарегистрирован'
    else:
        new_user = User(name=name, surname=surname, phone_number=phone_number, city=city, password=password)
        db.add(new_user)
        db.commit()

        return 'Пользователь успешно зарегистрирован'


# Логин либо проверка пароля
def login_user_db(phone_number, password):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker: #1234
        if checker.password == password:
            return checker
        elif checker.password != password:
            return 'Неверный пароль'
    else:
        return 'Ошибка в данных'

# Изменить информацию о пользователе
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = get_exact_user_db(user_id)

    if exact_user:
        if edit_info == 'name':
            exact_user.name = new_info
        elif edit_info == 'city':
            exact_user.city = new_info

        db.commit()

        return 'Данные успешно изменены'
    else:
        return 'Пользователь не найден(('

# Удаления пользователя либо (LogOut)
def delete_user_db(user_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        db.delete(user)
        db.commit()

        return 'Пользователь успешно удален!'
    else:
        return 'Польльзователь не найден'

#Добавить фото профиля
def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())
