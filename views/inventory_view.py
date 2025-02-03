import __init__
from models.database import engine ## Importando o engine que a gente criou no database.py
from models.model import Products, Categorys ## Importando as tabelas
from sqlmodel import Session, select, text
from datetime import date
from sqlalchemy import or_
import unicodedata
import re

class InventoryManagement():
    def __init__(self, engine):
        self.engine = engine

    def create_product(self, product: Products): ## Criei uma instância product que herda da tabela Products e estou adicionando um único produto na tabela
        with Session(engine) as session:
                session.add(product)
                session.commit()
            
    def list_query_products(self, query):
        with Session(engine) as session:
            statement = select(Products, Categorys.name).join(Categorys).where(or_(Products.name == query, Categorys.name == query)) ##To fazendo mais de uma verificação no where, para o usuario poder pesquisar não so apenas pelo nome, porém categoria,etc
            results = session.exec(statement).all() ## Depois de selecionar, o result vai retornar para a gente a tabela, agora precisamos dizer que queremos todos os valores da tabela, com o all

            self.table_content = []
            for products, category in results: ##Como a consulta tem o join, ele retorna uma tupla, com valores de Products e Categorys,é preciso criar um for que pegue os dois valores
                self.table_content.append([
                    products.id,
                    products.name,
                    f"{products.kg_price:.2f}",
                    products.quantity,
                    products.expiration_date,
                    products.enter_date,
                    products.active,
                    category,
                ])
            return self.table_content
    
    def create_table_view(self):
        with Session(engine) as session:
            statement = select(Products, Categorys.name).join(Categorys)
            results = session.exec(statement).all()
            
            self.table_content = []
            for products, category in results: ##Como a consulta tem o join, ele retorna uma tupla, com valores de Products e Categorys,é preciso criar um for que pegue os dois valores
                self.table_content.append([
                    products.id,
                    products.name,
                    f"{products.kg_price:.2f}",
                    products.quantity,
                    products.expiration_date,
                    products.enter_date,
                    products.active,
                    category,
                ])
            return self.table_content
           
    def get_category_id_by_name(self, name):
        with Session(engine) as session:
            statement = select(Categorys).where(Categorys.name == name)
            result = session.exec(statement).first()
            if result:
                return result.id
            else:
                new_category = Categorys(name = name)
                session.add(new_category)
                session.commit()
                return new_category.id
            
    def count_products(self):
        with Session(engine) as session:
            statement = select(Products)
            results = session.exec(statement).all()

            total = 0
            for result in results:
                total += 1
            
            return total
        
    def list_categorys_name(self):
        with Session(engine) as session:
            statement = select(Categorys)
            results = session.exec(statement).all()
            category_name = [result.name for result in results]

            return category_name


im = InventoryManagement(engine)  


# coxinha = Products(name = 'Coxinha', kg_price = '27.50', quantity = 15, enter_date = date.today(), expiration_date=date(2025, 10, 21) , category_id= 3)

# im.create_product(coxinha)




# FUNCTIONS THAT I'M NOT USING ANYMORE, BUT COULD USE LATER:

# def get_category_name_by_id(self, category_id):
#     with Session(engine) as session:
#         statement = select(Categorys).where(Categorys.id == category_id)
#         result = session.exec(statement).first()
#         return result

 
 
 # def get_category_id_by_name(self, name):
    #     with Session(engine) as session:
    #         statement = select(Categorys).where(Categorys.name == name)
    #         result = session.exec(statement).first()
    #         if result:
    #             return result.id
    #         else:
    #             new_category = Categorys(name = name)
    #             session.add(new_category)
    #             session.commit()
    #             return new_category.id

# ----------------------------------------------------------------------------------

    # def list_columns_table(self):
    #     self.column_content = []

    #     ##Separei os dois laços de repetições pois a coluna repetia por conta dos produtos
    #     for produto in self.list_products():
    #             self.column_content.append(
    #                     list(produto.model_fields.keys()) ##aqui estou usando model_fields que retorna todos os valores e chaves do banco de dados, porém utilizando keys para pegar apenas as chaves, para as colunas. Como eu quero que o resultado seja tipo [['id']], com duas listas, pois vou utilizar o CTkTable, fiz dessa forma utilizando append e list
    #                 )
    #             break
    
    #     return self.column_content

#-----------------------------------------------------------------------------------------
 
    #def list_rows_table(self):
        # self.table_content = []

        # for produto in self.list_products():
        #     category = self.get_category_name_by_id(produto.category_id)
        #     self.table_content.append([ ##Estou utilizando 2 listas por conta do TreeView(precisa ser dessa forma)
        #     produto.id,
        #     produto.name,
        #     f"{produto.kg_price:.2f}",
        #     produto.quantity,
        #     produto.expiration_date,
        #     produto.enter_date,
        #     produto.active,
        #     category.name,
        #     ])

        # return self.table_content
