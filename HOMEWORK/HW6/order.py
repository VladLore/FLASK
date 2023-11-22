from fastapi import APIRouter
from model import Order, OrderIn
from db import database, orders,users,products

router = APIRouter()

@router.get('/orders/', response_model=list[OrderIn])
async def get_order():
    query= orders.select()
    return await database.fetch_all(query)

@router.get('/orders/{order_id}', response_model=OrderIn)
async def one_order(order_id: int):
    query = orders.select().where(order_id=orders.c.id)
    return await database.fetch_one(query)

@router.post('/orders/')
async def creat_order(oreder: OrderIn):
    query= orders.insert().values(

    )