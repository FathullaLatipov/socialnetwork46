from database import get_db
from database.models import PostComment

from datetime import datetime


# Опубликовать комментарий
def add_comment_db(post_id, comment_text, user_id):
    db = next(get_db())

    new_comment = PostComment(post_id=post_id, comment_text=comment_text,
                              user_id=user_id)

    if new_comment:
        db.add(new_comment)
        db.commit()

        return 'Комментарий успешно добавлен'
    else:
        return 'Нету такого поста (('


# Удаления комментарий
def delete_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(PostComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Успешно удален'
    else:
        return 'Такого коммента нету(('


# Изменить определенную комментарию
def edit_comment_db(comment_id, changed_text):
    db = next(get_db())

    edit_comment = db.query(PostComment).filter_by(comment_id=comment_id).first()

    if edit_comment:
        edit_comment.comment_text = changed_text
        db.commit()

        return 'Комментарий успешно изменен юхууууу!'
    else:
        return 'Нету такого коммента'


# Получить все комменты определенного поста
def get_post_comments_db(post_id):
    db = next(get_db())

    post_comments = db.query(PostComment).filter_by(post_id=post_id).all()

    if post_comments:
        return post_comments
    else:
        return 'Нету'
