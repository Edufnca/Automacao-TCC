import mysql.connector
from Dicionario import *

conexao = mysql.connector.connect(
    host='containers-us-west-209.railway.app',
    user='root',
    password='3qe4hYKN5vC9qQg1jA92',
    port='5686',
    database='railway',
    charset='utf8mb4'
)
cursor = conexao.cursor()

# TABELAS: anotacao, aula, compromisso, prova, tarefa

def add_prova(codigo, assunto, materia, data, dia_da_semana):
    if dia_da_semana in dia_semana:
        try:
            comando_add_prova = f"INSERT INTO prova (codigo, assunto, materia, data, dia_da_semana ) VALUES ({codigo}, '{assunto}', '{materia}', {data}, '{dia_da_semana}')"
            cursor.execute(comando_add_prova)
            conexao.commit()
            cursor.close()
            conexao.close()
            return "Prova salva com sucesso!!"
        except:
            msg_erro = 'Erro ao inserir prova'
            return msg_erro
    else: return "digite um dia da semana: Segunda, Terça, Quarta, Quinta, Sexta, Sabado, Domingo"

def add_tarefa(codigo, descricao, data_inicial,data_final , materia):
    try:
        comando_add_tarefa = f'INSERT INTO tarefa (codigo, descricao, data, materia) VALUES ("{codigo}, "{descricao}", {data_inicial}, {data_final}, "{materia}")'
        cursor.execute(comando_add_tarefa)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'Erro ao inserir tarefa'
        return msg_erro

def add_compromomisso(id, nome, data, descricao):
    try:
        comando_add_compromisso = f'INSERT INTO compromisso (id, nome, data, descricao ) VALUES ("{id}","{nome}", {data},"{descricao}")'
        cursor.execute(comando_add_compromisso)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'Erro ao inserir compromisso'
        return msg_erro

def add_anotacao(data, nome, anotacao):
    try:
        comando_add_anotacao = f'INSERT INTO anotacao (data ,nome , anotacao) VALUES ({data}, "{nome}", "{anotacao}")'
        cursor.execute(comando_add_anotacao)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'Erro ao inserir anotação'
        return msg_erro

def add_aula(id, aula, horario_inicial, horario_final, materia, dia_da_semana, sala):
    try:
        comando = f"INSERT INTO aula (id, aula, horario_inicial, horario_final, materia, dia_da_semana, sala) VALUES {id}, '{aula}',{horario_inicial}, {horario_final}, '{materia}', '{dia_da_semana}', {sala} "
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'Erro ao inserir aula'
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
            msg_erro = 'nada selecionado'
            return msg_erro
    except:
        msg_erro = 'erro ao selecionar a linha da tabela'
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
            msg_erro = 'nada selecionado'
            return msg_erro
    except:
        msg_erro = 'erro ao selecionar a linha da tabela aula'
        return msg_erro

def delete_bd(tabela):
    try:
        comando = f'DELETE FROM {tabela}'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'erro ao apagar tabela'
        return msg_erro

def delete_parametro_txt(tabela, condicao, parametro):
    try:
        comando = f'DELETE FROM {tabela} WHERE "{condicao}" = "{parametro}"'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'erro ao apagar tabela'
        return msg_erro

def delete_parametro_int(tabela, condicao, parametro):
    try:
        comando = f'DELETE FROM {tabela} WHERE {condicao} = {parametro}'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'erro ao apagar a tabela'
        return msg_erro
      
def update_txt(tabela, novo_valor, condicao, parametro):
    try:
        comando = f'UPDATE {tabela} SET valor = "{novo_valor}" WHERE "{condicao}" = "{parametro}"'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'erro ao atualizar a tabela'
        return msg_erro

def update_int(tabela, novo_valor, condicao, parametro):
    try:
        comando = f'UPDATE {tabela} SET valor = {novo_valor} WHERE {condicao} = {parametro}'
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        conexao.close()
    except:
        msg_erro = 'erro ao atualizar a tabela'
        return msg_erro
