from fastapi import FastAPI
import uvicorn
from db import database
import user
import product
import order

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(user.router, tags=["Users"])

app.include_router(product.router, tags=["Products"])

app.include_router(order.router, tags=["Order"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
