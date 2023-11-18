from fastapi import APIRouter, HTTPException
from model import User, UserIn

router = APIRouter()

users = [
    User(id=1, name="Тест1", email="test1@mail.ru", password="fdsfsfsf"),
    User(id=2, name="test2", email="ifdjmif@mail.ru", password="fdsawfd"),
]


@router.get("/")
async def root():
    return "Hello world"


@router.get("/user/", response_model=list[User])
async def get_users():
    return users


@router.get("/user/{user_id}", response_model=User)
async def one_user(user_id: int):
    if len(users) < user_id:
        raise HTTPException(status_code=404, detail="User not Found")
    return users[user_id - 1]


@router.post("/users/", response_model=list[User])
async def new_user(new_user: UserIn):
    new_user = User(
        id=len(users) + 1,
        name=new_user.name,
        email=new_user.email,
        password=new_user.password,
    )
    users.append(new_user)
    return users


@router.put("/user/{user_id}", response_model=list[User])
async def edit_user(user_id: int, edit_user: UserIn):
    for user in users:
        if user.id == user_id:
            user.name = edit_user.name
            user.email = edit_user.email
            user.password = edit_user.password
            return users
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/user/{user_id}")
async def del_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f"Пользователь удален"
    raise HTTPException(status_code=404, detail="User not found")
