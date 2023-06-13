import mysql.connector
from Dicionario import *

conexao = mysql.connector.connect(
    host='192.168.0.90',
    user='pma',
    password='Franca21',
    port='3307',
    database='TCC',
    charset='utf8mb4'
)
cursor = conexao.cursor()

# TABELAS: anotacao, aula, compromisso, prova, tarefa

def add_prova(assunto, materia, data, dia_da_semana, aula):
    if dia_da_semana in dia_semana:
        try:
            comando_add_prova = f'INSERT INTO prova (assunto, materia, data, dia_da_semana, aula ) VALUES ("{assunto}", "{materia}", {data}, "{dia_da_semana}", {aula})'
            cursor.execute(comando_add_prova)
            conexao.commit()
            cursor.close()
            conexao.close()
            return "✅ Prova salva com sucesso!"
        except:
            msg_erro = '❌ Erro ao inserir prova.'
            return msg_erro
    else: return "Digite um dia da semana: Segunda, Terça, Quarta, Quinta, Sexta, Sabado, Domingo"

def add_tarefa(descricao, data, materia):
    try:
        comando_add_tarefa = f'INSERT INTO tarefa (descricao, data, materia) VALUES ("{descricao}", {data}, "{materia}")'
        cursor.execute(comando_add_tarefa)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao inserir tarefa.'
        return msg_erro

def add_compromomisso(nome, data, descricao):
    try:
        comando_add_compromisso = f'INSERT INTO compromisso (nome, data, descricao ) VALUES ("{nome}", {data},"{descricao}")'
        cursor.execute(comando_add_compromisso)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao inserir compromisso.'
        return msg_erro

def add_anotacao(data, nome, anotacao):
    try:
        comando_add_anotacao = f'INSERT INTO anotacao (data ,nome , anotacao) VALUES ({data}, "{nome}", "{anotacao}")'
        cursor.execute(comando_add_anotacao)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao inserir anotação.'
        return msg_erro

def add_aula(aula, horario_inicial, horario_final, materia, dia_da_semana, sala):
    try:
        comando = f'INSERT INTO aula (aula, horario_inicial, horario_final, materia, dia_da_semana, sala) VALUES {aula},{horario_inicial}, {horario_final}, "{materia}", "{dia_da_semana}", {sala}'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao inserir aula.'
        return msg_erro

def read_bd(atributo, tabela):
    comando = f'SELECT {atributo} FROM {tabela}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def read_parametro_txt(atributo,tabela, condicao, parametro):
    try:
        conexao.cursor()
        comando = f'SELECT {atributo} FROM {tabela} WHERE "{condicao}" = "{parametro}"'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        if resultado is not None:
            return resultado
        else:
            msg_erro = '❌ Nada selecionado!'
            return msg_erro
    except:
        msg_erro = '❌ Erro ao selecionar a linha da tabela.'
        return msg_erro

def read_parametro_int(atributo,tabela, condicao, parametro):
    try:
        conexao.cursor()
        comando = f'SELECT {atributo} FROM {tabela} WHERE {condicao} = {parametro}'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        if resultado is not None:
            return resultado
        else:
            msg_erro = '❌ Nada selecionado!'
            return msg_erro
    except:
        msg_erro = '❌ Erro ao selecionar a linha da tabela aula.'
        return msg_erro

def delete_bd(tabela):
    try:
        comando = f'DELETE FROM {tabela}'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao apagar tabela.'
        return msg_erro

def delete_parametro_txt(tabela, condicao, parametro):
    try:
        comando = f'DELETE FROM {tabela} WHERE "{condicao}" = "{parametro}"'
        cursor.execute(comando) 
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao apagar tabela.'
        return msg_erro

def delete_parametro_int(tabela, condicao, parametro):
    try:
        comando = f'DELETE FROM {tabela} WHERE {condicao} = {parametro}'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao apagar a tabela.'
        return msg_erro
      
def update_txt(tabela, novo_valor, condicao, parametro):
    try:
        comando = f'UPDATE {tabela} SET valor = "{novo_valor}" WHERE "{condicao}" = "{parametro}"'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao atualizar a tabela.'
        return msg_erro

def update_int(tabela, novo_valor, condicao, parametro):
    try:
        comando = f'UPDATE {tabela} SET valor = {novo_valor} WHERE {condicao} = {parametro}'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = '❌ Erro ao atualizar a tabela.'
        return msg_erro
