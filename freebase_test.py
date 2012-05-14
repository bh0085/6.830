from apiclient import discovery
from apiclient import model
import json

DEVELOPER_KEY = 'AIzaSyDGJapkaTMy09-nS96huqzdX4ftUCTJxwA'

model.JsonModel.alt_param = ""
freebase = discovery.build('freebase', 'v1', developerKey=DEVELOPER_KEY)
q_planets  = [{'id': None, 'name': None, 'type': '/astronomy/planet'}]


query = [{"type":"/music/artist","name":"The Police","album":[]}]


response = json.loads(freebase.mqlread(query=json.dumps(query)).execute())
for planet in response['result']:
	print planet
