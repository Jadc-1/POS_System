import __init__
from models.database import engine ## Importando o engine que a gente criou no database.py
from models.model import Products, Categorys ## Importando as tabelas
from sqlmodel import Session, select

class InventoryManagement():
    def __init__(self, engine):
        self.engine = engine

    def create_product(self, product: Products): ## Criei uma instância product que herda da tabela Products e estou adicionando um único produto na tabela
        with Session(engine) as session:
            session.add(product)
            session.commit()

    def create_category(self, category: Categorys):
        with Session(engine) as session:
            session.add(category)
            session.commit()

    def list_products(self):
        with Session(engine) as session:
            statement = select(Products) ## statement é geralmente usado para consulta, ele vai selecionar todos os produtos da tabela Products
            results = session.exec(statement).all() ## Depois de selecionar, o result vai retornar para a gente a tabela, agora precisamos dizer que queremos todos os valores da tabela, com o all
            return results ##Aqui não quero adicionar nada na tabela, apenas retornar a tabela por completo ao usuário
    
        