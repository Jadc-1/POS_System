import __init__
from models.database import engine ## Importando o engine que a gente criou no database.py
from models.model import Products, Categorys ## Importando as tabelas
from sqlmodel import Session, select
from datetime import date

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
    
    def list_rows_table(self):
        self.table_content = []
        
        for produto in self.list_products():
            self.table_content.append([ ##Estou utilizando 2 listas por conta do TreeView(precisa ser dessa forma)
            produto.id,
            produto.name,
            produto.kg_price,
            produto.quantity,
            produto.expiration_date,
            produto.enter_date,
            produto.active,
            produto.category_id,
            ])


        return self.table_content
    
    def list_columns_table(self):
        self.column_content = []

        ##Separei os dois laços de repetições pois a coluna repetia por conta dos produtos
        for produto in self.list_products():
                self.column_content.append(
                        list(produto.model_fields.keys()) ##aqui estou usando model_fields que retorna todos os valores e chaves do banco de dados, porém utilizando keys para pegar apenas as chaves, para as colunas. Como eu quero que o resultado seja tipo [['id']], com duas listas, pois vou utilizar o CTkTable, fiz dessa forma utilizando append e list
                    )
                break
    
        return self.column_content



im = InventoryManagement(engine)  

#coca_cola = Products(name = 'Coca Cola', kg_price = 6.50, quantity = 5, enter_date = date.today(), category_id= 2)
#refrigerante = Categorys(name= "refrigerante")
#im.create_product(coca_cola)

#for i in im.list_products():
    #print(f"{i.id}, {i.name}, {i.kg_price}, {i.quantity}, {i.enter_date}, {i.category_id}")


