import requests
import json
#######################################################################################################
StreamName = "REWARD / HR / CPL / "
####################################################
subid3 = "*_*"
#######
webid = "278"
#######
offerid = "478"
#######
starting_num = 330
final_num = 500
#######################################################################################################
print('Starting!')
headers = {
    'accept': 'application/json',
    'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/'+str(webid)+'/streams', headers=headers)
#################
r = json.loads(response.text)
stream_list = list()
done_list = list()
for i in r:
	m = starting_num
	n = final_num
	while m <= n:
		if 'app'+str(m) in str(i):
			if 'app'+str(m) not in str(stream_list):
				stream_list.append(i)		
		m = m + 1			
#################
def job():
	for i in stream_list:
		if 'app' in str(i['filters'][0]['payload'][0]):
			#################		
			if '_' in str(i['filters'][1]['payload'][0]):
				form = '_'
			elif '-' in str(i['filters'][1]['payload'][0]):	
				form = '-'
			elif '/' in str(i['filters'][1]['payload'][0]):	
				form = '/'
			#################
			sub_id_3 = subid3.replace('_', form).replace('/', form).replace('-', form)
			name = StreamName + ' / ' + str(i['filters'][0]['payload'][0][0:6]).upper()
			#################	
			if str(name).replace(' ', '') not in str(done_list).replace(' ', ''):		
				headers = {
				    'accept': 'application/json',
				    'Api-Key': 'key',
				    'Content-Type': 'application/json',
				}
				data = '{"campaign_id":'+webid+',"type":"forced","name":"'+name+'","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_2","mode":"accept","payload":["'+i['filters'][0]['payload'][0]+'"]},{"id":0,"name":"sub_id_3","mode":"accept","payload":["'+sub_id_3+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid+',"share":100,"state":"active"}]}'
				response = requests.post('https://domain/admin_api/v1/streams', headers=headers, data=data)
				done_list.append(str(name.replace(' ', '')))	
				print(name)	
		#######################################################################################################			
		elif 'app' in str(i['filters'][1]['payload'][0]):
			#################		
			if '_' in str(i['filters'][0]['payload'][0]):
				form = '_'
			elif '-' in str(i['filters'][0]['payload'][0]):	
				form = '-'
			elif '/' in str(i['filters'][0]['payload'][0]):	
				form = '/'
			#################
			sub_id_3 = subid3.replace('_', form).replace('/', form).replace('-', form)
			name = StreamName + ' / ' + str(i['filters'][1]['payload'][0][0:6]).upper()
			#################
			if str(name).replace(' ', '') not in str(done_list).replace(' ', ''):		
				headers = {
				    'accept': 'application/json',
				    'Api-Key': 'key',
				    'Content-Type': 'application/json',
				}
				data = '{"campaign_id":'+webid+',"type":"forced","name":"'+name+'","position":"1","action_options":"","comments":null,"state":"active","action_type":"http","schema":"landings","collect_clicks":true,"filter_or":false,"filters":[{"id":0,"name":"sub_id_2","mode":"accept","payload":["'+i['filters'][1]['payload'][0]+'"]},{"id":0,"name":"sub_id_3","mode":"accept","payload":["'+sub_id_3+'"]}],"triggers":null,"landings":[],"offers":[{"offer_id":'+offerid+',"share":100,"state":"active"}]}'
				response = requests.post('https://domain/admin_api/v1/streams', headers=headers, data=data)	
				done_list.append(str(name.replace(' ', '')))		
				print(name)	
############################################################################################################################################################################################################## -> Main
a =  0
while a < len(stream_list):
	job()
	a = a + 1
print("Finished!")
#######################################################################################################
print('Starting test...')
headers = {
    'accept': 'application/json',
    'Api-Key': 'key',
}
response = requests.get('https://domain/admin_api/v1/campaigns/'+str(webid)+'/streams', headers=headers)
r = json.loads(response.text)
appnum = list()
for i in r:
	appnum.append(int(str(filter(str.isdigit, i['name']))))
while starting_num < max(appnum):
	if str(StreamName + ' / ' + 'APP' + str(starting_num)).replace(' ', '') in str(r).replace(' ', ''):
		pass
	else: 
		print(str(StreamName + ' / ' + 'APP' + str(starting_num)) + ' Не создан!')
	starting_num += 1
print('Done testing!')	