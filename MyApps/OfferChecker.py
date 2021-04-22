import requests
import json
##################################################
webs = ['Sydney', 'Tenerife', 'Lemon', 'Rome', 'Dubai', 'Lissabon', 'Moskow', 'Chicago', 'SecretVictory', 'Graf', 'Dem', 'First', 'Djora', 'Iceman', 'Key', 'Test', 'Main']
exlude = [5, 3, 9, 17]
old = [142, 144, 190, 191, 204, 205, 257]
error_list = list()
##################################################
print('Запрашиваю данные...\n')
headers = {
    'accept': 'application/json',
    'Api-Key': key,
}
response = requests.get('https://domain/admin_api/v1/offers', headers=headers)
offers_data = json.loads(response.text)
print('Данные получены!\n')
##################################################
print('Начинаю анализ данных...\n')
for i in offers_data:
	name = str(i['name']).replace('web', '').replace(' ', '').lower()
	link = str(i['action_payload']).replace(' ', '').lower()
	for n in webs:
		buffer_name = name.replace(n.lower(), '')
		final_name = name.replace(buffer_name, '')
		if final_name in str(webs).lower() and final_name != '':
			if final_name in link:
				pass
			elif str(i['affiliate_network_id']) in str(exlude):	
				pass
			elif str(i['id']) in str(old):	
				pass	
			else:
				error_list.append(i['name'] + ', id #' + str(i['id']) + ' (' + i['action_payload'] + ')')
print('Данные проанализированны!\n')			
##################################################
print('Готовлю отчёт об ошибках...')
for i in error_list:
	error = '\nВыглядит подозрительно...\n' + str(i)
	print(error)	