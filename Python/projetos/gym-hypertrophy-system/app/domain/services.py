# Adicione esta linha no topo para que o serviço conheça o modelo
from app.domain.models import Exercicio

class ProgressaoService:
    @staticmethod
    def calcular_nova_carga(exercicio: Exercicio, reps_feitas: int) -> float:
        """
        Regra: Se atingiu o teto de repetições, aumenta 5% da carga.
        """
        if reps_feitas >= exercicio.repeticoes:
            nova_carga = exercicio.carga_atual * 1.05
            print(f"✅ Meta batida no {exercicio.nome}! Nova carga sugerida: {nova_carga:.2f}kg")
            return nova_carga
        return exercicio.carga_atual
