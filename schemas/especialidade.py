from pydantic import BaseModel
from typing import Optional, List
from model.especialidade import Especialidade
from datetime import datetime


class EspecialidadeSchema(BaseModel):
    """ Define como um novo especialidade a ser inserido deve ser representado
    """
    nome: str
        
class EspecialidadeBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do especialidade.
    """
    nome: str = "Eduardo Cruz"

class ListagemEspecialidadesSchema(BaseModel):
    """ Define como uma listagem de especialidades será retornada.
    """
    especialidades:List[EspecialidadeSchema]

def apresenta_especialidades(especialidades: List[Especialidade]):
    """ Retorna uma representação do especialidade.
    """
    lista_especialidades = []
    for especialidade in especialidades:
        lista_especialidades.append({ 
            "nome": especialidade.nome
        })

    return {"especialidades": lista_especialidades}

def apresenta_especialidade(especialidade: Especialidade):
    """ Retorna uma representação do especialidade.
    """
    return {
        "nome": especialidade.nome,
    }



class EspecialidadeDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

class EspecialidadeViewSchema(BaseModel):
    """ Define como um especialidade será retornado.
    """
    nome: str = "Eduardo Cruz"
