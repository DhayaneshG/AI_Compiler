from pydantic import BaseModel
from typing import List


class RolePermission(BaseModel):
    name: str
    permissions: List[str]


class AuthSchema(BaseModel):
    roles: List[RolePermission]