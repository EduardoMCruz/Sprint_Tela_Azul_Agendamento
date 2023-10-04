from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Especialidade(Base):
    __tablename__ = 'especialidade'

    nome = Column("Nome", String(140), primary_key=True)

    def __init__(self, nome:str):
        """
        Cria uma especialidade

        Arguments:
            nome: nome da especialidade

        """
        self.nome = nome
        