from pydantic import BaseModel
from typing import List


class Table(BaseModel):
    name: str
    fields: List[str]


class DBSchema(BaseModel):
    tables: List[Table]