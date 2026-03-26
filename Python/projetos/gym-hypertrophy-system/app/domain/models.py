from dataclasses import dataclass
from typing import List

@dataclass
class Exercicio:
    nome: str
    series: int
    repeticoes: int
    carga_atual: float

class PlanoTreino:
    def __init__(self, dia_semana: str):
        self.dia_semana = dia_semana
        self.exercicios: List[Exercicio] = []

    def adicionar_exercicio(self, exercicio: Exercicio):
        self.exercicios.append(exercicio)
