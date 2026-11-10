"""Operações sobre as tarefas do usuário autenticado."""

from __future__ import annotations

from datetime import date

from app.models import Tarefa
from app.models.enums import PrioridadeTarefa
from app.repositories import TarefaRepositorio

class TarefaServico:
    """Operacoes sobre as tarefas do usuario autenticado.

    Toda operacao recebe o id de quem esta pedindo. Isso não é desconfiança
    exagerada: e a unica forma de garantir que ninguem leia, altere ou apague
    tarefa de outra pessoa so por adivinhar um id.
    """

    def __init__(self, tarefas: TarefaRepositorio) -> None:
        self._tarefas = tarefas

    def criar(
        self,
        usuario_id: int,
        titulo: str,
        prioridade: PrioridadeTarefa,
        prazo: date | None,
    ) -> Tarefa:
        """Cria uma tarefa para o usuário autenticado
        """
        tarefa = Tarefa(
            usuario_id=usuario_id,
            titulo=titulo,
            prioridade=prioridade,
            prazo=prazo,
        )
        return self._tarefas.salvar(tarefa)
    
    def listar(self, usuario_id: int) -> list[Tarefa]:
        """Lista as tarefas do usuário autenticado."""
        return self._tarefas.listar(usuario_id)