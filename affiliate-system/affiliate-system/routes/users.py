from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users")
def criar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    novo_usuario = User(
        nome=user.nome,
        telefone=user.telefone,
        affiliate_link=user.affiliate_link
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario


@router.get("/users")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(User).all()
