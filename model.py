from tinydb import TinyDB, Query
from pathlib import Path
from dataclasses import asdict, dataclass


db_path = Path(__file__).parent / 'clientes.json'
db = TinyDB(db_path, indent=4)


@dataclass
class Crud:

    nome: str
    telefone: str
    endereco: str

    def as_dict(self):
        return asdict(self)

    CrudQuery = Query()
