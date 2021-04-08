import asyncio
from telethon import TelegramClient, events, utils, Button, functions, types
from telethon.tl.functions.messages import SendMessageRequest, GetBotCallbackAnswerRequest
import requests
import json
import schedule
import time
###################################################################
blacklist = list()
step = 0
step_bufer = 0
in_work = 'No'
###################################################################
headers = {
    'accept': 'application/json',
    'authorization': key,
}
response = requests.get('https://uclient.skakapp.com/api/app/list-available', headers=headers)
old = json.loads(response.text)
old = old.get('items')
for i in old:
	if str(i['category']) == str('GAMBLING'):
		blacklist.append(i['name'])	
###################################################################	
def job():
	global in_work
	if in_work == 'No':
	###################################################################
		headers = {
		    'accept': 'application/json',
		    'authorization': key,
		}
		params = (
		    ('active', '0'),
		)
		response = requests.get('https://uclient.skakapp.com/api/app/list', headers=headers, params=params)
		deleted = json.loads(response.text)
		deleted = deleted.get('items')
	###################################################################
		headers = {
		    'accept': 'application/json',
		    'authorization': key,
		}
		params = (
		    ('active', '1'),
		)
		response = requests.get('https://uclient.skakapp.com/api/app/list', headers=headers, params=params)
		active = json.loads(response.text)
		active = active.get('items')
	###################################################################
		headers = {
		    'accept': 'application/json',
		    'authorization': key,
		}
		response = requests.get('https://uclient.skakapp.com/api/app/list-available', headers=headers)
		appdata = json.loads(response.text)
		appdata = appdata.get('items')
		i = 0
		while i <= len(appdata) - 1:
			if 'GAMBLING' in appdata[i].get('category'):
				if appdata[i].get('name') not in str(deleted) and appdata[i].get('name') not in str(active) and appdata[i].get('name') not in str(blacklist):
					in_work = 'Yes'
					requests.post('https://api.telegram.org/bot1329396156:botkey/sendMessage?chat_id=-chat&text=Добавляю приложение '+appdata[i].get('name')+'!')
	###################################################################
					appname = appdata[i].get('name') + ' (Gambling)'
					api_id = 3488601
					api_hash = '5092026fe08f85528de7912b847d5a73'
					phone = '+380962931648'
					client = TelegramClient('Perm', api_id, api_hash)
					skak = ''
					with client:
	###################################################################	
						###################################################################
						async def step1():
							await client(SendMessageRequest(nickname, '📱 Приложения'))
							global step
							step += 1
							print('1')	
					############################		
						async def step2():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass
							try:
								await asyncio.wait_for(messages[0].click(text='Доступные'), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if 'Crypto' in str(messages):
									step += 1
									print('2')
								else:
									step_bufer -= 1
							except:	
								messages = await client.get_messages(nickname, limit=1)
								if 'Crypto' in str(messages):
									step += 1
									print('2')	
								else:
									step_bufer -= 1
					############################				
						async def step3():
							global step
							global step_bufer		
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass
							try:
								await asyncio.wait_for(messages[0].click(1), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if appname in str(messages):
									step += 1
									print('3')
								else:
									step_bufer -= 1
							except:
								messages = await client.get_messages(nickname, limit=1)
								if appname in str(messages):
									step += 1
									print('3')
								else:
									step_bufer -= 1		
					############################				
						async def step4():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass
							try:
								await asyncio.wait_for(messages[0].click(text=appname), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if 'Подключить' in str(messages):
									step += 1
									print('4')
								else:
									step_bufer -= 1				
							except:
								messages = await client.get_messages(nickname, limit=1)
								if 'Подключить' in str(messages):
									step += 1
									print('4')
								else:
									step_bufer -= 1						
					############################				
						async def step5():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass
							try:		
								await asyncio.wait_for(messages[0].click(text='Подключить'), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if 'Install' in str(messages):
									step += 1
									print('5')
								else:
									step_bufer -= 1	
							except:
								messages = await client.get_messages(nickname, limit=1)
								if 'Install' in str(messages):
									step += 1
									print('5')
								else:
									step_bufer -= 1						
					############################				
						async def step6():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass	
							try:				
								await asyncio.wait_for(messages[0].click(text='Install'), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if 'Да' in str(messages):
									step += 1
									print('6')	
								else:
									step_bufer -= 1	
							except:
								messages = await client.get_messages(nickname, limit=1)
								if 'Да' in str(messages):
									step += 1
									print('6')	
								else:
									step_bufer -= 1						
					############################				
						async def step7():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass
							try:		
								await asyncio.wait_for(messages[0].click(text='Да'), 0.4)
								messages = await client.get_messages(nickname, limit=5)
								if 'Подключено приложение' in str(messages):
									step += 1
									print('7')
								else:
									step_bufer -= 1	
							except:
								messages = await client.get_messages(nickname, limit=5)
								if 'Подключено приложение' in str(messages):
									step += 1
									print('7')
								else:
									step_bufer -= 1							
					############################				
						async def step8():
							global step
							await client(SendMessageRequest(nickname, '📱 Приложения'))
							step += 1
							print('8')							
					############################				
						async def step9():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass
							try:		
								await asyncio.wait_for(messages[0].click(text='Активные'), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if appname in str(messages):
									step += 1
									print('9')
								else:
									step_bufer -= 1		
							except:
								messages = await client.get_messages(nickname, limit=1)
								if appname in str(messages):
									step += 1
									print('9')
								else:
									step_bufer -= 1		
					############################				
						async def step10():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:	
									pass	
							try:
								await asyncio.wait_for(messages[0].click(text=appname), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if 'Страны / Органика' in str(messages):
									step += 1
									print('10')
								else:
									step_bufer -= 1		
							except:
								messages = await client.get_messages(nickname, limit=1)
								if 'Страны / Органика' in str(messages):
									step += 1
									print('10')
								else:
									step_bufer -= 1				
					############################				
						async def step11():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass	
							try:			
								await asyncio.wait_for(messages[0].click(text='Страны / Органика'), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if 'Подключить органику' in str(messages):
									step += 1
									print('11')
								else:
									step_bufer -= 1	
							except:
								messages = await client.get_messages(nickname, limit=1)
								if 'Подключить органику' in str(messages):
									step += 1
									print('11')
								else:
									step_bufer -= 1									
					############################				
						async def step12():
							global step
							global step_bufer
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass
							try:			
								await asyncio.wait_for(messages[0].click(text='Подключить органику'), 0.4)
								messages = await client.get_messages(nickname, limit=1)
								if 'Занятые страны' in str(messages):
									step += 1
									print('12')	
								else:
									step_bufer -= 1	
							except:
								messages = await client.get_messages(nickname, limit=1)
								if 'Занятые страны' in str(messages):
									step += 1
									print('12')	
								else:
									step_bufer -= 1					
					############################				
						async def step13():
							global step
							await client(SendMessageRequest(nickname, 'SK, CH, KR, IT, PT, SI, EE, BE'))
							step += 1
							print('13')						
					############################				
						async def step14():
							global step_bufer
							global in_work
							messages = await client.get_messages(nickname, limit=1)
							txt = str(messages)
							if 'Приложение уже подключено' in txt or '* Подходит для FB, TT, Unity, In-app, Google ADS 👉 можно лить по' in txt or 'Для приложения' in txt or 'получен первый инсталл' in txt or 'Ни одна страна не выбрана' in txt or 'Подключение стран к приложению отменено' in txt:
								try:
									await asyncio.wait_for(client.delete_messages(nickname, messages[0]), 0.4)
								except:
									pass	
							try:	
								await asyncio.wait_for(messages[0].click(text='Подключить'), 0.4)
								messages = await client.get_messages(nickname, limit=2)
								if 'подключены к приложению' in str(messages):
									print('14')
									in_work = 'No'
								else:
									step_bufer -= 1	
							except:
								messages = await client.get_messages(nickname, limit=2)
								if 'подключены к приложению' in str(messages):
									print('14')
									in_work = 'No'
								else:
									step_bufer -= 1							
						###################################################################	
						loop = asyncio.get_event_loop()
						loop.run_until_complete(step1())
						def job():
							global step
							global step_bufer
							while True:
								time.sleep(0.4)
								if step != step_bufer:
									step_bufer += 1	
									if step == 1:
										loop.run_until_complete(step2())
									elif step == 2:
										loop.run_until_complete(step3())
									elif step == 3:
										loop.run_until_complete(step4())
									elif step == 4:
										loop.run_until_complete(step5())
									elif step == 5:
										loop.run_until_complete(step6())
									elif step == 6:
										loop.run_until_complete(step7())
									elif step == 7:
										loop.run_until_complete(step8())
									elif step == 8:
										loop.run_until_complete(step9())
									elif step == 9:
										loop.run_until_complete(step10())	
									elif step == 10:
										loop.run_until_complete(step11())		
									elif step == 11:
										loop.run_until_complete(step12())
									elif step == 12:
										loop.run_until_complete(step13())	
									elif step == 13:
										loop.run_until_complete(step14())
						job()
					###################################################################
	###################################################################	
				else:
					print('Checking...')
				i = i + 1
			else:
				i = i + 1	
	else:
		pass
###################################################################
def check():
	requests.post('https://api.telegram.org/bot1329396156:botkey/sendMessage?chat_id=-chat&text=Готовлюсь добавлять Скаков...')
###################################################################
check()
schedule.every(1).seconds.do(job)
schedule.every(10).minutes.do(check)
while True:
    schedule.run_pending()
    time.sleep(1)