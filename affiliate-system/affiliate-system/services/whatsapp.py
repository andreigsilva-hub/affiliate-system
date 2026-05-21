import webbrowser
import urllib.parse


def enviar_whatsapp(numero, mensagem):
    texto = urllib.parse.quote(mensagem)
    url = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    webbrowser.open(url)
