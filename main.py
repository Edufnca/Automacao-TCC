import discord
import re
from Funcoes import *
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
  print('Bot ligado S2....')


@client.event
async def on_member_join(member, ctx):
  await ctx.send(f'Ola, {ctx.author}')


@client.event
async def on_reaction_add(reaction, user):
  print(reaction.emoji)
  if reaction.emoji == '💵':
    print('ricasso')


@client.command(help='O comando da informações sobre algum elemento químico.',
                aliases=ComandosElemento)
async def elemento(ctx, message: str):
  if message in Quimica[0]:
    Elemento = elemento_simbolo(message)
  else:
    Elemento = elemento_nome(message)
  title = Elemento['nome']
  massa_atomica = Elemento['massa_quantica']
  numero_atomico = Elemento['numero_atomico']
  simbolo = Elemento['simbolo']
  familia = Elemento['familia']
  grupo = Elemento['grupo']
  periodo = Elemento['periodo']
  embed_provas = discord.Embed(title=f'{title}',
                               description='Descrição do elemento: ',
                               colour=discord.Colour.blue())
  embed_provas.set_author(name='👨‍🔬 Química ⚗️',
                          icon_url='https://i.imgur.com/X1Zglh3.png')
  embed_provas.set_image(url='https://i.imgur.com/siwb8qk.gif'),
  embed_provas.add_field(name='Massa Atômica', value=f'{massa_atomica}')
  embed_provas.add_field(name='Número Atômico', value=f'{numero_atomico}')
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
    await ctx.send(f'{y}')  #APERFEIÇÕAR


@client.command(help='O comando calcula um expressão matemática',
                aliases=comandosCalcular)
async def calcular(ctx, *expression):
  expression = ''.join(expression)
  expression.replace('x', '*')
  resposta = eval(expression)
  await ctx.send('A resposta é: ' + str(resposta))


@client.command(help='O comando te devolve o valor do dolar atualizado',
                aliases=ComandCota)
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
  await ctx.send(mensagem_temperatura())  #ERRO


@client.command(help='O comando te devolve a temperatua atual',
                aliases=ComandClima)
async def temperatura(ctx):
  embed = discord.Embed(title='🌡️ Agora está fazendo: ' + ' ' + str(TempC) +
                        'º',
                        description='',
                        colour=0x0000FF)
  embed.set_author(name='Temperatura',
                   icon_url='https://i.imgur.com/yq8CEq9.png')
  embed.add_field(name=Tempo_descricao, value='', inline=False)
  embed.add_field(name=f'Máxima: {Tempo_max}º e Mínima: {Tempo_min}º',
                  value='',
                  inline=False)
  embed.add_field(name=f'Umidade: {Umidade}%', value='')
  embed.add_field(name=f'Nuvens: {Nuvens}%', value='')
  embed.add_field(name=f'Vento: {Vento}Km/H', value='')
  embed.add_field(name='', value=f'{mensagem_temperatura()}', inline=False)
  embed.set_footer(text=f'{cidade}   {Data}')
  await ctx.send(embed=embed)


@client.command()
async def addprova(ctx):
  perguntas = [
    "📝 Digite a aula da prova: ", "📝 Digite o assunto da prova: ",
    "📝 Digite a matéria da prova: ", "📅 Digite a data da prova: ",
    "📅 Digite o dia da semana da prova: "
  ]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for(
      'message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
    await ctx.send(f"{pergunta} {resposta}")
  aula = respostas[0]
  assunto = respostas[1]
  materia = respostas[2]
  data = respostas[3]
  dia_da_semana = respostas[4]
  data = data_transform(data)
  await ctx.send(add_prova(codigo, assunto, materia, data, dia_da_semana,
                           aula))


@client.command()
async def addtarefa(ctx):
  perguntas = [
    "Digite a descrição: ", "Digite a data inicial: ", "digite a data final: ",
    "digite a materia"
  ]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for(
      'message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
    await ctx.send(f"{pergunta} {resposta}")
  descricao = [0]
  data_inicial = [1]
  data_final = [2]
  materia = [3]
  data_inicial = data_transform(data_inicial)
  data_final = data_transform(data_final)
  await ctx.send(
    add_tarefa(codigo, descricao, data_inicial, data_final, materia))


@client.command()
async def addcompromisso(ctx):
  perguntas = ["digite o nome", "digite a data", "digite a descrição"]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for(
      'message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
    await ctx.send(f"{pergunta} {resposta}")
  nome = respostas[0]
  data = respostas[1]
  descricao = respostas[2]
  data = data_transform(data)
  await ctx.send(add_compromomisso(codigo, nome, data, descricao))


@client.command()
async def addanotacao(ctx):
  perguntas = ["digite a data:", "digite o nome:", "digite a anotação:"]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for(
      'message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
    await ctx.send(f"{pergunta} {resposta}")
  data = respostas[0]
  nome = respostas[1]
  anotacao = respostas[2]
  data = data_transform(data)
  await ctx.send(add_anotacao(codigo, data, nome, anotacao))


@client.command()
async def addaula(ctx):
  perguntas = [
    "Digite a aula:", "Digite o horário inicial", "Digite o horário final",
    "Digite a matéria:", "Digite o dia da semana:", "digite a sala:"
  ]
  respostas = []
  for pergunta in perguntas:
    await ctx.send(pergunta)
    resposta = await client.wait_for(
      'message', check=lambda message: message.author == ctx.author)
    respostas.append(resposta.content)
  await ctx.send("Obrigado! As informações coletadas foram:")
  for pergunta, resposta in zip(perguntas, respostas):
    await ctx.send(f"{pergunta} {resposta}")
  aula = resposta[0]
  horario_inicial = resposta[1]
  horario_final = resposta[2]
  materia = resposta[3]
  dia_da_semana = resposta[4]
  sala = resposta[5]
  horario_inicial = re.sub(r'h H', ':')
  horario_final = re.sub(r'h H', ':')
  await ctx.send(
    add_aula(codigo, aula, horario_inicial, horario_final, materia,
             dia_da_semana, sala))


@client.command()
async def verprovas(ctx):
  embed = discord.Embed(title='📌 Provas ', description='', colour=0x0000FF)
  provas = read_bd("materia", "prova")
  descricao = read_bd("data", "prova")
  for item, descricao in zip(provas, descricao):
    item = re.sub(r"[[]'()]", '')
    embed.add_field(name=item, value=descricao, inline=False)
  await ctx.send(embed=embed)


@client.command()
async def vercompromissos(ctx):
  embed = discord.Embed(title='📌 Compromissos',
                        description='',
                        colour=0x0000FF)
  compromissos = read_bd("nome, data", "compromisso")
  descricao = read_bd("descricao", "compromisso")
  compromissos = str(compromissos)
  for item, descricao in zip(compromissos, descricao):
    item = re.sub(r"[[]'()]", ' ')
    embed.add_field(name=item, value=descricao, inline=False)
  await ctx.send(embed=embed)


@client.command()
async def vertarefas(ctx):
  embed = discord.Embed(title='tarefas', description='', colour=0x0000FF)
  tarefas = read_bd("data_inicial,data_final , materia", "tarefa")
  descricao = read_bd("descricao", "tarefa")
  for item, descricao in zip(tarefas, descricao):
    item = str(item)
    tarefas = re.sub(r"[[]'()]", '')
    embed.add_field(name=item, value=descricao, inline=False)
  await ctx.send(embed=embed)


@client.command()
async def veranotacao(ctx):
  embed = discord.Embed(title='anotações', description='', colour=0x0000FF)
  anotacao = read_bd("data, nome", "anotacao")
  descricao = read_bd("anotacao", "anotacao")
  for item, descricao in zip(anotacao, descricao):
    item = str(item)
    item = re.sub(r"[[]'()]", '')
    embed.add_field(name=item, value=descricao, inline=False)
  await ctx.send(embed=embed)


@client.command()
async def veraulas(ctx):
  embed = discord.Embed(title='Aulas', description='', colour=0x0000FF)
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
  lista_comandos = "📝 Provas: \n addprova \n deletarprova \n verprovas \n\n📝 Aulas: \n addaula \n veraulas \n\n📝 Anotações: \n addanotacao \n veranotacao \n\n📝 Tarefas: \n addtarefa \n vertarefas \n\n📝 Compromissos: \n addcompromisso \n vercompromissos \n\n ⚗️ Química: \n elementos \n elemento \n\n 🔩 Outros: \n dolar \n htemp \n calcular \n temperatura"
  embed = discord.Embed(title="📌 Lista de Comandos",
                        description=lista_comandos,
                        color=discord.Color.purple())
  embed.add_field(name="📝 Provas",
                  value="\n addprova \n deletarprova \n verprovas",
                  inline=True)
  embed.add_field(name="📝 Aulas", value="\n addaula \n veraulas", inline=True)
  await ctx.send('\n📌 Digite "\help" + "comando" para saber mais informações!')
  await ctx.send(embed=embed)


@client.command()
async def deletarprova(ctx):
  embed = discord.Embed(title='Provas', description='', colour=0x0000FF)
  await ctx.send(embed=embed)


@client.command()
async def perfil(ctx):
  1 == 1


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
    author = ctx.author
    mention = author.mention
    await ctx.send(
      f"📢 Comando inválido! \n{mention}, por favor, digite um comando válido ou digite '/comandos' para ver os comandos."
    )
  elif isinstance(error, commands.MissingRequiredArgument):
    author = ctx.author
    mention = author.mention
    await ctx.send(
      f"📢 Sem permissões concedidas! \n {mention}, por favor, mude em *all* argumentos."
    )
  elif isinstance(error, commands.MissingPermissions):
    author = ctx.author
    mention = author.mention
    await ctx.send(f"📢 {mention}, você não tem a permissão necessária.")
  elif isinstance(error, commands.CommandOnCooldown):
    msg = "📢 você está em cooldown, por favor tente denovo em {:.2f}s".format(
      error.retry_after)
    await ctx.send(msg)


client.run(
  'MTEwMTUxNTEyOTc2NzYwMDE2OQ.GF9zQd.dsFsQhQTd5Uat1DjRG8ckBacuRuPmS4AoY8MrI')
