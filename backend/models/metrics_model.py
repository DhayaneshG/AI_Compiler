from pydantic import BaseModel


class Metrics(BaseModel):
    generation_time: float
    validation_passed: bool
    repair_count: int
    