from fastapi import APIRouter
from model import Products, ProductsIn
from db import products, database

router = APIRouter()


@router.get("/products/", response_model=list[Products])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{product_id}", response_model=Products)
async def one_product(product_id: int):
    query = products.select().where(product_id == products.c.id)
    return await database.fetch_one(query)


@router.post("/products/")
async def creat_product(product: ProductsIn):
    query = products.insert().values(
        title=product.title, description=product.description, price=product.price
    )
    await database.execute(query)
    return "Продукт создан"


@router.put("/products/{product_id}")
async def edit_product(product_id: int, new_product: ProductsIn):
    query = (
        products.update()
        .where(product_id == products.c.id)
        .values(
            title=new_product.title,
            description=new_product.description,
            price=new_product.price,
        )
    )
    await database.execute(query)
    return new_product


@router.delete("/products/{product_id}")
async def del_product(product_id: int):
    query = products.delete().where(product_id == products.c.id)
    await database.execute(query)
    return "Пользователь удален"
