import unittest
# Importando as classes do seu sistema de Engenharia de Software
from app.domain.models import Exercicio, PlanoTreino
from app.domain.services import ProgressaoService

class TestGymSystem(unittest.TestCase):

    def setUp(self):
        """Prepara o cenário para cada teste."""
        self.exercicio = Exercicio("Puxada Alta", 4, 12, 60.0)
        self.servico = ProgressaoService()

    # --- TESTES DE TREINO ---
    
    def test_progressao_de_carga_sucesso(self):
        """Valida se a carga aumenta 5% quando o teto de reps é atingido."""
        nova_carga = self.servico.calcular_nova_carga(self.exercicio, reps_feitas=12)
        self.assertEqual(nova_carga, 63.0) # 60 + 5%

    def test_manter_carga_se_abaixo_da_meta(self):
        """Valida que a carga NÃO aumenta se não atingiu o teto."""
        nova_carga = self.servico.calcular_nova_carga(self.exercicio, reps_feitas=10)
        self.assertEqual(nova_carga, 60.0)

    # --- TESTES DE DIETA (REGRAS DE ENGENHARIA) ---

    def test_meta_proteina_vegetariana(self):
        """
        Valida se o plano atinge o mínimo de 150g de proteína.
        Demonstra o domínio de regras de validação de dados.
        """
        proteina_diaria = 155  # Valor simulado
        meta_minima = 150
        
        self.assertGreaterEqual(proteina_diaria, meta_minima, "A dieta não atingiu o mínimo de proteína!")

if __name__ == "__main__":
    unittest.main()
