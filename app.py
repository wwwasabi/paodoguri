from flask import Flask, render_template, request
from crud import Registro
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

    if request.method == 'POST':
        sabor = request.form['sabor']
        quantidade = request.form['quantidade']

        if sabor == 'Outros':
            descricao = request.form['descricao']
            valor = request.form['valor']
            resultado = f"Registrando {quantidade} unidades de {sabor} - {descricao} por R${valor} cada."
        else:
            resultado = f"Registrando {quantidade} unidades de {sabor}."
            
            #Registrando a venda
            conteudo = ('2003-12-12', 10, 10, quantidade,'', 3, 1)
            r.cadastrar_item(conteudo)
            
        return render_template('resultado.html', resultado=resultado)
    return render_template('registrar_pao.html', sabores=sabores)

if __name__ == '__main__':
    app.run(debug=True)
