from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    price: float

class Receipt(BaseModel):
    items: List[Item]
    date: str
    total_amount: float
