from fastapi import APIRouter
from db import users, database
from model import User, UserIn
from werkzeug.security import generate_password_hash, check_password_hash

router = APIRouter()


@router.get("/")
async def root():
    return "Welcome"


@router.get("/user/", response_model=list[User])
async def all_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/user/{user_id}")
async def one_user(user_id: int):
    query = users.select().where(user_id == users.c.id)
    return await database.fetch_one(query)


@router.post("/user/", response_model=str)
async def creat_user(user: UserIn):
    query = users.insert().values(
        surname=user.surname,
        name=user.name,
        email=user.email,
        adress=user.adress,
        password=generate_password_hash(user.password),
    )
    await database.execute(query)
    return "Пользователь создан"


@router.put("/user/{user_id}", response_model=str)
async def edit_user(user_id: int, new_user: UserIn):
    query = (
        users.update()
        .where(users.c.id == user_id)
        .values(
            surname=new_user.surname,
            name=new_user.name,
            email=new_user.email,
            adress=new_user.adress,
        )
    )
    await database.execute(query)
    return "Данные обновлены"


# @router.get('/user/{user_id}')
# async def change_password(user_id: int):
#     query = users.select(users.c.password).where(users.c.id==user_id)
#     await database.fetch_one(query)
#     return query


@router.delete("/user/{user_id}", response_model=str)
async def del_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return "Пользователь удален"
