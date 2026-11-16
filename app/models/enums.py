"""Enumerações do domínio.

Antes, os valores validos de status e prioridade estavam escritos como texto
solto em tres lugares: no 'Literal' dos schemas, no 'default' das colunas e no
case' que ordenava por prioridade. Acrescentar uma prioridade nova exigia
lembrar dos tres. Aqui eles passam a ter um unico lugar de definicão.

Herdar de 'str' faz cada membro se comportar como o proprio texto - o que
permite grava-lo em uma coluna `String`, compara-lo com uma string vinda do
banco e serializa-lo em JSON sem conversao manual.
"""

from enum import Enum

class StatusTarefa(str, Enum):
    """Status de uma tarefa."""

    PENDENTE = "pendente"
    CONCLUIDA = "concluída"

class PrioridadeTarefa(str, Enum):
    """Prioridade de uma tarefa."""

    BAIXA = "baixa"
    MEDIA = "média"
    ALTA = "alta"
    URGENTE = "urgente"
    @property
    def peso(self) -> int:
        """"Posicao na ordenacao por prioridade - 0 e a mais urgente.
        Ordenar pelo texto daria "alta, baixa, media, urgente", que nao e a
        ordem que o usuario espera ver. 0 peso existe para isso.
        """
        return _PESOS[self]
    @classmethod
    def mapa_de_pesos(cls) -> dict[str, int]:
        """Mapa `valor -> peso`, no formato que o `case()` do SQL consome."""
        return {prioridade.value: prioridade.peso for prioridade in cls}
_PESOS = {
    PrioridadeTarefa.URGENTE: 0,
    PrioridadeTarefa.ALTA: 1,
    PrioridadeTarefa.MEDIA: 2,
    PrioridadeTarefa.BAIXA: 3,
}

class  CampoOrdenacao(str, Enum):
    """Campos pelos quais a listagem de tarefas pode ser ordenada.

    Os valores repetem o nome publico do campo na API (camelCase), porque é
    isso que o cliente envia em `?ordernarPor=`. Como é um enum, um valor fora
    da lista passa a ser recusado com 422 - antes, o codigo caía
    silenciosamente na ordenacão por data de criação e o cliente nunca sabia
    que seu parâmetro havia sido ignorado.
    """

    CRIADO_EM = "criadoEm"
    PRAZO = "prazo"
    PRIORIDADE = "prioridade"

class Ordem(str, Enum):
    """Sentido de ordenação."""

    ASC = "asc"
    DESC = "desc"