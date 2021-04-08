#!/usr/bin/env python
import telebot
import sqlite3
from telebot import types
import requests
import json
import os
import sys
from Keys import *
from Apps import *
from Webs import *
from Sql import *
###################################################################
bot = telebot.TeleBot(TOKEN)
###################################################################
webs = [web1, web2, web3, web4, web5, web6, web7, web8, web9, web10, web11]
apps = [app1, app2, app3, app4, app5, app6, app7, app8, app9, app10, app11, app12, app13, app14, app15, app16, app17, app18, app19, app20]
###################################################################
@bot.message_handler(commands=['start'])
def command_start(message):
	bot.reply_to(message, """
Список активных приложений:
"""+str(app1).replace('Template', '')+""" 
"""+str(app2).replace('Template', '')+""" 
"""+str(app3).replace('Template', '')+""" 
"""+str(app4).replace('Template', '')+""" 
"""+str(app5).replace('Template', '')+""" 
"""+str(app6).replace('Template', '')+""" 
"""+str(app7).replace('Template', '')+""" 
"""+str(app8).replace('Template', '')+""" 
"""+str(app9).replace('Template', '')+""" 
"""+str(app10).replace('Template', '')+""" 
"""+str(app11).replace('Template', '')+""" 
"""+str(app12).replace('Template', '')+""" 
"""+str(app13).replace('Template', '')+""" 
"""+str(app14).replace('Template', '')+""" 
"""+str(app15).replace('Template', '')+"""
"""+str(app16).replace('Template', '')+""" 
"""+str(app17).replace('Template', '')+""" 
"""+str(app18).replace('Template', '')+""" 
"""+str(app19).replace('Template', '')+""" 
"""+str(app20).replace('Template', '')+"""

Список активных вебов:
"""+web1+""" 
"""+web2+""" 
"""+web3+""" 
"""+web4+""" 
"""+web5+""" 
"""+web6+""" 
"""+web7+""" 
"""+web8+""" 
"""+web9+""" 
"""+web10+""" 
"""+web11+"""

Список активных комманд:
add del /start /info
""")
###################################################################
@bot.message_handler(commands=['myid'])
def command_myid(message):
	message.chat.id
	bot.reply_to(message, message.chat.id)
###################################################################	
@bot.message_handler(commands=['restart'])
def command_restart(message):
	bot.reply_to(message, "Перезапускаюсь!")	
	os.execv(sys.executable, ['python3'] + sys.argv)
###################################################################
@bot.message_handler(commands=['help'])
def command_help(message):
	bot.reply_to(message, """
Добавить РК -> MagicWheel add 123
Удалить РК -> MagicWheel del 123
Чекнуть себя и приложение -> MagicWheel
Чекнуть помощника -> MagicWheel WebMoskow
""")
###################################################################
@bot.message_handler(commands=['check'])
def check(message):
	bot.reply_to(message, "Рико пашет!")
	requests.post('https://api.telegram.org/bot1329396156:botchat/sendMessage?chat_id=-chat&text=Рико пашет!')
###################################################################
@bot.message_handler(commands=['info'])
def command_info(message):
###################################################################
	headers = {
	    'accept': 'application/json',
	    'authorization': skak_key, }
	params = (
	    ('active', '1'),
	)
	response = requests.get('https://uclient.skakapp.com/api/app/list', headers=headers, params=params)
	active = json.loads(response.text)
	active = active.get('items')
#################
	if len(active) >= 1:
		app1lim = active[0].get('fbdddcc_limit')
	else:
		app1lim = "228"
#################
	if len(active) >= 2:
		app2lim = active[1].get('fbdddcc_limit')
	else:
		app2lim = "228"		
#################
	if len(active) >= 3:
		app3lim = active[2].get('fbdddcc_limit')
	else:
		app3lim = "228"			
#################
	if len(active) >= 4:
		app4lim = active[3].get('fbdddcc_limit')
	else:
		app4lim = "228"		
#################
	if len(active) >= 5:
		app5lim = active[4].get('fbdddcc_limit')
	else:
		app5lim = "228"		
#################
	if len(active) >= 6:
		app6lim = active[5].get('fbdddcc_limit')
	else:
		app6lim = "228"		
#################
	if len(active) >= 7:
		app7lim = active[6].get('fbdddcc_limit')
	else:
		app7lim = "228"		
#################
	if len(active) >= 8:
		app8lim = active[7].get('fbdddcc_limit')
	else:
		app8lim = "228"		
#################
	if len(active) >= 9:
		app9lim = active[8].get('fbdddcc_limit')
	else:
		app9lim = "228"		
#################
	if len(active) >= 10:
		app10lim = active[9].get('fbdddcc_limit')
	else:
		app10lim = "228"		
#################
	if len(active) >= 11:
		app11lim = active[10].get('fbdddcc_limit')
	else:
		app11lim = "228"		
#################
	if len(active) >= 12:
		app12lim = active[11].get('fbdddcc_limit')
	else:
		app12lim = "228"		
#################
	if len(active) >= 13:
		app13lim = active[12].get('fbdddcc_limit')
	else:
		app13lim = "228"		
#################
	if len(active) >= 14:
		app14lim = active[13].get('fbdddcc_limit')
	else:
		app14lim = "228"		
#################
	if len(active) >= 15:
		app15lim = active[14].get('fbdddcc_limit')
	else:
		app15lim = "228"		
#################
	if len(active) >= 16:
		app16lim = active[15].get('fbdddcc_limit')
	else:
		app16lim = "228"		
#################
	if len(active) >= 17:
		app17lim = active[16].get('fbdddcc_limit')
	else:
		app17lim = "228"		
#################
	if len(active) >= 18:
		app18lim = active[17].get('fbdddcc_limit')
	else:
		app18lim = "228"		
#################
	if len(active) >= 19:
		app19lim = active[18].get('fbdddcc_limit')
	else:
		app19lim = "228"		
#################
	if len(active) >= 20:
		app20lim = active[19].get('fbdddcc_limit')
	else:
		app20lim = "228"				
###################################################################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app1id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count1 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app2id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count2 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app3id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count3 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app4id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count4 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app5id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count5 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app6id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count6 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app7id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count7 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app8id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count8 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app9id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count9 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app10id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count10 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app11id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count11 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app12id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count12 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app13id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count13 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app14id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count14 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app15id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count15 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app16id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count16 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app17id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count17 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app18id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count18 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app19id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count19 = data['count']
#################
	headers = {
				'accept': 'application/json',
				'authorization': skak_key,
					}
	params = (
				 ('app_id', app20id),
				 )
	response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
	data = json.loads(response.text)
	count20 = data['count']
#################
	bot.reply_to(message, """
Актуальные данные по приложениям:

 """+ app1 + """ 
 Всего рк: """ + str(count1) + """, лимит: """ + str(app1lim) + """, свободно: """ + str(int(app1lim) - int(count1)) + """

 """+ app2 + """ 
 Всего рк: """ + str(count2) + """, лимит: """ + str(app2lim) + """, свободно: """ + str(int(app2lim) - int(count2)) + """

 """+ app3 + """
 Всего рк: """ + str(count3) + """, лимит: """ + str(app3lim) + """, свободно: """ + str(int(app3lim) - int(count3)) + """ 

 """+ app4 + """
 Всего рк: """ + str(count4) + """, лимит: """ + str(app4lim) + """, свободно: """ + str(int(app4lim) - int(count4)) + """ 

 """+ app5 + """
 Всего рк: """ + str(count5) + """, лимит: """ + str(app5lim) + """, свободно: """ + str(int(app5lim) - int(count5)) + """ 

 """+ app6 + """
 Всего рк: """ + str(count6) + """, лимит: """ + str(app6lim) + """, свободно: """ + str(int(app6lim) - int(count6)) + """ 

 """+ app7 + """
 Всего рк: """ + str(count7) + """, лимит: """ + str(app7lim) + """, свободно: """ + str(int(app7lim) - int(count7)) + """ 

 """+ app8 + """
 Всего рк: """ + str(count8) + """, лимит: """ + str(app8lim) + """, свободно: """ + str(int(app8lim) - int(count8)) + """ 

 """+ app9 + """
 Всего рк: """ + str(count9) + """, лимит: """ + str(app9lim) + """, свободно: """ + str(int(app9lim) - int(count9)) + """ 

 """+ app10 + """
 Всего рк: """ + str(count10) + """, лимит: """ + str(app10lim) + """, свободно: """ + str(int(app10lim) - int(count10)) + """ 

 """+ app11 + """
 Всего рк: """ + str(count11) + """, лимит: """ + str(app11lim) + """, свободно: """ + str(int(app11lim) - int(count11)) + """

 """+ app12 + """
 Всего рк: """ + str(count12) + """, лимит: """ + str(app12lim) + """, свободно: """ + str(int(app12lim) - int(count12)) + """  

 """+ app13 + """
 Всего рк: """ + str(count13) + """, лимит: """ + str(app13lim) + """, свободно: """ + str(int(app13lim) - int(count13)) + """ 

 """+ app14 + """
 Всего рк: """ + str(count14) + """, лимит: """ + str(app14lim) + """, свободно: """ + str(int(app14lim) - int(count14)) + """ 

 """+ app15 + """
 Всего рк: """ + str(count15) + """, лимит: """ + str(app15lim) + """, свободно: """ + str(int(app15lim) - int(count15)) + """ 

 """+ app16 + """
 Всего рк: """ + str(count16) + """, лимит: """ + str(app16lim) + """, свободно: """ + str(int(app16lim) - int(count16)) + """

 """+ app17 + """
 Всего рк: """ + str(count17) + """, лимит: """ + str(app17lim) + """, свободно: """ + str(int(app17lim) - int(count17)) + """  

 """+ app18 + """
 Всего рк: """ + str(count18) + """, лимит: """ + str(app18lim) + """, свободно: """ + str(int(app18lim) - int(count18)) + """ 

 """+ app19 + """
 Всего рк: """ + str(count19) + """, лимит: """ + str(app19lim) + """, свободно: """ + str(int(app19lim) - int(count19)) + """ 

 """+ app20 + """
 Всего рк: """ + str(count20) + """, лимит: """ + str(app20lim) + """, свободно: """ + str(int(app20lim) - int(count20)) + """ 
""")
###################################################################
@bot.message_handler(content_types=['text'])
def handle_message(message):
	command = message.text
	comm = command.split()
	lastChatId = message.chat.id
###################################################################
# Add()
###################################################################
	def add(app, appid, web, sql, db, id):
		headers = {
						'accept': 'application/json',
						'authorization': skak_key,
						'Content-Type': 'application/json',
						}
		data = '{"app_id": '+str(appid)+', "wuid": null, "fb_ids": '+id+'}'
		response = requests.post('https://uclient.skakapp.com/api/fbadacc/add', headers=headers, data=data)
		requests.post('https://api.telegram.org/bot1329396156:botchat/sendMessage?chat_id=-chat&text=' + 'Запушил на ' + app + ": " + id + " | chat_id: " + str(lastChatId))
		db = sqlite3.connect(app + ".db")
		sql = db.cursor()
		sql.execute('INSERT INTO webs('+web+') VALUES('+id+')')
		db.commit()
		db.close()
###################################################################
	def add_by_one(app, appid, web, sql, db):
		i = 2
		while i <= (len(comm) - 1):
			if comm[i].isdigit() == True:
				add(app, appid, web, sql, db, comm[i])
				i = i + 1
			else:
				bot.reply_to(message, "В "+ comm[i] + " есть буквы!")	
				break
###################################################################				
	def add_main(app, appid, web, sql, db):
		if len(comm) >= 3:	
#################				
			headers = {
	    			'accept': 'application/json',
	    			'authorization': skak_key,
						}
			params = (
	   			 ('app_id', appid),
					 )
			response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
			data = json.loads(response.text)
			count = data['count']
#################
			headers = {
			    'accept': 'application/json',
			    'authorization': skak_key,
			}
			params = (
			    ('active', '1'),
			)
			response = requests.get('https://uclient.skakapp.com/api/app/list', headers=headers, params=params)
			active = json.loads(response.text)
			active = active.get('items')
			i = 0
			while i < len(active):
				if app in str(active[i]).replace(" ", ""):
					applim = active[i].get('fbdddcc_limit')
				elif app not in str(active[i]):
					pass
				i = i + 1			
			if count + (len(comm) - 2) <= int(applim):
				add_by_one(app, appid, web, sql, db)
				bot.reply_to(message, "+")
			else: 
				bot.reply_to(message, "Мест нет( ... " +str(count)+ " из " + str(applim))	
###################################################################	
	def add_by_app(web):
		if comm[0].lower() == app1.lower():
			add_main(app1, app1id, web, sql1, db1)
#################
		elif comm[0].lower() == app2.lower():		
			add_main(app2, app2id, web, sql2, db2)
#################
		elif comm[0].lower() == app3.lower():		
			add_main(app3, app3id, web, sql3, db3)
#################				
		elif comm[0].lower() == app4.lower():		
			add_main(app4, app4id, web, sql4, db4)
#################					
		elif comm[0].lower() == app5.lower():		
			add_main(app5, app5id, web, sql5, db5)
#################
		elif comm[0].lower() == app6.lower():		
			add_main(app6, app6id, web, sql6, db6)
#################				
		elif comm[0].lower() == app7.lower():		
			add_main(app7, app7id, web, sql7, db7)
################# 
		elif comm[0].lower() == app8.lower():		
			add_main(app8, app8id, web, sql8, db8)
################# 				
		elif comm[0].lower() == app9.lower():		
			add_main(app9, app9id, web, sql9, db9)
################# 		
		elif comm[0].lower() == app10.lower():		
			add_main(app10, app10id, web, sql10, db10)
#################			
		elif comm[0].lower() == app11.lower():		
			add_main(app11, app11id, web, sql11, db11)
################# 			
		elif comm[0].lower() == app12.lower():		
			add_main(app12, app12id, web, sql12, db12)
#################			
		elif comm[0].lower() == app13.lower():		
			add_main(app13, app13id, web, sql13, db13)
#################	
		elif comm[0].lower() == app14.lower():		
			add_main(app14, app14id, web, sql14, db14)	
#################	
		elif comm[0].lower() == app15.lower():		
			add_main(app15, app15id, web, sql15, db15)	
#################			
		elif comm[0].lower() == app16.lower():		
			add_main(app16, app16id, web, sql16, db16)
################# 			
		elif comm[0].lower() == app17.lower():		
			add_main(app17, app17id, web, sql17, db17)
#################			
		elif comm[0].lower() == app18.lower():		
			add_main(app18, app18id, web, sql18, db18)
#################	
		elif comm[0].lower() == app19.lower():		
			add_main(app19, app19id, web, sql19, db19)	
#################	
		elif comm[0].lower() == app20.lower():		
			add_main(app20, app20id, web, sql20, db20)			
#################																																																																							
		else:
			bot.reply_to(message, "Что-то пошло не так(")	
###################################################################	
	def add_by_web():
		if lastChatId == web1_id or lastChatId == web7_id:
			add_by_app(web1)
#################			
		elif lastChatId == web2_id or lastChatId == web12_id or lastChatId == 1360561691:
			add_by_app(web2)
#################			
		elif lastChatId == web3_id:
			add_by_app(web3)
#################
		elif lastChatId == web4_id:
			add_by_app(web4)
#################
		elif lastChatId == web5_id:
			add_by_app(web5)
#################
		elif lastChatId == web6_id:
			add_by_app(web6)
#################
		elif lastChatId == web7_id:
			add_by_app(web7)
#################
		elif lastChatId == web8_id:
			add_by_app(web8)
#################
		elif lastChatId == web9_id:
			add_by_app(web9)
#################
		elif lastChatId == web10_id:
			add_by_app(web10)
#################
		elif lastChatId == web11_id:
			add_by_app(web11)
# ################
# 		elif lastChatId == web12_id:
# 			add_by_app(web12)
# ################
#  		elif lastChatId == web13_id:
# 			add_by_app(web13)
# ################
# 		elif lastChatId == web14_id:
# 			add_by_app(web14)
# ################
# 		elif lastChatId == web15_id:
# 			add_by_app(web15)
# ################
		else:
			bot.reply_to(message, "Ты хто?")
###################################################################
# Del()
###################################################################
	def delete(app, appid, web, sql, db, id):
		headers = {
					'accept': 'application/json',
					'authorization': skak_key,
					'Content-Type': 'application/json',
					}
		data = '{"app_id": '+str(appid)+', "wuid": null, "fb_ids": '+id+', "all": false, "all_org": false}'
		response = requests.post('https://uclient.skakapp.com/api/fbadacc/delete', headers=headers, data=data)
		requests.post('https://api.telegram.org/bot1329396156:botchat/sendMessage?chat_id=-chat&text=' + 'Удалил на ' + app + ": " + id + " | chat_id: " +str(lastChatId))
		db = sqlite3.connect(app + ".db")
		sql = db.cursor()
		sql.execute('DELETE FROM webs WHERE '+web+'='+id+'')
		db.commit()
		db.close()
###################################################################
	def delete_by_one(app, appid, web, sql, db):
		i = 2
		while i <= (len(comm) - 1):
			if comm[i].isdigit() == True:
				delete(app, appid, web, sql, db, comm[i])
				i = i + 1
			else:
				bot.reply_to(message, "В "+ comm[i] + " есть буквы!")	
				break
###################################################################				
	def delete_main(app, appid, web, sql, db):
		if len(comm) >= 3:
			delete_by_one(app, appid, web, sql, db)
			bot.reply_to(message, "+")
###################################################################				
	def delete_by_app(web):
		if comm[0].lower() == app1.lower():
			delete_main(app1, app1id, web, sql1, db1)
#################
		elif comm[0].lower() == app2.lower():		
			delete_main(app2, app2id, web, sql2, db2)
#################
		elif comm[0].lower() == app3.lower():		
			delete_main(app3, app3id, web, sql3, db3)
#################				
		elif comm[0].lower() == app4.lower():		
			delete_main(app4, app4id, web, sql4, db4)
#################					
		elif comm[0].lower() == app5.lower():		
			delete_main(app5, app5id, web, sql5, db5)
#################
		elif comm[0].lower() == app6.lower():		
			delete_main(app6, app6id, web, sql6, db6)
#################				
		elif comm[0].lower() == app7.lower():		
			delete_main(app7, app7id, web, sql7, db7)
################# 
		elif comm[0].lower() == app8.lower():		
			delete_main(app8, app8id, web, sql8, db8)
################# 				
		elif comm[0].lower() == app9.lower():		
			delete_main(app9, app9id, web, sql9, db9)
################# 		
		elif comm[0].lower() == app10.lower():		
			delete_main(app10, app10id, web, sql10, db10)
#################			
		elif comm[0].lower() == app11.lower():		
			delete_main(app11, app11id, web, sql11, db11)
################# 			
		elif comm[0].lower() == app12.lower():		
			delete_main(app12, app12id, web, sql12, db12)
#################			
		elif comm[0].lower() == app13.lower():		
			delete_main(app13, app13id, web, sql13, db13)
#################	
		elif comm[0].lower() == app14.lower():		
			delete_main(app14, app14id, web, sql14, db14)	
#################	
		elif comm[0].lower() == app15.lower():		
			delete_main(app15, app15id, web, sql15, db15)	
#################
		elif comm[0].lower() == app16.lower():		
			delete_main(app16, app16id, web, sql16, db16)
################# 			
		elif comm[0].lower() == app17.lower():		
			delete_main(app17, app17id, web, sql17, db17)
#################			
		elif comm[0].lower() == app18.lower():		
			delete_main(app18, app18id, web, sql18, db18)
#################	
		elif comm[0].lower() == app19.lower():		
			delete_main(app19, app19id, web, sql19, db19)	
#################	
		elif comm[0].lower() == app20.lower():		
			delete_main(app20, app20id, web, sql20, db20)			
#################																																																																							
		else:
			bot.reply_to(message, "Что-то пошло не так(")	
###################################################################	
	def delete_by_web():
		if lastChatId == web1_id or lastChatId == web7_id:
			delete_by_app(web1)
#################			
		elif lastChatId == web2_id or lastChatId == web12_id or lastChatId == 1360561691:
			delete_by_app(web2)
#################			
		elif lastChatId == web3_id:
			delete_by_app(web3)
#################
		elif lastChatId == web4_id:
			delete_by_app(web4)
#################
		elif lastChatId == web5_id:
			delete_by_app(web5)
#################
		elif lastChatId == web6_id:
			delete_by_app(web6)
#################
		elif lastChatId == web7_id:
			delete_by_app(web7)
#################
		elif lastChatId == web8_id:
			delete_by_app(web8)
#################
		elif lastChatId == web9_id:
			delete_by_app(web9)
#################
		elif lastChatId == web10_id:
			delete_by_app(web10)
#################
		elif lastChatId == web11_id:
			delete_by_app(web11)
# ################
# 		elif lastChatId == web12_id:
# 			delete_by_app(web12)
# ################
#  		elif lastChatId == web13_id:
# 			delete_by_app(web13)
# ################
# 		elif lastChatId == web14_id:
# 			delete_by_app(web14)
# ################
# 		elif lastChatId == web15_id:
# 			delete_by_app(web15)
# ################
		else:
			bot.reply_to(message, "Ты хто?")
###################################################################	
# Check()
###################################################################				
	def check_main(app, appid, web, sql, db):
		headers = {
    			'accept': 'application/json',
    			'authorization': skak_key,
					}
		params = (
   			 ('app_id', appid),
				 )
		response = requests.get('https://uclient.skakapp.com/api/fbadacc/list', headers=headers, params=params)
		data = json.loads(response.text)
		count = data['count']
#################
		headers = {
		    'accept': 'application/json',
		    'authorization': skak_key,
		}
		params = (
		    ('active', '1'),
		)
		response = requests.get('https://uclient.skakapp.com/api/app/list', headers=headers, params=params)
		active = json.loads(response.text)
		active = active.get('items')
		i = 0
		while i < len(active):
			if app in str(active[i]).replace(" ", ""):
				applim = active[i].get('fbdddcc_limit')
				geo = active[i].get('organic_countries')
			elif app not in str(active[i]):
				pass
			i = i + 1
#################
		headers = {
		    'accept': 'application/json',
		    'authorization': skak_key,
		}
		response = requests.get('https://uclient.skakapp.com/api/fbadacc/list?app_id='+str(appid)+'', headers=headers)
		r = json.loads(response.text)
		r = r.get('items')
		i = 0
		skaklist = list()
		while i < len(r):
			skaklist.append(r[i].get('fb_id'))
			i = i + 1
#################
		db = sqlite3.connect(app + ".db")
		sql = db.cursor()
		sql.execute("SELECT "+web+" FROM webs")
		results = str(sql.fetchall())
		db.close()		
		res = results.replace("(None,)", "")
		res = str(res)
		res = res.replace("(", "")
		res = res.replace(")", "")
		res = res.replace(" ", "")
		res = res.replace("[", "")
		res = res.replace("]", "")			
		res = res.replace(",", " ")	
		res = res.split()
		res = str(res)
		res = res.replace("[", "")
		res = res.replace("]", "")	
		res = res.replace("'", "")		
		res = res.replace(" ", "")
		res = res.replace(",", " ")
		res = res.split()
#################		
		true_list = list(set(skaklist) & set(res))
#################
		# if web == 'WebDem' or web == 'WebSydney':
		# 	delfid = '[2]'
		# elif web == 'WebGraf' or web == 'WebMoskow':
		# 	delfid == '[3]'
		# elif web == 'WebSecretVictory':
		# 	delfid == '[4]'
		# elif web == 'WebAnelin' or web == 'WebLissabon':
		# 	delfid == '[6]'
		# elif web == 'WebDubai':
		# 	delfid == '[7]'
		# elif web == 'WebLemon':
		# 	delfid == '[8]'
		# elif web == 'WebIceman':
		# 	delfid == '[9]'
		# elif web == 'WebTenerife':
		# 	delfid == '[10]'
		# else:
		# 	delfid == '-1'																			
#################
		headers = {
		    'Content-Type': 'application/json',
		    'Authorization': dolphin_key,
		}
		data = '{"users_ids": -1}'
		response = requests.get('https://domain/new/cabs', headers=headers, data=data)
		r = json.loads(response.text)
		r = r.get('data')
		active_list = list()
		inactive_list = list()
		moder_list = list()
		token_list = list()	
		for i in r:
			if i['account']['status'] == 'TOKEN_ERROR':
				token_list.append(i['cab_id'])			
			elif i['status'] == 1:
				active_list.append(i['cab_id'])
			elif i['status'] == 2 and i['disable_reason'] == 1:
				inactive_list.append(i['cab_id'])	
			elif i['status'] == 2 and i['disable_reason'] == 3:
				inactive_list.append(i['cab_id'])									
			else:
				moder_list.append(i['cab_id'])					
#################						
		active_list = list(set(true_list) & set(active_list))
		inactive_list = list(set(true_list) & set(inactive_list))		
		moder_list = list(set(true_list) & set(moder_list))		
		token_list = list(set(true_list) & set(token_list))			
		unknown_list = list(set(true_list) - set(active_list + moder_list + inactive_list))			
#################
		true_list = str(true_list)
		true_list = true_list.replace(" ", "")
		true_list = true_list.replace("[", "")
		true_list = true_list.replace("]", "")	
		true_list = true_list.replace("'", "")			
		true_list = true_list.replace(",", " ")
#################			
		active_list = str(active_list)
		active_list = active_list.replace(" ", "")
		active_list = active_list.replace("[", "")
		active_list = active_list.replace("]", "")	
		active_list = active_list.replace("'", "")			
		active_list = active_list.replace(",", " ")	
#################	
		inactive_list = str(inactive_list)
		inactive_list = inactive_list.replace(" ", "")
		inactive_list = inactive_list.replace("[", "")
		inactive_list = inactive_list.replace("]", "")	
		inactive_list = inactive_list.replace("'", "")			
		inactive_list = inactive_list.replace(",", " ")	
#################					
		moder_list = str(moder_list)
		moder_list = moder_list.replace(" ", "")
		moder_list = moder_list.replace("[", "")
		moder_list = moder_list.replace("]", "")	
		moder_list = moder_list.replace("'", "")			
		moder_list = moder_list.replace(",", " ")								
#################					
		token_list = str(token_list)
		token_list = token_list.replace(" ", "")
		token_list = token_list.replace("[", "")
		token_list = token_list.replace("]", "")	
		token_list = token_list.replace("'", "")			
		token_list = token_list.replace(",", " ")
#################		
		unknown_list = str(unknown_list)
		unknown_list = unknown_list.replace(" ", "")
		unknown_list = unknown_list.replace("[", "")
		unknown_list = unknown_list.replace("]", "")	
		unknown_list = unknown_list.replace("'", "")			
		unknown_list = unknown_list.replace(",", " ")	
#################
		geo = str(geo)
		geo = geo.replace("[", "")
		geo = geo.replace("]", "")
		geo = geo.replace("'", "")
		geo = geo.replace(",", " ")
		bot.reply_to(message, """
Название: """+app+"""

Всего РК: """+str(count)+"""

Лимит: """+str(applim)+"""

Свободно: """+str(applim - count)+"""

Органика: """+str(geo)+"""


МОЙ СПИСОК
("""+str(web)+""")

Всего РК: """+str(len(true_list.split()))+"""

Все:
"""+str(true_list)+"""

Из них активные:
"""+str(active_list)+"""

Из них неактивные:
"""+str(inactive_list)+"""

Из них ошибка токена:
"""+str(token_list)+"""

Из них на модерации (или другая проблема):
"""+str(moder_list)+"""

Из них нет в дельфине:
"""+str(unknown_list)+"""
""")
###################################################################				
	def check_by_app(web):
		if comm[0].lower() == app1.lower():
			check_main(app1, app1id, web, sql1, db1)
#################
		elif comm[0].lower() == app2.lower():		
			check_main(app2, app2id, web, sql2, db2)
#################
		elif comm[0].lower() == app3.lower():		
			check_main(app3, app3id, web, sql3, db3)
#################				
		elif comm[0].lower() == app4.lower():		
			check_main(app4, app4id, web, sql4, db4)
#################					
		elif comm[0].lower() == app5.lower():		
			check_main(app5, app5id, web, sql5, db5)
#################
		elif comm[0].lower() == app6.lower():		
			check_main(app6, app6id, web, sql6, db6)
#################				
		elif comm[0].lower() == app7.lower():		
			check_main(app7, app7id, web, sql7, db7)
################# 
		elif comm[0].lower() == app8.lower():		
			check_main(app8, app8id, web, sql8, db8)
################# 				
		elif comm[0].lower() == app9.lower():		
			check_main(app9, app9id, web, sql9, db9)
################# 		
		elif comm[0].lower() == app10.lower():		
			check_main(app10, app10id, web, sql10, db10)
#################			
		elif comm[0].lower() == app11.lower():		
			check_main(app11, app11id, web, sql11, db11)
################# 			
		elif comm[0].lower() == app12.lower():		
			check_main(app12, app12id, web, sql12, db12)
#################			
		elif comm[0].lower() == app13.lower():		
			check_main(app13, app13id, web, sql13, db13)
#################	
		elif comm[0].lower() == app14.lower():		
			check_main(app14, app14id, web, sql14, db14)	
#################	
		elif comm[0].lower() == app15.lower():		
			check_main(app15, app15id, web, sql15, db15)	
#################
		elif comm[0].lower() == app16.lower():		
			check_main(app16, app16id, web, sql16, db16)
################# 			
		elif comm[0].lower() == app17.lower():		
			check_main(app17, app17id, web, sql17, db17)
#################			
		elif comm[0].lower() == app18.lower():		
			check_main(app18, app18id, web, sql18, db18)
#################	
		elif comm[0].lower() == app19.lower():		
			check_main(app19, app19id, web, sql19, db19)	
#################	
		elif comm[0].lower() == app20.lower():		
			check_main(app20, app20id, web, sql20, db20)			
#################																																																																							
		else:
			bot.reply_to(message, "Что-то пошло не так(")	
###################################################################	
	def check_by_web():
		if lastChatId == web1_id or lastChatId == web7_id:
			check_by_app(web1)
#################			
		elif lastChatId == web2_id or lastChatId == web12_id or lastChatId == 1360561691:
			check_by_app(web2)
#################			
		elif lastChatId == web3_id:
			check_by_app(web3)
#################
		elif lastChatId == web4_id:
			check_by_app(web4)
#################
		elif lastChatId == web5_id:
			check_by_app(web5)
#################
		elif lastChatId == web6_id:
			check_by_app(web6)
#################
		elif lastChatId == web7_id:
			check_by_app(web7)
#################
		elif lastChatId == web8_id:
			check_by_app(web8)
#################
		elif lastChatId == web9_id:
			check_by_app(web9)
#################
		elif lastChatId == web10_id:
			check_by_app(web10)
#################
		elif lastChatId == web11_id:
			check_by_app(web11)
# ################
# 		elif lastChatId == web12_id:
# 			check_by_app(web12)
# ################
#  		elif lastChatId == web13_id:
# 			check_by_app(web13)
# ################
# 		elif lastChatId == web14_id:
# 			check_by_app(web14)
# ################
# 		elif lastChatId == web15_id:
# 			check_by_app(web15)
# ################
		else:
			bot.reply_to(message, "Ты хто?")	
###################################################################			
	def mylist(web, app, appid):
#################
		headers = {
		    'accept': 'application/json',
		    'authorization': skak_key,
		}
		response = requests.get('https://uclient.skakapp.com/api/fbadacc/list?app_id='+str(appid)+'', headers=headers)
		r = json.loads(response.text)
		r = r.get('items')
		i = 0
		skaklist = list()
		while i < len(r):
			skaklist.append(r[i].get('fb_id'))
			i = i + 1
#################
		db = sqlite3.connect(app + ".db")
		sql = db.cursor()
		sql.execute("SELECT "+web+" FROM webs")
		results = str(sql.fetchall())
		db.close()		
		res = results.replace("(None,)", "")
		res = str(res)
		res = res.replace("(", "")
		res = res.replace(")", "")
		res = res.replace(" ", "")
		res = res.replace("[", "")
		res = res.replace("]", "")			
		res = res.replace(",", " ")	
		res = res.split()
		res = str(res)
		res = res.replace("[", "")
		res = res.replace("]", "")	
		res = res.replace("'", "")		
		res = res.replace(" ", "")
		res = res.replace(",", " ")
		res = res.split()
#################		
		true_list = list(set(skaklist) & set(res))
#################
		# if web == 'WebDem' or web == 'WebSydney':
		# 	delfid = '[2]'
		# elif web == 'WebGraf' or web == 'WebMoskow':
		# 	delfid == '[3]'
		# elif web == 'WebSecretVictory':
		# 	delfid == '[4]'
		# elif web == 'WebAnelin' or web == 'WebLissabon':
		# 	delfid == '[6]'
		# elif web == 'WebDubai':
		# 	delfid == '[7]'
		# elif web == 'WebLemon':
		# 	delfid == '[8]'
		# elif web == 'WebIceman':
		# 	delfid == '[9]'
		# elif web == 'WebTenerife':
		# 	delfid == '[10]'
		# else:
		# 	delfid == '-1'																			
#################
		headers = {
		    'Content-Type': 'application/json',
		    'Authorization': dolphin_key,
		}
		data = '{"users_ids": -1}'
		response = requests.get('https://domain/new/cabs', headers=headers, data=data)
		r = json.loads(response.text)
		r = r.get('data')
		active_list = list()
		inactive_list = list()
		moder_list = list()	
		token_list = list()				
		for i in r:
			if i['account']['status'] == 'TOKEN_ERROR':
				token_list.append(i['cab_id'])			
			elif i['status'] == 1:
				active_list.append(i['cab_id'])
			elif i['status'] == 2 and i['disable_reason'] == 1:
				inactive_list.append(i['cab_id'])	
			elif i['status'] == 2 and i['disable_reason'] == 3:
				inactive_list.append(i['cab_id'])									
			else:
				moder_list.append(i['cab_id'])		
#################						
		active_list = list(set(true_list) & set(active_list))
		inactive_list = list(set(true_list) & set(inactive_list))		
		moder_list = list(set(true_list) & set(moder_list))		
		token_list = list(set(true_list) & set(token_list))
		unknown_list = list(set(true_list) - set(active_list + moder_list + inactive_list))			
#################
		true_list = str(true_list)
		true_list = true_list.replace(" ", "")
		true_list = true_list.replace("[", "")
		true_list = true_list.replace("]", "")	
		true_list = true_list.replace("'", "")			
		true_list = true_list.replace(",", " ")
#################			
		active_list = str(active_list)
		active_list = active_list.replace(" ", "")
		active_list = active_list.replace("[", "")
		active_list = active_list.replace("]", "")	
		active_list = active_list.replace("'", "")			
		active_list = active_list.replace(",", " ")	
#################	
		inactive_list = str(inactive_list)
		inactive_list = inactive_list.replace(" ", "")
		inactive_list = inactive_list.replace("[", "")
		inactive_list = inactive_list.replace("]", "")	
		inactive_list = inactive_list.replace("'", "")			
		inactive_list = inactive_list.replace(",", " ")	
#################					
		moder_list = str(moder_list)
		moder_list = moder_list.replace(" ", "")
		moder_list = moder_list.replace("[", "")
		moder_list = moder_list.replace("]", "")	
		moder_list = moder_list.replace("'", "")			
		moder_list = moder_list.replace(",", " ")
#################			
		token_list = str(token_list)
		token_list = token_list.replace(" ", "")
		token_list = token_list.replace("[", "")
		token_list = token_list.replace("]", "")	
		token_list = token_list.replace("'", "")			
		token_list = token_list.replace(",", " ")										
#################
		unknown_list = str(unknown_list)
		unknown_list = unknown_list.replace(" ", "")
		unknown_list = unknown_list.replace("[", "")
		unknown_list = unknown_list.replace("]", "")	
		unknown_list = unknown_list.replace("'", "")			
		unknown_list = unknown_list.replace(",", " ")	
#################
		bot.reply_to(message, """
("""+str(web)+""")

Всего РК: """+str(len(true_list.split()))+"""

Все:
"""+str(true_list)+"""

Из них активные:
"""+str(active_list)+"""

Из них неактивные:
"""+str(inactive_list)+"""

Из них ошибка токена:
"""+str(token_list)+"""

Из них на модерации (или другая проблема):
"""+str(moder_list)+"""

Из них нет в дельфине:
"""+str(unknown_list)+"""
""")
###################################################################			
	def mylist_by_web(app, appid):
		mylist(web1, app, appid)
		mylist(web2, app, appid)
		mylist(web3, app, appid)
		mylist(web4, app, appid)
		mylist(web5, app, appid)
		mylist(web6, app, appid)
		mylist(web7, app, appid)
		mylist(web8, app, appid)
		mylist(web9, app, appid)
		mylist(web10, app, appid)
		mylist(web11, app, appid)
		# mylist(web12, app, appid)
		# mylist(web13, app, appid)
		# mylist(web14, app, appid)
		# mylist(web15, app, appid)	
###################################################################			
	def mylist_by_app():
		if comm[0].lower() == app1.lower():
			mylist_by_web(app1, app1id)
		elif comm[0].lower() == app2.lower():
			mylist_by_web(app2, app2id)
		elif comm[0].lower() == app3.lower():
			mylist_by_web(app3, app3id)
		elif comm[0].lower() == app4.lower():
			mylist_by_web(app4, app4id)
		elif comm[0].lower() == app5.lower():
			mylist_by_web(app5, app5id)
		elif comm[0].lower() == app6.lower():
			mylist_by_web(app6, app6id)
		elif comm[0].lower() == app7.lower():
			mylist_by_web(app7, app7id)
		elif comm[0].lower() == app8.lower():	
			mylist_by_web(app8, app8id)
		elif comm[0].lower() == app9.lower():	
			mylist_by_web(app9, app9id)
		elif comm[0].lower() == app10.lower():	
			mylist_by_web(app10, app10id)
		elif comm[0].lower() == app11.lower():	
			mylist_by_web(app11, app11id)
		elif comm[0].lower() == app12.lower():	
			mylist_by_web(app12, app12id)
		elif comm[0].lower() == app13.lower():
			mylist_by_web(app13, app13id)
		elif comm[0].lower() == app14.lower():
			mylist_by_web(app14, app14id)
		elif comm[0].lower() == app15.lower():
			mylist_by_web(app15, app15id)
		elif comm[0].lower() == app16.lower():		
			mylist_by_web(app16, app16id) 			
		elif comm[0].lower() == app17.lower():		
			mylist_by_web(app17, app17id)			
		elif comm[0].lower() == app18.lower():		
			mylist_by_web(app18, app18id)	
		elif comm[0].lower() == app19.lower():		
			mylist_by_web(app19, app19id)		
		elif comm[0].lower() == app20.lower():		
			mylist_by_web(app20, app20id)							
		else:
			bot.reply_to(message, "Не понял куда, бос")			
###################################################################	
	def mylist_by_web_classic(app, appid):
		if lastChatId == web5_id and comm[1] == web3:
			mylist(web3, app, appid)
		elif lastChatId == web1_id and comm[1] == web7:
			mylist(web7, app, appid)
		elif lastChatId == web8_id and comm[1] == web11:
			mylist(web11, app, appid)
		# elif (comm[1].lower() == web12.lower() and lastChatId == web2_id) or lastChatId == 1360561691:
		# 	mylist(web12, app)			
		else:
			bot.reply_to(message, "Нет доступа, дружок")	
###################################################################				
	def mylist_by_app_classic():
		if comm[0].lower() == app1.lower():
			mylist_by_web_classic(app1, app1id)
		elif comm[0].lower() == app2.lower():
			mylist_by_web_classic(app2, app2id)
		elif comm[0].lower() == app3.lower():
			mylist_by_web_classic(app3, app3id)
		elif comm[0].lower() == app4.lower():
			mylist_by_web_classic(app4, app4id)
		elif comm[0].lower() == app5.lower():
			mylist_by_web_classic(app5, app5id)
		elif comm[0].lower() == app6.lower():
			mylist_by_web_classic(app6, app6id)
		elif comm[0].lower() == app7.lower():
			mylist_by_web_classic(app7, app7id)
		elif comm[0].lower() == app8.lower():	
			mylist_by_web_classic(app8, app8id)
		elif comm[0].lower() == app9.lower():	
			mylist_by_web_classic(app9, app9id)
		elif comm[0].lower() == app10.lower():	
			mylist_by_web_classic(app10, app10id)
		elif comm[0].lower() == app11.lower():	
			mylist_by_web_classic(app11, app11id)
		elif comm[0].lower() == app12.lower():	
			mylist_by_web_classic(app12, app12id)
		elif comm[0].lower() == app13.lower():
			mylist_by_web_classic(app13, app13id)
		elif comm[0].lower() == app14.lower():
			mylist_by_web_classic(app14, app14id)
		elif comm[0].lower() == app15.lower():
			mylist_by_web_classic(app15, app15id)
		elif comm[0].lower() == app16.lower():		
			mylist_by_web_classic(app16, app16id) 			
		elif comm[0].lower() == app17.lower():		
			mylist_by_web_classic(app17, app17id)			
		elif comm[0].lower() == app18.lower():		
			mylist_by_web_classic(app18, app18id)	
		elif comm[0].lower() == app19.lower():		
			mylist_by_web_classic(app19, app19id)		
		elif comm[0].lower() == app20.lower():		
			mylist_by_web_classic(app20, app20id)			
		else:
			bot.reply_to(message, "Куда?")
######################################################################################################################################				
	if comm[0] == somekey:
		os._exit(0)					
	elif comm[0].lower() not in str(apps).lower():
		bot.reply_to(message, "Куда-куда?")	
###################################################################
	elif len(comm) == 1:
		check_by_web()
###################################################################		
	elif comm[1] == "add":
		if len(comm) == 2:
			bot.reply_to(message, "Пустовато как-то...")	
		elif len(comm) > 2:
			add_by_web()	
###################################################################			
	elif comm[1] == "del":
		if len(comm) == 2:
			bot.reply_to(message, "Пустовато как-то...")	
		elif len(comm) > 2:
			delete_by_web()
###################################################################
	elif comm[1].lower() in str(webs).lower():
		mylist_by_app_classic()	
###################################################################			
	elif comm[1].lower() == "master" and (lastChatId == 1360561691 or 1260324935):
		mylist_by_app()
################################################################### 
	else:
		bot.reply_to(message, "Во втором слове что-то не так...")
######################################################################################################################################
bot.polling()