from database.models import PostPhoto, UserPost
from database import get_db

# Получить все публикации
def get_all_posts_db():
    pass
    # UserPost

# Получить определенную публикацию
def get_exact_post_db(post_id):
    pass
    # UserPost

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

# ДЗ Загрузить фотографии к определенному посту
# def upload_post_photo_db() ---> PostPhoto()
# НЕ сделаете 10 отжиманий без обид)