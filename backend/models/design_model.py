from pydantic import BaseModel
from typing import List


class Design(BaseModel):
    entities: List[str]
    flows: List[str]