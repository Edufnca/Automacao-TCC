import discord
import re
from datetime import datetime, timedelta
from discord.ext import commands
from Elementos_químicos import *
from Cotações import *
from OpenWeather import *
from Banco_de_dados import *
from Dicionario_de_comandos import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix="/",
                      case_insensitive=True,
                      intents=intents)


@client.event
async def on_ready():
  print('Bot ligado S2')

@client.event
async def on_member_join(member, ctx):
  await ctx.send(f'Ola, {ctx.author}')

@client.event
async def on_reaction_add(reaction, user):
  print(reaction.emoji)
  if reaction.emoji == '💵':
    print('ricasso')

@client.command(help='O comando da informações sobre algum elemento químico.', aliases=ComandosElemento)
async def elemento(ctx, message:str):
  if message in Quimica[0]:
    Elemento = elemento_simbolo(message)
  else:
    Elemento = elemento_nome(message)
  title = Elemento['nome']
  massa_atomica = Elemento['massa_quantica']
  numero_atomico = Elemento['numero_atomico']
  simbolo = Elemento['simbolo']
  familia =  Elemento['familia']
  grupo =  Elemento['grupo']
  periodo =  Elemento['periodo']
  embed_provas = discord.Embed(title=f'{title}',
                               description='Descrição do elemento: ',
                               colour=discord.Colour.blue())
  embed_provas.set_author(name='👨‍🔬 Química ⚗️', icon_url='https://i.imgur.com/X1Zglh3.png')
  embed_provas.set_image(url='https://i.imgur.com/siwb8qk.gif'),
  embed_provas.add_field(name='Massa Atômica', value=f'{massa_atomica}', inline=True)
  embed_provas.add_field(name='Número Atômico', value=f'{numero_atomico}', inline=True)
  embed_provas.add_field(name='Simbolo', value=f'{simbolo}', inline=False)
  embed_provas.add_field(name='Grupo', value=f'{grupo}', inline=True)
  embed_provas.add_field(name='Periodo', value=f'{periodo}', inline=True)
  await ctx.send(embed=embed_provas)

@client.command()
async def elementos(ctx):
  tabela_periodica = list()
  for x in Quimica[0]:
    tabela_periodica.append(Quimica[0][x]['nome'])
  for y in tabela_periodica:
    await ctx.send(f'{y}') #APERFEIÇÕAR

@client.command(help='O comando calcula um expressão matemática', aliases=comandosCalcular)
async def calcular(ctx, *expression):
  expression = ''.join(expression)
  expression.replace('x', '*')
  resposta = eval(expression)
  await ctx.send('A resposta é: '+ str(resposta))

@client.command(help='O comando te devolve o valor do dolar atualizado', aliases=ComandCota)
async def dolar(ctx):
  title = QDolar_name
  cotacao = QDolar_bid
  embed_cotacao = discord.Embed(title=f'{title}  💵',
                               description='',
                               colour=discord.Colour.yellow())
  embed_cotacao.add_field(name=f'{cotacao}', value='', inline=False)
  await ctx.send(embed=embed_cotacao)

@client.command()
async def ola(ctx):
  name = ctx.author.name
  await message.channel.send(f'Ola, {name}')

@client.command()
async def Htempe(ctx):
  await ctx.send(mensagem_temperatura()) #ERRO

@client.command(help='O comando te devolve a temperatua atual', aliases=ComandClima)
async def temperatura(ctx):
  embed = discord.Embed(title='🌡️ Agora está fazendo: ' + ' '+str(TempC) +'º',
                               description='',
                               colour= 0x0000FF)
  embed.set_author(name='Temperatura', icon_url='https://i.imgur.com/yq8CEq9.png')
  embed.add_field(name='', value=f'{mensagem_temperatura()}')
  embed.set_footer(text=f"{cidade}")
  await ctx.send(embed=embed)

@client.command()
async def addprova(ctx):
  perguntas = ["📝 Digite um código para a prova: ",
    "📝 Digite o assunto da prova: ",
    "📝 Digite a matéria da prova: ",
    "📅 Digite a data da prova: ",
    "📅 Digite o dia da semana da prova: "]
  
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
      await ctx.send(f"{pergunta} {resposta}")
  codigo = respostas[0]
  assunto = respostas[1]
  materia = respostas[2]
  data = respostas[3]
  dia_da_semana = respostas[4]
  data = data.replace("/", '-')
  data = '2023-'+data
  data = str(data)
  await ctx.send(add_prova(codigo, assunto, materia, data, dia_da_semana))

@client.command()
async def addtarefa(ctx):
  perguntas = ["Digite o código:",
              "Digite a descrição: ",
              "Digite a data inicial: ",
              "digite a data final: ",
              "digite a materia"]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
      await ctx.send(f"{pergunta} {resposta}")
  codigo = resposta[0]
  descricao = [1]
  data_inicial = [2]
  data_final = [3]
  materia = [4]
  await ctx.send(add_tarefa(codigo, descricao, data_inicial,data_final , materia))

@client.command()
async def addcompromisso(ctx):
  perguntas = ["digite o id:",
              "digite o nome",
              "digite a data",
              "digite a descrição"]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
      await ctx.send(f"{pergunta} {resposta}")
  id = respostas[0]
  nome = respostas[1]
  data = respostas[2]
  descricao = respostas[3]
  await ctx.send(add_compromomisso(id, nome, data, descricao))

@client.command()
async def addanotacao(ctx):
  perguntas = ["digite a data:",
              "digite o nome:",
              "digite a anotação:"]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
      await ctx.send(f"{pergunta} {resposta}")
  data = respostas[0]
  nome = respostas[1]
  anotacao = respostas[2]
  await ctx.send(add_anotacao(data, nome, anotacao))

@client.command()
async def addaula(ctx):
  perguntas = ["digite o id:",
              "Digite a aula:",
              "Digite o horário inicial",
              "Digite o horário final",
              "Digite a matéria:",
              "Digite o dia da semana:",
              "digite a sala:"]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
      await ctx.send(f"{pergunta} {resposta}")
  id = resposta[0]
  aula = resposta[1]
  horario_inicial = resposta[2]
  horario_final = resposta[3]
  materia = resposta[4]
  dia_da_semana = resposta[5]
  sala = resposta[6]
  await ctx.send(add_aula(id, aula, horario_inicial, horario_final, materia, dia_da_semana, sala))

@client.command()
async def verprovas(ctx):
  embed = discord.Embed(title='📌 Provas 📖',
                               description='',
                               colour= 0x0000FF)
  provas = read_bd("materia", "prova")
  descricao = read_bd("data", "prova")
  for item, descricao in zip(provas, descricao):
    item = re.sub(r"[[]'()]", '')
    embed.add_field(name=item, value=descricao, inline=False)
  await ctx.send(embed=embed)

@client.command()
async def vercompromissos(ctx):
  embed = discord.Embed(title='compromissos',
                               description='',
                               colour= 0x0000FF)
  compromissos = read_bd("nome, data", "compromisso")
  descricao = read_bd("descricao", "compromisso")
  compromissos = str(compromissos)
  for item, descricao in zip(compromissos, descricao):
    item = re.sub(r"[[]'()]", ' ')
    embed.add_field(name=item, value=descricao, inline=False)
  await ctx.send(embed=embed)

@client.command()
async def vertarefas(ctx):
  embed = discord.Embed(title='tarefas',
                               description='',
                               colour= 0x0000FF)
  tarefas = read_bd("data_inicial,data_final , materia", "tarefa")
  descricao = read_bd("descricao", "tarefa")
  for item, descricao in zip(tarefas, descricao):
    item = str(item)
    tarefas = re.sub(r"[[]'()]", '')
    embed.add_field(name=item, value=descricao, inline=False)
  await ctx.send(embed=embed)

@client.command()
async def veranotacao(ctx):
  embed = discord.Embed(title='anotações',
                               description='',
                               colour= 0x0000FF)
  anotacao = read_bd("data, nome", "anotacao")
  descricao = read_bd("anotacao", "anotacao")
  for item, descricao in zip(anotacao, descricao):
    item = str(item)
    item = re.sub(r"[[]'()]", '')
    embed.add_field(name=item, value=descricao, inline=False)
  await ctx.send(embed=embed)

@client.command()
async def veraulas(ctx):
  embed = discord.Embed(title='Aulas',
                               description='',
                               colour= 0x0000FF)
  dia = read_bd("dia_da_semana", "aula")
  materia = read_bd("materia", "aula")
  horario = read_bd("horario_inicial, horario_final", "aula")
  descricao = read_bd("aula", "aula")
  for dia, materia, horario, aula in zip(dia, materia, horario, descricao):
    materia = str(item)
    materia = re.sub(r"[[]'()]", '')
    aula = str(aula)
    aula = aula + 'º'
    embed_provas.set_author(name=dia)
    embed.add_field(name=materia, value=horario, inline=False)
    embed.add_field(name='', value=aula, inline=False)
  await ctx.send(embed=embed)

@client.command(help='lista todos os comandos')
async def comandos(ctx):
  command_names = [command.name for command in client.commands]
  lista_comandos = "\n".join(command_names)
  embed = discord.Embed(title="Lista de Comandos", description=lista_comandos, color=discord.Color.green())
  await ctx.send(embed=embed)
  
@client.command()
async def deletarprova(ctx):
  embed = discord.Embed(title='Provas',
                               description='',
                               colour= 0x0000FF)
  await ctx.send(embed=embed)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('ola'):
    await message.channel.send('Olá! 🥰')
  await client.process_commands(message)

@client.event
async def help(ctx):
  await ctx.send('--------Comandos---------')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando inválido.    Por favor digite um comando valido ou digite /help para ver os comandos")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Sem permissões concedidas. Por favor mude em *all* argumentos.")    
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Você não tem a permissão necessária.")
    elif isinstance(error, commands.CommandOnCooldown):
      msg = "Você esta em cooldown, por favor tente denovo em {:.2f}s".format(error.retry_after)
      await ctx.send(msg)

client.run(
  'MTEwMTUxNTEyOTc2NzYwMDE2OQ.GF9zQd.dsFsQhQTd5Uat1DjRG8ckBacuRuPmS4AoY8MrI')
