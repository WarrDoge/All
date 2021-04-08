import requests
import json
#################
webid = 278
Stream_Name = "REWARD / HR /"
#######
offer_id = 482
#######
starting_num = 1
final_num = 500
#################
print('Starting!')
headers = {
    'accept': 'application/json',
    'Api-Key': key,
}
response = requests.get('https://domian/admin_api/v1/campaigns/'+str(webid)+'/streams', headers=headers)
#################
r = json.loads(response.text)
stream_list = list()
for i in r:
	if str(Stream_Name).replace(' ', '') in str(i['name']).replace(' ', ''):
		m = starting_num
		n = final_num
		while m <= n:
			if 'app'+str(m) in str(i):
				stream_list.append(i['id'])		
			m = m + 1		
#################
for i in stream_list:
	headers = {
	    'accept': 'application/json',
	    'Api-Key': key,
	}
	response = requests.get('https://domian/admin_api/v1/streams/'+str(i)+'', headers=headers)
	r = json.loads(response.text)
	r.update(offers = [{'offer_id': offer_id, 'share': 100, 'state': 'active'}])
	name = r['name']
	r = json.dumps(r)
	#################
	headers = {
	    'accept': 'application/json',
	    'Api-Key': key,
	    'Content-Type': 'application/json',
	}
	#################
	data = r
	response = requests.put('https://domian/admin_api/v1/streams/'+str(i)+'', headers=headers, data=data)
################
	print(name)
print('Finished!')
################
print('Starting test...')
headers = {
    'accept': 'application/json',
    'Api-Key': key,
}
response = requests.get('https://domian/admin_api/v1/campaigns/'+str(webid)+'/streams', headers=headers)
r = json.loads(response.text)
stream_list = list()
for i in r:
	if str(Stream_Name).replace(' ', '') in str(i['name']).replace(' ', ''):
		m = starting_num
		n = final_num
		while m <= n:
			if 'app'+str(m) in str(i) and str(Stream_Name).replace(' ', '') in str(i['name']).replace(' ', ''):
				stream_list.append(i)		
			m = m + 1	
for i in stream_list:
	if str(offer_id) in str(i['offers']):
		pass
	else: 
		print(str(i['name']) + ' Не изменился!')	
print('Done testing!')		