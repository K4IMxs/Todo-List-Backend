"""Contrato JSON de tarefa."""

from datetime import date

from pydantic import Field

from app.models.enums import PrioridadeTarefa, StatusTarefa
from app.schemas.base import DataHoraUTC, EsquemaDeEntrada, EsquemaDeSaida

# ----------------------------------------------------------------------------- Tarefa

class TarefaCreate(EsquemaDeEntrada):
    """Dados para criar uma tarefa."""

    titulo: str = Field(min_length=1, max_length=200)
    prioridade: PrioridadeTarefa = PrioridadeTarefa.MEDIA
    prazo: date | None = None

class TarefaUpdate(EsquemaDeEntrada):
    """Campos que podem ser alterados. Todos opcionais(atualização parcial)."""

    titulo: str | None = Field(default=None, min_length=1, max_length=200)
    prioridade: PrioridadeTarefa | None = None
    prazo: date | None = None

class TarefaOut (EsquemaDeSaida):
    """Representação completa de uma tarefa nas respostas da API"""

    id: int
    usuario_id: int
    titulo: str
    status: StatusTarefa
    prioridade: PrioridadeTarefa
    prazo: date | None
    criado_em: DataHoraUTC
    atualizado_em: DataHoraUTC
    concluido_em: DataHoraUTC | None