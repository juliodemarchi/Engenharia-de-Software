import json
import os

class TreinoRepository:
    def __init__(self, arquivo="app/data/treino.json"):
        self.arquivo = arquivo

    def salvar(self, dados):
        """Salva o dicionário de treino no arquivo JSON."""
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"💾 Dados salvos em {self.arquivo}")

    def carregar(self):
        """Carrega os dados do arquivo. Se não existir, retorna um dicionário vazio."""
        if not os.path.exists(self.arquivo):
            return {}
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
        