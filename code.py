from telethon import TelegramClient, events, sync
import time
def main():
	api_id = 15441983
	api_hash = '0d7c8810e52dd32051de312f5bbf3f9b' 
	client = TelegramClient('session_name', api_id, api_hash) 
	client.start()
	temp = ""
	chat = open("chats")
	m = open("message")
	for line in m:
		temp = temp + line
	for line in chat: 
		try:
			client.send_message(line, temp)
		except:
			print(f"Can not send message to {line}")
main()