from datetime import datetime

from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    value: int


class ItemResponse(BaseModel):
    id: int
    name: str
    value: int
    created_at: datetime

    model_config = {"from_attributes": True}