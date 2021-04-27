from apscheduler.schedulers.background import BackgroundScheduler
import time
import requests
import json
import random

url = "http://127.0.0.1:8000/api/characters"

def characters():
	try:
		item = random.randint(1,2000)
		url = "https://anapioficeandfire.com/api/characters/"+str(item)
		payload={}
		headers = {}
		response = requests.request("GET", url, headers=headers, data=payload)
		return response.text
	except Exception as e:
		print(e) 

def insert_haracter(name, gender):
	try:
		payload={
				'name': name,
				'gender': gender,
		}
		files=[]
		headers = {}
		requests.request("POST", url, headers=headers, data=payload, files=files)
	except Exception as e:
		print(e) 

# This is the function you want to schedule - add as many as you want and then register them in the start() function below
def deactivate_expired_accounts():
	try:
		data = characters()
		j = json.loads(data)
		if j['name'] != '' and j['gender'] != '':
			insert_haracter(j['name'], j['gender'])
	except Exception as e:
		print(e)   

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(deactivate_expired_accounts, 'interval', seconds=3)
    scheduler.start()

init = False
while True:
    if init == False:
        start()
        init = True
    time.sleep(1)