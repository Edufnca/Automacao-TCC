import requests
import random
from Dicionario import *
from datetime import datetime
from Banco_de_dados import *

API_Key = "c48e4df2bbde99b3dd8a3cdeaab76d41"

cidade = 'itatiba'

#   Requesição do Json
link_request = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_Key}&lang=pt_br'
request = requests.get(link_request)
weather = request.json()

#   Uso do Json para pegar informações
Temp = weather['main']['temp'] - 273.15
TempC = int(Temp)  #transformção em Celsius
Tempo_descricao = weather['weather'][0]['description']
Tempo = weather['weather'][0]['main']
Tempo_max = weather['main']['temp_max'] - 273.15
Tempo_max = int(Tempo_max)
Tempo_min = weather['main']['temp_min'] - 273.15
Tempo_min = int(Tempo_min)
Umidade = weather['main']['humidity']
Nuvens = weather['clouds']['all']
Vento = weather['wind']['speed']
Vento = Vento * 3, 6
Vento = float(''.join(map(str, Vento)))
Vento = round(Vento)
Data = weather['dt']
Data = datetime.fromtimestamp(Data)


def notificacao_temperatura(hora_notificacao):
  hora = datetime.now()
  hora_notifica = hora.strftime("%H:%M")
  if hora_notifica == f"{hora_notificacao}":
    mensagem_temperatura()


def mensagem_temperatura():
  if TempC > 24 and TempC < 30:
    mensagem = random.choice(mensagem_temperatura_media)
    mensagem = mensagem + ' 🌞'
    return mensagem

  if TempC > 0 and TempC < 25:
    mensagem = random.choice(mensagem_temperatura_baixa)
    mensagem = mensagem + ' ⛄'
    return mensagem

  if TempC > 30:
    mensagem = random.choice(mensagem_temperatura_alta)
    mensagem = mensagem + ' 🔥'
    return mensagem


notificacao_temperatura("06:30")
