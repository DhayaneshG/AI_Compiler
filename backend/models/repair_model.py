from pydantic import BaseModel
from typing import List


class RepairResult(BaseModel):
    repaired: bool
    repaired_components: List[str]
    message: str