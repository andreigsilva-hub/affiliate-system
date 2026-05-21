from pydantic import BaseModel


class UserCreate(BaseModel):
    nome: str
    telefone: str
    affiliate_link: str


class UserResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    affiliate_link: str

    class Config:
        orm_mode = True
