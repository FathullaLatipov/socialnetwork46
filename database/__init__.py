from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Указать нашу БД
SQLALCHEMY_DATABASE_URI = 'sqlite:///social.db'

# Подключения к БД
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Генерация сессий
SessionLocal = sessionmaker(bind=engine)

# Общий класс для моделей
Base = declarative_base()


# Функция для генерации связей к БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
