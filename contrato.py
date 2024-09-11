from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, validator


class ProdutoEnum(str, Enum):
    produto1 = "Consignado INSS"
    produto2 = "Consignado Privado"
    produto3 = "FGTS"

class Venda(BaseModel):
    """"
    Modelo de dados para a venda

    Args:
        email (EmailStr): email do vendedor
        nome (str): nome do vendedor
        data (datetime): data da venda
        valor (PositiveFloat): valor da venda
        produto (ProdutoEnum): produto vendido
    """

    email: EmailStr
    nome: str
    data: datetime
    valor: PositiveFloat
    produto: ProdutoEnum