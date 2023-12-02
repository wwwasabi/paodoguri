import mysql.connector

class Registro:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '13101990',
            database = 'paodoguri'
        )

        self.cursor = self.conexao.cursor()
        
    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
        
    
    def cadastrar_item(self, conteudo):
        value = ', '.join(['%s'] * len(conteudo))

        sql = f"INSERT INTO item (data_venda, valor_bruto, valor_liquido, quantidade_vendida, descricao, produto_id, venda_id)  VALUES ({value})"
        
        self.cursor.execute(sql, conteudo)
        self.conexao.commit()
        
    
    def alterar_item(self, id, colunas):
        # Use placeholders para as colunas a serem atualizadas
        sql = f"UPDATE item SET {', '.join([f'{coluna} = ?' for coluna in colunas])} WHERE id = ?"

        # Adicione a coluna 'id' à lista de colunas
        parametros = colunas + [id]

        # Execute a consulta SQL
        self.cursor.execute(sql, parametros)
        self.conexao.commit()

    
    def excluir_item(self, id):
        sql = "DELETE FROM item WHERE id = ?"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
    

    def mostrar_item(self):
        sql = "SELECT * FROM item"
        self.cursor.execute(sql)
        
        resultados = self.cursor.fetchall()
        
        for resultado in resultados:
            print(resultado)
        
        return resultado