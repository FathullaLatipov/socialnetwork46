from pydantic import BaseModel
from datetime import datetime

# Валидатор для публикации поста
class PublicPostValidator(BaseModel):
    user_id: int
    post_text: str
    publish_date: datetime


# Валидатор для изменения текста к посту
class EditPostValidator(BaseModel):
    post_id: int
    new_text: str
    user_id: int
