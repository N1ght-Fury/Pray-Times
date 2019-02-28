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
	for i in range(2):
		print(i)
		url = "https://www.sabah.com.tr/json/getpraytimes/istanbul?dayafter=" + str(i)
		response = requests.get(url)
		data = str(response.content)

		data = data[2:]
		data = data.replace("xc4","").replace("xb0","")
		data = data[:-1]

		data = json.loads(data,encoding = "UTF-8")

		Imsak = int(data['List'][i]['Imsak'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
		Gunes = int(data['List'][i]['Gunes'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
		Ogle = int(data['List'][i]['Ogle'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
		Ikindi = int(data['List'][i]['Ikindi'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
		Aksam = int(data['List'][i]['Aksam'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000  
		Yatsi = int(data['List'][i]['Yatsi'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000

		current_time = datetime.now()
		in_secs = datetime.timestamp(current_time)
		difference = 0

		if (in_secs < Imsak):
			inform_user(in_secs, Imsak, "Imsak")
			return 0
		elif (in_secs < Gunes):
			inform_user(in_secs, Gunes, "Gunes")
			return 0
		elif (in_secs < Ogle):
			inform_user(in_secs, Ogle, "Ogle")
			return 0
		elif (in_secs < Ikindi):
			inform_user(in_secs, Ikindi, "Ikindi")
			return 0
		elif (in_secs < Aksam):
			inform_user(in_secs, Aksam, "Aksam")
			return 0
		elif (in_secs < Yatsi):
			inform_user(in_secs, Yatsi, "Yatsi")
			return 0

if __name__ == "__main__":
	main()
