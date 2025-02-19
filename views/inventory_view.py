import __init__
import os
from models.database import engine ## Importando o engine que a gente criou no database.py
from models.model import Products, Categorys ## Importando as tabelas
from sqlmodel import Session, select
from datetime import date, datetime
import pandas as pd
from tkinter import filedialog
from customtkinter import CTkLabel

class InventoryManagement():
    def __init__(self, engine):
        self.engine = engine

    def create_product(self, product: Products): ## Criei uma instância product que herda da tabela Products e estou adicionando um único produto na tabela
        with Session(engine) as session:
                session.add(product)
                session.commit()
                session.refresh(product)
                
    def _list_products(self, results):
        self.table_content = []
        for products, category in results: ##Como a consulta tem o join, ele retorna uma tupla, com valores de Products e Categorys,é preciso criar um for que pegue os dois valores
            self.table_content.append([
                products.id,
                products.name,
                f"R$ {products.kg_price:.2f}",
                products.quantity,
                products.expiration_date,
                products.enter_date,
                products.active,
                category,
            ])
        return self.table_content

    def list_query_products(self, query):
        with Session(engine) as session:
            statement = select(Products, Categorys.name).outerjoin(Categorys).where(Products.name.like(f"%{query}%")) ##To fazendo mais de uma verificação no where, para o usuario poder pesquisar não so apenas pelo nome, porém categoria,etc
            results = session.exec(statement).all() ## Depois de selecionar, o result vai retornar para a gente a tabela, agora precisamos dizer que queremos todos os valores da tabela, com o all

            self.table = self._list_products(results)
            
            return self.table
        
    def list_query_categories(self, query):
        with Session(engine) as session:
            statement = select(Products,Categorys.name).outerjoin(Categorys).where(Categorys.name == query)
            results = session.exec(statement).all()

            self.table = self._list_products(results)

            return self.table

    def search_delete_product(self, name):
        with Session(engine) as session:
            statement = select(Products.name).where(Products.name == name)
            result = session.exec(statement).first()
            if result:
                return True
            else:
                return None
                
    def search_delete_category(self,name):
        with Session(engine) as session:
            statement = select(Categorys.name).where(Categorys.name == name)
            result = session.exec(statement).first()
            if result:
                return True
            else:
                return None

    def delete_product(self, name):
        with Session(engine) as session:
            statement = select(Products).where(Products.name == name)
            result = session.exec(statement).first()
            if result:
                session.delete(result)
                session.commit()
            else:
                return

    def delete_category(self,name):
        with Session(engine) as session:
            statement = select(Categorys).where(Categorys.name == name)
            result = session.exec(statement).first()
            if result:
                session.delete(result)
                session.commit()
            else:
                return
    
    def create_table_view(self):
        with Session(engine) as session:
            statement = select(Products, Categorys.name).outerjoin(Categorys)
            results = session.exec(statement).all()
            
            self.table = self._list_products(results)

            return self.table
           
    def get_category_id_by_name(self, name):
        with Session(engine) as session:
            statement = select(Categorys).where(Categorys.name == name)
            result = session.exec(statement).first()
            if result:
                return result.id
            else:
                new_category = Categorys(name = name.strip())
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
        
    def list_categories_name(self):
        with Session(engine) as session:
            statement = select(Categorys)
            results = session.exec(statement).all()
            category_name = [result.name for result in results]

            return category_name

    def get_total_categories(self):
        with Session(engine) as session:
            statement = select(Categorys)
            results = session.exec(statement).all()
            total = 0
            for category in results:
                total += 1
            return total

    def get_stock_value(self):
        with Session(engine) as session:
            statement = select(Products.kg_price, Products.quantity)
            results = session.exec(statement).all()
            total = 0
            for result in results:
                total += (result.kg_price * result.quantity)
        return f"R$ {total:.2f}"
    
    def choose_file(self):
        self.file = str(filedialog.askopenfilename(
            title="Choose a file",
            filetypes=[("Excel file", '.xlsx', '.xls'),("Txt file", '.txt')]
        ))

        if self.file:
            self.convert_file(self.file)

    def convert_file(self, file):
        #Verifica a extensão do arquivo
        self.file_path = file
        #Separo o nome da extensão
        self.file_name, self.file_extension = os.path.splitext(file)

        if self.file_extension in ['.xlsx', '.xls']:
            self.df = pd.read_excel(file, skiprows=1)
            self.df_name = file.replace(self.file_extension, ".txt")
            self.df.to_csv(self.df_name, sep=",", index=False)
            self._add_products(self.df_name)
        elif self.file_extension == ".txt":
            self._add_products(self.file_path)
        else: 
            return None

    def _add_products(self, file):
        with open(file, "r", encoding="UTF-8") as openfile:
            for index,line in enumerate(openfile):
                self.name = line.split(",")[0].strip()
                self.price = float(line.split(",")[1].strip())
                self.quantity = int(line.split(",")[2].strip())
                if index == 0:
                    self.enter_date = datetime.strptime(line.split(",")[4], r"%Y-%m-%d %H:%M:%S").date()
                    self.category = self.get_category_id_by_name(line.split(",")[5].strip())
                    if "Unnamed" in line.split(",")[3]: ##Caso expiration for vazio
                        product = Products(name=self.name, kg_price=self.price, quantity=self.quantity, expiration_date=None, enter_date=self.enter_date, category_id=self.category)
                    else:
                        self.expiration_date = datetime.strptime(line.split(",")[3], r"%Y-%m-%d %H:%M:%S").date()
                        product = Products(name=self.name, kg_price=self.price, quantity=self.quantity, expiration_date=self.expiration_date, enter_date=self.enter_date, category_id=self.category)
                    self.create_product(product)   
                else:
                    if line.split(",")[3] == "":
                        try:
                            self.enter_date = datetime.strptime(line.split(",")[4], r"%Y-%m-%d").date() #Transformo todo o codigo em um tipo de dado date
                        except ValueError:
                            self.enter_date = datetime.strptime(line.split(",")[4], r"%Y-%m-%d %H:%M:%S").date() 
                        self.category = self.get_category_id_by_name(line.split(",")[5].strip())
                        product = Products(name=self.name, kg_price=self.price, quantity=self.quantity, expiration_date=None, enter_date=self.enter_date, category_id=self.category)
                        self.create_product(product)
                    else:
                        try:
                            self.expiration_date = datetime.strptime(line.split(",")[3], r"%Y/%m/%d").date()
                            self.enter_date = datetime.strptime(line.split(",")[4], r"%Y/%m/%d").date() 
                        except ValueError:
                            self.expiration_date = datetime.strptime(line.split(",")[3], r"%Y-%m-%d").date()
                            self.enter_date = datetime.strptime(line.split(",")[4], r"%Y-%m-%d").date() 
                        self.category = self.get_category_id_by_name(line.split(",")[5].strip())
                        product = Products(name=self.name, kg_price=self.price, quantity=self.quantity, expiration_date=self.expiration_date, enter_date=self.enter_date, category_id=self.category)
                        self.create_product(product)
                  

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
