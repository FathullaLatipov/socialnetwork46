from database.models import PostPhoto, UserPost
from database import get_db


# Получить все публикации
def get_all_posts_db():
    db = next(get_db())

    all_post = db.query(UserPost).all()

    return all_post


# Получить определенную публикацию
def get_exact_post_db(post_id):
    db = next(get_db())

    exact_user = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_user:
        return get_all_posts_db()
    else:
        return 'такой пост не найден:('


# Добавить публикацию
def add_new_post_db(user_id, post_text, publish_date):
    db = next(get_db())

    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=publish_date)
    db.add(new_post)
    db.commit()

    return f'Успешно {new_post.post_id}'


# Изменить текст к публикации
def edit_post_text_db(post_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.post_text = new_text
        db.commit()

        return 'Текст к публикации изменен!'
    else:
        return 'Пост не найден(('


# Удаления публикацию
def delete_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        db.delete(exact_post)
        db.commit()

        return 'Пост успешно удален!'
    else:
        return 'Пост не найден'


# Добавить лайк к публикации
def like_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes += 1
        db.commit()

        return 'Успешно'
    else:
        return 'Пост не найден(('


# Удаления лайка из публикации
def unlike_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes -= 1
        db.commit()

        return 'Успешно'
    else:
        return 'Пост не найден(('


# Диер 20
# ДЗ Загрузить фотографии к определенному посту
def upload_post_photo_db(post_id, photo_path):
    db = next(get_db())

    new_photo = PostPhoto(post_id=post_id, photo_path=photo_path)

    if new_photo:
        db.add(new_photo)
        db.commit()

        return 'Фото к публикации добавлен'
    else:
        return 'Нету поста(('


# Удаления фотографию в определенном посте
def delete_post_photo_db(post_id, photo_path):
    db = next(get_db())

    new_photo = PostPhoto(post_id=post_id, photo_path=photo_path)

    if new_photo:
        db.delete(new_photo)
        db.commit()

        return 'Фото к публикации удален'
    else:
        return 'Нету поста(('


# Запрос на получении всех фотографий
def all_photos_db():
    db = next(get_db())

    photos = db.query(PostPhoto).all()

    return photos