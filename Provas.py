from datetime import date, datetime, timedelta
import random
from Banco_de_dados import *
days_notificacao = 3

def notifica_provas():
    data_atual = datetime.now().date()
    data_notificacao = data_atual + timedelta(days=days_notificacao)
    read = read_bd('data', 'prova')
    for prova in read():
        if data_atual == data_notificacao.date():
            comando = f'SELECT name_prova FROM provas WHERE data_prova = {data_notificacao}'
            cursor.execute(comando)
            prova = cursor.fetchall()
            mensagem = random.choice(mensagem_alerta_prova)
            notificacao = f"{mensagem} {prova}"
            return notificacao
    conexao.close()