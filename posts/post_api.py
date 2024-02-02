from fastapi import APIRouter
from database.postservice import get_all_posts_db, get_exact_post_db, add_new_post_db, edit_post_text_db, \
    delete_post_db, \
    like_post_db, unlike_post_db, upload_post_photo_db, delete_post_photo_db

from posts import PublicPostValidator

posts_router = APIRouter(prefix='/posts', tags=['Работа с постами'])

# Запрос на публикацию поста
@posts_router.post('/public_post')
async def public_post(data: PublicPostValidator):
    result = add_new_post_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка брат!'}

# Запрос на удаление публикации
@posts_router.delete('/delete-post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не найден брат!'}

# Запрос на получение всех публикаций
@posts_router.get('/get-all-posts')
async def get_all_posts():
    result = get_all_posts_db()

    return {'message': result}
