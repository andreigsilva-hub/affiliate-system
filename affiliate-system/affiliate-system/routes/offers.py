from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

from services.offers import buscar_oferta
from services.affiliate import gerar_link_afiliado
from services.whatsapp import enviar_whatsapp

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/send-offers")
def enviar_ofertas(db: Session = Depends(get_db)):
    usuarios = db.query(User).all()

    for usuario in usuarios:
        try:
            oferta = buscar_oferta()

            link = gerar_link_afiliado(
                oferta['link'],
                usuario.affiliate_link
            )

            mensagem = (
                f"🔥 OFERTA IMPERDIVEL 🔥\n\n"
                f"{oferta['titulo']}\n"
                f"💰 {oferta['preco']}\n\n"
                f"🛒 Comprar:\n{link}"
            )

            enviar_whatsapp(usuario.telefone, mensagem)

        except Exception as e:
            print(f"Erro ao enviar para {usuario.nome}: {e}")

    return {"message": "Ofertas enviadas"}
