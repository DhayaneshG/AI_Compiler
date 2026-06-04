from pydantic import BaseModel
from typing import List


class Intent(BaseModel):
    app_name: str
    features: List[str]
    roles: List[str]