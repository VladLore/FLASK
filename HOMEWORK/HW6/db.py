import databases
import sqlalchemy
from setting import settings

"""
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
"""

DATASBASE_URL = settings.DATABASE_URL
database = databases.Database(DATASBASE_URL)
metadata = sqlalchemy.MetaData()

products = sqlalchemy.Table('products', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer, primary_key = True),
                            sqlalchemy.Column('title', sqlalchemy.String(50)),
                            sqlalchemy.Column('description', sqlalchemy.String(128)),
                            sqlalchemy.Column('price', sqlalchemy.Integer))

users = sqlalchemy.Table('user',metadata,
                        sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                        sqlalchemy.Column('surname', sqlalchemy.String(128)),
                        sqlalchemy.Column('name', sqlalchemy.String(128)),
                        sqlalchemy.Column('email', sqlalchemy.String(128)),
                        sqlalchemy.Column('adress', sqlalchemy.String(128)),
                        sqlalchemy.Column('password', sqlalchemy.String(128)))

orders = sqlalchemy.Table('order',metadata,
                         sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column('user_id', sqlalchemy.Integer,sqlalchemy.ForeignKey('user.id')),
                         sqlalchemy.Column('product_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('products.id')),
                         sqlalchemy.Column('date', sqlalchemy.Date),
                         sqlalchemy.Column('status', sqlalchemy.Boolean))



engine = sqlalchemy.create_engine(DATASBASE_URL)
metadata.create_all(engine)