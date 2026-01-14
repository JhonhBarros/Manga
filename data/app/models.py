from pydantic import BaseModel
from typing import Dict, Any

class Product(BaseModel):
    """
    Product model used for validation and serialization.
    """
    id: int
    name: str
    image_url: str
    description: str
    price: float
    rating: float
    specifications: Dict[str, Any]