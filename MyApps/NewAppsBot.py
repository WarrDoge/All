import requests
import json
import schedule
import time
###################################################################
blacklist = list()
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
				requests.post('https://api.telegram.org/bot1329396156:botkey/sendMessage?chat_id=-chat&text='+appdata[i].get('name')+'! SkakApp добавил приложение!')
			else:
				print('Checking...')
			i = i + 1
		else:
			i = i + 1			
###################################################################
def check():
	requests.post('https://api.telegram.org/bot1329396156:botkey/sendMessage?chat_id=-chat&text=Чекаю Скаков...')
###################################################################
check()
schedule.every(2).seconds.do(job)
schedule.every(5).minutes.do(check)
while True:
    schedule.run_pending()
    time.sleep(1)