import requests
import json
from Keys import *
###################################################################
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
###################################################################
if len(active) >= 1:
	app1 = active[0].get('name')
	app1id = active[0].get('id')
#################
	app1 = app1[-(len(app1)-5):]
	app1 = app1.replace(" ", "")
#################
else:
	app1 = "Template"
	app1id = "2616"
###################################################################
if len(active) >= 2:
	app2 = active[1].get('name')
	app2id = active[1].get('id')
#################
	app2 = app2[-(len(app2)-5):]
	app2 = app2.replace(" ", "")
#################	
else:
	app2 = "Template"
	app2id = "2616"
###################################################################
if len(active) >= 3:
	app3 = active[2].get('name')
	app3id = active[2].get('id')
#################
	app3 = app3[-(len(app3)-5):]
	app3 = app3.replace(" ", "")
#################	
else:
	app3 = "Template"
	app3id = "2616"
###################################################################
if len(active) >= 4:
	app4 = active[3].get('name')
	app4id = active[3].get('id')
#################
	app4 = app4[-(len(app4)-5):]
	app4 = app4.replace(" ", "")
#################	
else:
	app4 = "Template"
	app4id = "2616"
###################################################################
if len(active) >= 5:
	app5 = active[4].get('name')
	app5id = active[4].get('id')
#################
	app5 = app5[-(len(app5)-5):]
	app5 = app5.replace(" ", "")
#################	
else:
	app5 = "Template"
	app5id = "2616"
###################################################################
if len(active) >= 6:
	app6 = active[5].get('name')
	app6id = active[5].get('id')
#################
	app6 = app6[-(len(app6)-5):]
	app6 = app6.replace(" ", "")
#################	
else:
	app6 = "Template"
	app6id = "2616"
###################################################################
if len(active) >= 7:
	app7 = active[6].get('name')
	app7id = active[6].get('id')
#################
	app7 = app7[-(len(app7)-5):]
	app7 = app7.replace(" ", "")
#################	
else:
	app7 = "Template"
	app7id = "2616"
###################################################################
if len(active) >= 8:
	app8 = active[7].get('name')
	app8id = active[7].get('id')
#################
	app8 = app8[-(len(app8)-5):]
	app8 = app8.replace(" ", "")
#################	
else:
	app8 = "Template"
	app8id = "2616"
###################################################################
if len(active) >= 9:
	app9 = active[8].get('name')
	app9id = active[8].get('id')
#################
	app9 = app9[-(len(app9)-5):]
	app9 = app9.replace(" ", "")
#################	
else:
	app9 = "Template"
	app9id = "2616"
###################################################################
if len(active) >= 10:
	app10 = active[9].get('name')
	app10id = active[9].get('id')
#################
	app10 = app10[-(len(app10)-5):]
	app10 = app10.replace(" ", "")
#################
else:
	app10 = "Template"
	app10id = "2616"
###################################################################
if len(active) >= 11:
	app11 = active[10].get('name')
	app11id = active[10].get('id')
#################
	app11 = app11[-(len(app11)-5):]
	app11 = app11.replace(" ", "")
#################	
else:
	app11 = "Template"
	app11id = "2616"
###################################################################
if len(active) >= 12:
	app12 = active[11].get('name')
	app12id = active[11].get('id')
#################
	app12 = app12[-(len(app12)-5):]
	app12 = app12.replace(" ", "")
#################
else:
	app12 = "Template"
	app12id = "2616"
###################################################################
if len(active) >= 13:
	app13 = active[12].get('name')
	app13id = active[12].get('id')
#################
	app13 = app13[-(len(app13)-5):]
	app13 = app13.replace(" ", "")
#################
else:
	app13 = "Template"
	app13id = "2616"
###################################################################
if len(active) >= 14:
	app14 = active[13].get('name')
	app14id = active[13].get('id')
#################
	app14 = app14[-(len(app14)-5):]
	app14 = app14.replace(" ", "")
#################
else:
	app14 = "Template"
	app14id = "2616"
###################################################################
if len(active) >= 15:
	app15 = active[14].get('name')
	app15id = active[14].get('id')
#################
	app15 = app15[-(len(app15)-5):]
	app15 = app15.replace(" ", "")
#################
else:
	app15 = "Template"
	app15id = "2616"
###################################################################
if len(active) >= 16:
	app16 = active[15].get('name')
	app16id = active[15].get('id')
#################
	app16 = app16[-(len(app16)-5):]
	app16 = app16.replace(" ", "")
#################
else:
	app16 = "Template"
	app16id = "2616"
###################################################################
if len(active) >= 17:
	app17 = active[16].get('name')
	app17id = active[16].get('id')
#################
	app17 = app17[-(len(app17)-5):]
	app17 = app17.replace(" ", "")
#################
else:
	app17 = "Template"
	app17id = "2616"
###################################################################
if len(active) >= 18:
	app18 = active[17].get('name')
	app18id = active[17].get('id')
#################
	app18 = app18[-(len(app18)-5):]
	app18 = app18.replace(" ", "")
#################
else:
	app18 = "Template"
	app18id = "2616"
###################################################################
if len(active) >= 19:
	app19 = active[18].get('name')
	app19id = active[18].get('id')
#################
	app19 = app19[-(len(app19)-5):]
	app19 = app19.replace(" ", "")
#################
else:
	app19 = "Template"
	app19id = "2616"
###################################################################
if len(active) >= 20:
	app20 = active[19].get('name')
	app20id = active[19].get('id')
#################
	app20 = app20[-(len(app20)-5):]
	app20 = app20.replace(" ", "")
#################
else:
	app20 = "Template"
	app20id = "2616"
###################################################################