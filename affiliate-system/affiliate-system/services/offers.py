import random

produtos = [
    {
        "titulo": "Nike Air Max",
        "preco": "R$ 429",
        "link": "https://produto.com/nike"
    },
    {
        "titulo": "Fone JBL",
        "preco": "R$ 199",
        "link": "https://produto.com/jbl"
    }
]


def buscar_oferta():
    return random.choice(produtos)
