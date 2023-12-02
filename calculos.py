import mysql.connector
from datetime import datetime

class Calcular:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            username = 'root',
            password = '13101990',
            database = 'paodoguri'
        )
        
        self.cursor = self.conexao.cursor()
    
    def desconectar(self):
        self.cursor.close()
        self.conexao.close()
        
    def data_venda(self):
        data_venda = datetime.now()
        data_venda_configurada = data_venda.strftime("%Y-%m-%d")
        return data_venda_configurada
    
    def valor_bruto(self, id):
        sql = f'SELECT preco FROM produto WHERE id = {id}'
        self.cursor.execute(sql)
        valor_bruto = self.cursor.fetchone()

        if valor_bruto:
            valor = valor_bruto[0]
            print("Valor:", valor)
            return valor
        else:
            print("Produto não encontrado.")
            return None
    
    def valor_liquido(self, id):
        sql = f'SELECT preco_producao FROM produto WHERE id = {id}'
        self.cursor.execute(sql)
        preco_producao = self.cursor.fetchone()
        
        if preco_producao:
            valor_liquido = self.valor_bruto(id) - preco_producao[0]
            print("Valor:", valor_liquido)
            return valor_liquido
        else:
            print("Produto não encontrado.")
            return None
    
    def obter_id_do_sabor(self, mapeamento, sabor_escolhido):
        # Use o mapeamento para obter o ID correspondente ao sabor escolhido
        print(mapeamento)
        print(mapeamento.get(sabor_escolhido))
        return mapeamento.get(sabor_escolhido)
        
        

calc = Calcular()
calc.valor_liquido(8)