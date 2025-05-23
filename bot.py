import os
from telegram import Bot
from telegram.ext import CommandHandler, Updater

TOKEN = os.getenv("TOKEN")

def start(update, context):
    texto = """
**Análise de Escanteios - Hoje**
Jogo: Corinthians x São Paulo – 20h

- Média de escanteios FT: 11.2
- Over 10.5 cantos: 5 dos últimos 6 jogos
- Sugestão: Over 9.5 Cantos – Odd 1.80 (Betano)

Boa sorte nas apostas!
"""
    update.message.reply_text(texto)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("Bot rodando...")
    updater.idle()

if __name__ == '__main__':
    main()
