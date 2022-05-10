import telegram

chat_token = "1781877084:AAGF8vvjhGSv69oY_LT9CRUJwdpAVoW62jQ"
chat = telegram.Bot(token = chat_token)
updates = chat.getUpdates()

for u in updates:
    print(u.message)
    # print(u.message['bot']['test_bot'])
    # print(u.message['chat']['id'])