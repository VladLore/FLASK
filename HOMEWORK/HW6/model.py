from pydantic import BaseModel, Field
from datetime import date


class User(BaseModel):
    id: int
    surname: str
    name: str
    email: str
    adress: str
    password: str


class Products(BaseModel):
    id: int
    title: str
    description: str
    price: int


class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    date: date
    status: bool


class UserIn(BaseModel):
    surname: str
    name: str
    email: str
    adress: str
    password: str


class ProductsIn(BaseModel):
    title: str
    description: str
    price: int


class OrderIn(BaseModel):
    user_id: int
    product_id: int
    date: date
    status: bool

class ReadOrder(BaseModel):
   product_id: int
   date: date
   status: bool
   title: str
   price: int
