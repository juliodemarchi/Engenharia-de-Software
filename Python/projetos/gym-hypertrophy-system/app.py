from flask import Flask, render_template, request, redirect
import os

# Importando sua lógica de Engenharia de Software
from app.domain.models import Exercicio
from app.domain.services import ProgressaoService
from app.data.repository import TreinoRepository

app = Flask(__name__)

# Instanciando as camadas de dados e lógica
repo = TreinoRepository()
servico = ProgressaoService()

@app.route('/')
def index():
    # Carrega o histórico do seu arquivo JSON
    historico = repo.carregar()
    return render_template('index.html', historico=historico)

@app.route('/treinar', methods=['POST'])
def treinar():
    # Coleta os dados do formulário da página Web
    nome = request.form.get('nome')
    carga_atual = float(request.form.get('carga'))
    reps_feitas = int(request.form.get('reps'))
    
    # Criamos o objeto de domínio (Model)
    # Definimos 12 como a meta de repetições padrão
    exercicio = Exercicio(nome, 3, 12, carga_atual)
    
    # Aplicamos a regra de negócio (Service)
    nova_carga = servico.calcular_nova_carga(exercicio, reps_feitas)

    # Salvamos a nova carga no "Banco de Dados" (JSON)
    historico = repo.carregar()
    historico[nome] = round(nova_carga, 2)
    repo.salvar(historico)

    # Redireciona de volta para a página inicial para ver o resultado
    return redirect('/')

if __name__ == "__main__":
    # Porta padrão para o Flask
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)