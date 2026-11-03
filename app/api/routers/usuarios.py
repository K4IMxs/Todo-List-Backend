"""Endpoints de usuário: cadastro.

A rota traduz HTTP em uma chamada de serviço e devolve o resultado. Não há
consulta ao banco, `if` de regra de negócio nem `raise HTTPException`: os erros
de negócio sobem com exceções de domínio e são convertido em código de status por `main.py`.
"""

from typing import Annotated
from fastapi import APIRouter, Depends, status
from app.api.dependencies import obter_usuario_servico
from app.schemas import SessaoOut, UsuarioCreate, UsuarioLogin, UsuarioOut
from app.services import UsuarioServico
router = APIRouter(prefix="/usuarios", tags=["Usuários"])
@router.post(
    "",
    response_model=UsuarioOut,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar usuário",
    responses={409: {"description": "E-mail ja cadastrado."}},
)
def cadastrar_usuario(
    dados: UsuarioCreate,
    servico: Annotated[UsuarioServico, Depends(obter_usuario_servico)],
) -> UsuarioOut:
    """Cadastra um novo usuário com a senha armazenada como hash."""
    return servico.cadastrar(dados.nome, dados.email, dados.senha)

@router.post(
    "/login",
    response_model=SessaoOut,
    summary="Entrar (receber o token de acesso)",
    responses={401: {"description": "E-mail ou senha inválidos."}},
)
def entrar(
    dados: UsuarioLogin,
    servico: Annotated[UsuarioServico, Depends(obter_usuario_servico)],
) -> SessaoOut:
    """Autentica e devolve o token de acesso."""
    sessao = servico.entrar(dados.email, dados.senha)
    return SessaoOut(
        access_token=sessao.token.valor,
        expira_em=sessao.token.expira_em,
        usuario=UsuarioOut.model_validate(sessao.usuario)
)