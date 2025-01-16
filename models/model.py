from sqlmodel import Field, SQLModel, Relationship
from decimal import Decimal
from datetime import date
from typing import List ## O List vai ser usado para listar elementos de um tipo específico, no nosso caso, listar do tipo Products, que é a nossa tabela.

class Categorys(SQLModel, table= True):
    id: int = Field(primary_key=True)
    name: str
    products: List['Products'] = Relationship(back_populates='categorys') ##Aqui estamos armazenando dentro de products um lista dos valores da tabela, e também passando o back populates que expliquei abaixo

class Products(SQLModel, table= True):
    id: int = Field(primary_key=True)
    name: str
    kg_price: Decimal
    quantity: int ## Por KG ou Unidade
    expiration_date: date = Field(default = None)
    enter_date: date
    active: str = Field(default = 'Active') ##Active or Inactive
    category_id: int = Field(foreign_key='categorys.id')
    categorys: Categorys = Relationship(back_populates='products') ##fiz a relação com a tabela categorys, o back populates, permite que a gente consiga chamar algo como print(products.categorys.name) e consiga chamar o nome da categoria do produto especifico