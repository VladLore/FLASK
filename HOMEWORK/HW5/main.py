from fastapi import FastAPI
import uvicorn
from model import User
import user

"""
Необходимо создать API для управления списком пользователей. Создайте класс User с полями id, name, email и password.

API должен содержать следующие конечные точки:
— GET /users — возвращает список пользователей.
— GET /users/{id} — возвращает пользователя с указанным идентификатором.
— POST /users — добавляет нового пользователя.
— PUT /users/{id} — обновляет пользователя с указанным идентификатором.
— DELETE /users/{id} — удаляет пользователя с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.
"""


app = FastAPI()


app.include_router(user.router, tags=["Users"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
