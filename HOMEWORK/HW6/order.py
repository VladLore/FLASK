from fastapi import APIRouter
from model import Order, OrderIn, ReadOrder
from db import database, orders, users, products
from sqlalchemy import select

router = APIRouter()


@router.get("/orders/", response_model=list[Order])
async def get_order():
    query = orders.select()
    return await database.fetch_all(query)


# @router.get("/orders/{order_id}", response_model=OrderIn)
# async def one_order(order_id: int):
#     query = orders.select().where(order_id=orders.c.id)
#     return await database.fetch_one(query)


# @router.get("/orders/{user_id}")
# async def select_tst(user_id: int):
    # query = (
    #     orders.select(
    #         orders.c.date,
    #         orders.c.status,
    #         products.c.title,
    #         products.c.title,
    #     )
    #     .join(users.id)
    #     .where(user_id == users.c.id)
    # )
    # await database.fetch_all(query)

    # query = select([orders.c.date,orders.c.status,products.c.title,products.c.price]).where(user_id == users.c.id)
    # # .where(orders.c.product_id==products.c.id)
    # print(query)
    # return await database.fetch_all(query)

@router.post("/orders/")
async def creat_order(order: OrderIn):
    query = orders.insert().values(
        user_id=order.user_id,
        product_id=order.product_id,
        date= order.date,
        status=order.status
    )
    await database.execute(query)
    return order

@router.put('/orders/{order_id}')
async def edit_order(order_id:int, new_order: Order):
    query = orders.update().where(orders.c.id==order_id).values(
        user_id=new_order.user_id,
        product_id=new_order.product_id,
        date = new_order.date,
        status = new_order.status
    )
    await database.execute(query)
    return 'Заказ изменен'


@router.delete('/orders/{order_id}')
async def del_order(order_id: int):
    query= orders.delete().where(orders.c.id==order_id)
    await database.execute(query)
    return 'Пользоатель удален'