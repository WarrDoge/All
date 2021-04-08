import requests
import json
import schedule
import time
import os
import sys
import asyncio
from telethon import TelegramClient, events, utils, Button, functions, types
from telethon.tl.functions.messages import SendMessageRequest, GetBotCallbackAnswerRequest
#################################################
headers = {
    'accept': 'application/json',
    'authorization': key,
}
params = (
    ('active', '1'),
)
response = requests.get('https://domain/api/app/list', headers=headers, params=params)
active = json.loads(response.text)
active = active.get('items')
active_list = list()
for i in active:
	active_list.append(i.get('name'))
#################################################
def job():
	headers = {
    'accept': 'application/json',
    'authorization': key,
	}
	params = (
	    ('active', '1'),
	)
	response = requests.get('https://domain/api/app/list', headers=headers, params=params)
	check = json.loads(response.text)
	check = check.get('items')

	check_list = list()
	for i in check:
		check_list.append(i.get('name'))
	if len(check_list) > len(active_list):
		newapp = check_list - active_list
		active_list.append(newapp[0])
		appname = str(newapp[0]) + ' (Gambling)'
		requests.post('https://api.telegram.org/bot1329396156:botkey/sendMessage?chat_id=-chat&text=Добавляю органику на '+str(newapp[0])+'!')
#################################################		
		api_id = 2533090
		api_hash = '8e5e945e7c34ba5011b8fbc4d4b80dd4'
		phone = '+380500565329'
		client = TelegramClient('skakbot2', api_id, api_hash)
		skak = '@SkakAppUClient_bot'
		with client:
#################################################			
			async def cleaner(skak):
				await asyncio.sleep(0.2)
				while True:			
					await asyncio.sleep(0.5)	
					messages = await client.get_messages(skak, limit=1)
					txt = str(messages)						
					if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
						await client.delete_messages(skak, messages[0])	
			#################################################
			async def start():		
				await client(SendMessageRequest(skak, '📱 Приложения'))
			#################################################	
			async def click_active(skak):
				await asyncio.sleep(0.2)		
				while True:
					await asyncio.sleep(0.4)	
					messages = await client.get_messages(skak, limit=1)
					await messages[0].click(text='Активные')
			#################################################
			async def click_app(skak):
				await asyncio.sleep(0.3)		
				while True:
					await asyncio.sleep(0.4)	
					messages = await client.get_messages(skak, limit=1)
					await messages[0].click(text=appname)
			#################################################		
			async def click_geo(skak):
				await asyncio.sleep(0.4)			
				while True:
					await asyncio.sleep(0.4)	
					messages = await client.get_messages(skak, limit=1)
					await messages[0].click(text='Страны / Органика')
			#################################################		
			async def click_geo_add(skak):
				await asyncio.sleep(0.5)			
				while True:
					await asyncio.sleep(0.4)	
					messages = await client.get_messages(skak, limit=1)
					await messages[0].click(text='Подключить органику')
			#################################################
			async def message_geo(skak):
				await asyncio.sleep(0.6)			
				while True:
					await asyncio.sleep(0.4)	
					messages = await client.get_messages(skak, limit=3)
					txt = str(messages)
					if 'Занятые страны:' in txt:
						await client(SendMessageRequest(skak, 'SK, CH, KR, IT, PT, SI, EE, BE'))
						break
			#################################################			
			async def click_add(skak):
				await asyncio.sleep(0.7)	
				while True:
					await asyncio.sleep(0.4)	
					messages = await client.get_messages(skak, limit=1)	
					await messages[0].click(text='Подключить')
			#################################################
			loop = asyncio.get_event_loop()	
			loop.create_task(start())	
			loop.create_task(cleaner(skak))
			###################################	
			loop.create_task(click_active(skak))
			###################################		
			loop.create_task(click_app(skak))
			###################################		
			loop.create_task(click_geo(skak))
			###################################			
			loop.create_task(click_geo_add(skak))
			###################################	
			loop.create_task(message_geo(skak))
			###################################	
			loop.create_task(click_add(skak))
			###################################	
			loop.run_until_complete(asyncio.sleep(20))
###################################################################
def restart():
	os.execv(sys.executable, ['python3'] + sys.argv)
###################################################################
def check():
	requests.post('https://api.telegram.org/bot1329396156:botkey/sendMessage?chat_id=-chat&text=Готовлюсь добавлять органику...')
###################################################################
check()
schedule.every(3).seconds.do(job)
schedule.every(10).minutes.do(restart)
schedule.every(20).minutes.do(check)
while True:
    schedule.run_pending()
    time.sleep(1)			