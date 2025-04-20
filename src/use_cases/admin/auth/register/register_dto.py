from pydantic import BaseModel


class RegisterDTO(BaseModel):
    name: str
    email: str
    password: str