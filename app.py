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
        id_sabor = c.obter_id_do_sabor(mapeamento_sabores_id, sabor)
        quantidade = request.form['quantidade']

        if sabor == 'Outros':
            descricao = request.form['descricao']
            valor = request.form['valor']
            resultado = f"Registrando {quantidade} unidades de {sabor} - {descricao} por R${valor} cada."
            conteudo = (f'{data}', valor, c.valor_liquido(id_sabor), quantidade,f'{descricao}', id_sabor, 1)
            r.cadastrar_item(conteudo)
        else:
            resultado = f"Registrando {quantidade} unidades de {sabor}."
            
            #Registrando a venda
            conteudo = (f'{data}', c.valor_bruto(id_sabor), c.valor_liquido(id_sabor), quantidade,'', id_sabor, 1)
            r.cadastrar_item(conteudo)
            
        return render_template('resultado.html', resultado=resultado)
    return render_template('registrar_pao.html', sabores=sabores)

if __name__ == '__main__':
    app.run(debug=True)
