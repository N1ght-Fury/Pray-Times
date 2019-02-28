import requests
from datetime import datetime
from datetime import timedelta
import json
							 

def inform_user(current_secs, next_time, name_of_time):
	difference = int(next_time - current_secs)
	Pray_Time = datetime.fromtimestamp(next_time)
	time_left = timedelta(seconds=difference)
	print(name_of_time + " Time:", datetime.strftime(Pray_Time, "%X"))
	print("Remaining Time:", time_left)

def main():
	url = "https://www.sabah.com.tr/json/getpraytimes/istanbul?dayafter=0"
	response = requests.get(url)
	data = str(response.content)

	data = data[2:]
	data = data.replace("xc4","").replace("xb0","")
	data = data[:-1]

	data = json.loads(data,encoding = "UTF-8")

	Imsak = int(data['List'][0]['Imsak'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
	Gunes = int(data['List'][0]['Gunes'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
	Ogle = int(data['List'][0]['Ogle'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
	Ikindi = int(data['List'][0]['Ikindi'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
	Aksam = int(data['List'][0]['Aksam'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000  
	Yatsi = int(data['List'][0]['Yatsi'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000

	current_time = datetime.now()
	in_secs = datetime.timestamp(current_time)
	difference = 0

	if (in_secs < Imsak):
		inform_user(in_secs, Imsak, "Imsak")
	elif (in_secs < Gunes):
		inform_user(in_secs, Gunes, "Gunes")
	elif (in_secs < Ogle):
		inform_user(in_secs, Ogle, "Ogle")
	elif (in_secs < Ikindi):
		inform_user(in_secs, Ikindi, "Ikindi")
	elif (in_secs < Aksam):
		inform_user(in_secs, Aksam, "Aksam")
	elif (in_secs < Yatsi):
		inform_user(in_secs, Yatsi, "Yatsi")

if __name__ == "__main__":
	main()