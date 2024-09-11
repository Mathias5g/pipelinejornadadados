from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, validator


class ProdutoEnum(str, Enum):
    produto1 = "Consignado INSS"
    produto2 = "Consignado Privado"
    produto3 = "FGTS"

class Venda(BaseModel):
    email: EmailStr
    nome: str
    data: datetime
    valor: PositiveFloat
    produto: ProdutoEnum