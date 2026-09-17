"""
TELEGRAM MESSAGE MIRROR BOT

Script de automação desenvolvido de forma independente por Pablo Phillipe Cândido dos Santos, destinado ao espelhamento assíncrono de mensagens e organização automática de tópicos de fórum entre canais/grupos do Telegram.

Automation script independently developed by Pablo Phillipe Cândido dos Santos, designed for asynchronous message mirroring and automatic forum topic organization between Telegram channels/groups.

O desenvolvimento contou com ferramentas de inteligência artificial generativa como recurso auxiliar.
The development included generative artificial intelligence tools as an auxiliary resource.

Currículo Lattes: http://lattes.cnpq.br/9500873674712528
"""

import asyncio
import random
import logging
import os
import json
from telethon import TelegramClient, events, functions

# Configuração do painel de controle (Log)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# 1. Suas Credenciais e Canais
API_ID = 12345678  # Substitua pelo seu ID numérico
API_HASH = 'seu_api_hash_aqui'  # Substitua pelo seu Hash entre aspas
CANAL_ORIGEM = 'origem' 
CANAL_DESTINO = 'destino'

# 2. Configuração dos arquivos de memória
ARQUIVO_MEMORIA = 'ultimo_id.txt'
ARQUIVO_MAPA = 'mapa_topicos.json'
client = TelegramClient('sessao_local', API_ID, API_HASH)
fila_mensagens = asyncio.Queue()

# --- FUNÇÕES DE MEMÓRIA ---
def carregar_ultimo_id():
    if os.path.exists(ARQUIVO_MEMORIA):
        with open(ARQUIVO_MEMORIA, 'r') as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo.isdigit():
                return int(conteudo)
    return 0

def salvar_ultimo_id(mensagem_id):
    with open(ARQUIVO_MEMORIA, 'w') as arquivo:
        arquivo.write(str(mensagem_id))

def carregar_mapa():
    if os.path.exists(ARQUIVO_MAPA):
        with open(ARQUIVO_MAPA, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_mapa(mapa):
    with open(ARQUIVO_MAPA, 'w', encoding='utf-8') as f:
        json.dump(mapa, f, ensure_ascii=False, indent=4)

mapa_topicos = carregar_mapa()

async def obter_titulo_topico(topic_id):
    try:
        msg = await client.get_messages(CANAL_ORIGEM, ids=topic_id)
        if msg and msg.action and hasattr(msg.action, 'title'):
            return msg.action.title
    except Exception as e:
        logging.warning(f"Não foi possível ler o nome do tópico {topic_id}.")
    return f"Subgrupo {topic_id}"

# --- MOTOR DE CÓPIA ---
async def processador_de_fila():
    while True:
        mensagem = await fila_mensagens.get()
        try:
            if mensagem.action:
                salvar_ultimo_id(mensagem.id)
                continue

            espera = random.randint(3, 7)
            await asyncio.sleep(espera)
            
            destino_reply_id = None
            
            if mensagem.reply_to and getattr(mensagem.reply_to, 'forum_topic', False):
                topic_id = getattr(mensagem.reply_to, 'reply_to_top_id', None) or getattr(mensagem.reply_to, 'reply_to_msg_id', None)
                
                if topic_id:
                    topic_id_str = str(topic_id)
                    
                    if topic_id_str not in mapa_topicos:
                        titulo = await obter_titulo_topico(topic_id)
                        logging.info(f"Criando novo subgrupo no destino: '{titulo}'...")
                        
                        try:
                            novo_topico = await client(functions.messages.CreateForumTopicRequest(
                                peer=CANAL_DESTINO,
                                title=titulo
                            ))
                            
                            for update in novo_topico.updates:
                                if hasattr(update, 'message') and hasattr(update.message, 'id'):
                                    mapa_topicos[topic_id_str] = update.message.id
                                    salvar_mapa(mapa_topicos)
                                    break
                        except Exception as e:
                            logging.error(f"Erro ao criar o subgrupo '{titulo}': {e}. Mensagem será enviada na aba Geral.")
                    
                    destino_reply_id = mapa_topicos.get(topic_id_str)
            
            await client.send_message(CANAL_DESTINO, mensagem, reply_to=destino_reply_id)
            salvar_ultimo_id(mensagem.id)
            
            logging.info(f"Sucesso: Mensagem ID {mensagem.id} copiada! (Pausa de {espera}s).")
            
        except Exception as e:
            logging.error(f"Erro ao encaminhar mensagem ID {mensagem.id}: {e}")
        finally:
            fila_mensagens.task_done()

@client.on(events.NewMessage(chats=CANAL_ORIGEM))
async def escutar_canal_tempo_real(event):
    logging.info("Nova mensagem detectada no canal (Tempo real)!")
    await fila_mensagens.put(event.message)

async def recuperar_mensagens_perdidas():
    ultimo_id = carregar_ultimo_id()
    
    if ultimo_id == 0:
        logging.info("Primeira execução: Iniciando a cópia de TODAS as mensagens do canal do zero...")
    else:
        logging.info(f"Retomando a cópia a partir do ID {ultimo_id}...")
        
    contador = 0
    async for mensagem in client.iter_messages(CANAL_ORIGEM, min_id=ultimo_id, reverse=True):
        await fila_mensagens.put(mensagem)
        contador += 1
        
    if contador > 0:
        logging.info(f"{contador} mensagem(ns) antiga(s) adicionada(s) à fila. Começando o espelhamento...")
    else:
        logging.info("O bot está em dia. Nenhuma mensagem pendente no histórico.")

async def main():
    await client.start()
    logging.info("Bot conectado com sucesso!")
    
    asyncio.create_task(processador_de_fila())
    await recuperar_mensagens_perdidas()
    
    if not fila_mensagens.empty():
        logging.info("Aguardando o envio de todo o histórico (isso pode demorar devido às pausas de segurança)...")
        await fila_mensagens.join() 
        logging.info("✅ ESPELHAMENTO CONCLUÍDO! O histórico inteiro foi copiado com sucesso.")
        logging.info("O bot agora está de plantão, aguardando novas mensagens em tempo real.")
        
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())