import telegram

chat_token = "HTTP API"
bot = telegram.Bot(token = '1781877084:AAGF8vvjhGSv69oY_LT9CRUJwdpAVoW62jQ')
text = 'hello'
bot.sendMessage(chat_id = "-565130259", text=text)