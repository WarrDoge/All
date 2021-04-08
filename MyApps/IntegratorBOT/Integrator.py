import requests
import json
from NewApp import *
#############################################
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
	'Content-Type': 'application/json',
}
data = '{"campaign_id":'+str(ringid)+',"type":"forced","name":"'+AppName+'","position":"1","action_options":null,"comments":null,"state":"active","schema":"action","action_type":"campaign","action_payload":"'+str(compid)+'","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_2","mode":"accept","payload":["'+str(subid2)+'"]}],"triggers":null,"landings":[],"offers":[]}'
response = requests.post('https://domain/admin_api/v1/streams', headers=headers, data=data)
############################################################################################
def job(response, subid2, AppName, form):
#################
	stream_list = list()
	for i in r:
		if 'sub_id_2' in str(i) and 'sub_id_3' in str(i):
############################################################################################			
			if i['filters'][0]['payload'][0][3:6] == str(int(subid2[3:6]) - 1):
				del i['id']
				for n in i['offers']:
					del n['id']
					del n['stream_id']
				offers = i['offers']
				for n in i['filters']:
					del n['id']
					del n['stream_id']				
				i['filters'][0]['payload'][0] = subid2
				i['filters'][1]['payload'][0] = i['filters'][1]['payload'][0].replace('_', form).replace('/', form).replace('-', form)
				name = i['name']
				name  = name.split('/')
				name[-1] = str(subid2[0:6].upper()) + '|' + str(AppName)
				name = str(name).replace(' ', '').replace('[', '').replace(']', '').replace("'", '').replace(',', ' / ').replace('|', ' ')
				i['name'] = name
				i.update(offers = offers)
				result = json.dumps(i)							
				if str(name).replace(' ', '') not in str(stream_list).replace(' ', ''):				
#############################################
					headers = {
						'accept': 'application/json',
						'Api-Key': 'key',
						'Content-Type': 'application/json',
					}
					data = result
					response = requests.post('https://domain/admin_api/v1/streams', headers=headers, data=data)
					stream_list.append(str(name.replace(' ', '')))	
					print(i['name'])								
############################################################################################			
			if i['filters'][1]['payload'][0][3:6] == str(int(subid2[3:6]) - 1):
				del i['id']
				for n in i['offers']:
					del n['id']
					del n['stream_id']		
				offers = i['offers']
				for n in i['filters']:
					del n['id']		
					del n['stream_id']								
				i['filters'][1]['payload'][0] = subid2
				i['filters'][0]['payload'][0] = i['filters'][0]['payload'][0].replace('_', form).replace('/', form).replace('-', form)
				name = i['name']
				name  = name.split('/')
				name[-1] = str(subid2[0:6].upper()) + '|' + str(AppName)
				name = str(name).replace(' ', '').replace('[', '').replace(']', '').replace("'", '').replace(',', ' / ').replace('|', ' ')
				i['name'] = name
				i.update(offers = offers)
				result = json.dumps(i)	
				if str(name).replace(' ', '') not in str(stream_list).replace(' ', ''):				
#############################################
					headers = {
						'accept': 'application/json',
						'Api-Key': 'key',
						'Content-Type': 'application/json',
					}
					data = result
					response = requests.post('https://domain/admin_api/v1/streams', headers=headers, data=data)
					stream_list.append(str(name.replace(' ', '')))	
					print(i['name'])
#######################################################################################################
print('Starting Sydney...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/309/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Tenerife...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/278/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Lemon...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/200/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Dubai...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/151/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Moskow...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/146/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting SecretVictory...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/32/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Graf...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/31/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Dem...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/24/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Anelin...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/20/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Starting Iceman...')
########
headers = {
	'accept': 'application/json',
	'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/13/streams', headers=headers)
r = json.loads(response.text)
########
job(r, subid2, AppName, form)
print('Done!')
#################
print('Finished!')