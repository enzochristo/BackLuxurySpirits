from pydantic import BaseModel

class AddToCartDTO(BaseModel):
    product_id: str
    previous_price: float
