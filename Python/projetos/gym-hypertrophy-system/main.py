from app.domain.models import Exercicio, PlanoTreino
from app.domain.services import ProgressaoService

def executar_treino_hoje():
    # Simulando o treino de segunda: Back, Triceps e Forearm
    meu_treino = PlanoTreino("Segunda-feira")
    
    puxada_alta = Exercicio("Puxada Alta", 4, 12, 60.0)
    meu_treino.adicionar_exercicio(puxada_alta)

    print(f"Iniciando treino de {meu_treino.dia_semana}...")
    
    # Simulação: O atleta fez 12 repetições (bateu o teto)
    nova_carga = ProgressaoService.calcular_nova_carga(puxada_alta, reps_feitas=12)
    puxada_alta.carga_atual = nova_carga

if __name__ == "__main__":
    executar_treino_hoje()
