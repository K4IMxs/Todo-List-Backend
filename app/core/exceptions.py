"""Exceções de domínio (ou de negócio) da aplicação.
"""

class ErroDeDominio(Exception):
    """Classe base de todo erro previsto de negócio. """
    mensagem = "Não foi possível concluir a operação."
    def __init__(self, mensagem: str | None = None) -> None:
        self.mensagem = mensagem or type(self).mensagem
        super().__init__(self.mensagem)

class RecursoNaoEncontrado(ErroDeDominio):
    """Pediram um registro que não existe."""

    mensagem = "Recurso não encontrado."

class UsuarioNaoEncontrado(RecursoNaoEncontrado):
    mensagem = "Usuário não encontrado."

class RegraDeNegocioViolada(ErroDeDominio):
    """A operação é compreensível, mas contraria uma regra do negócio."""
    mensagem = "Operação recusada por uma regra de negócio."

class ValorInvalido(RegraDeNegocioViolada):
    """Valor fora do conjunto aceito por um campo do domínio."""
    mensagem = "Valor inválido para o campo."

class EmailJaCadastrado(ErroDeDominio):
    """RN-01: Um mesmo e-mail não pode ser usado mais de uma vez."""
    mensagem = "Ja existe uma conta com este e-mail."

class NaoAutentiado(ErroDeDominio):
    """Família de erros de identidade - a camada HTTP traduz em 401"""
    mensagem = "É preciso entrar na conta para continuar"

class CredenciaisInvalidas(NaoAutentiado):
    """E-mail ou senha não conferem."""
    mensagem = "E-mail ou senha inválidos."
class TokenInvalido(NaoAutentiado):
    """Token de acesso ausente, expirado, adulterado ou de usuário removido."""
    mensagem = "Sessão inválida. Entre na conta novamente para continuar."