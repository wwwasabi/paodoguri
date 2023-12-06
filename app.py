from flask import Flask, render_template, request
from crud import Registro
from calculos import Calcular
c = Calcular()
r = Registro()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def registrar_pao():
    sabores = [
        'Pão de Pizza',
        'Pão de Calabresa',
        'Pão de Frango',
        'Pão de Queijo Manteiga',
        'Pão de Marguerita',
        'Pão de Calabresa com Bacon',
        'Pão de Chocolate',
        'Pão de Carne de Sol na Nata',
        'Outros'
    ]
    
    #Data da venda
    data = c.data_venda()
    
    mapeamento_sabores_id = {sabor: str(i + 1) for i, sabor in enumerate(sabores)}
    
    if request.method == 'POST':
        sabor = request.form['sabor']
        quantidade = request.form['quantidade']
        id_sabor = c.obter_id_do_sabor(mapeamento_sabores_id, sabor)
        id_venda = c.venda(data)

        
        if sabor == 'Outros':
            descricao = request.form['descricao']
            valor = request.form['valor']
            conteudo = (f'{data}', valor, c.valor_liquido(id_sabor, quantidade), quantidade,f'{descricao}', id_sabor, id_venda)
            r.cadastrar_item(conteudo)            
        else:
            #Registrando a venda
            conteudo = (f'{data}', c.valor_bruto(id_sabor, quantidade), c.valor_liquido(id_sabor, quantidade), quantidade,'', id_sabor, id_venda)
            r.cadastrar_item(conteudo)
            
    return render_template('registrar_pao.html', sabores=sabores)

if __name__ == '__main__':
    app.run(debug=True)
