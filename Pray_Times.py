import requests
from datetime import datetime
from datetime import timedelta
import json
import sys
					 

def inform_user(current_secs, next_time, name_of_time):
	difference = int(next_time - current_secs)
	Pray_Time = datetime.fromtimestamp(next_time)
	time_left = timedelta(seconds=difference)
	print(name_of_time + " Time:", datetime.strftime(Pray_Time, "%X"))
	print("Remaining Time:", time_left)

def get_city():
	response = requests.get('https://ipinfo.io/json')
	city = str(json.loads(response.content)['city']).lower()
	return city

def write_city_to_file(city):
	with open('city.txt', 'w+') as f:
		f.write(city)

def read_city():
	with open('city.txt', 'r') as f:
		return str(f.read())

def check_if_province_exists(province):
	provinces = []
	with open('provinces.txt', 'r') as f:
		provinces = [city.replace('\n', '') for city in f.readlines()]

	for city in provinces:
		if (city == province):
			return True
	return False

def main():

	if (len(sys.argv) > 1):
		if (sys.argv[1] == '--update'):
			write_city_to_file(sys.argv[2])
			city = read_city()
		elif (check_if_province_exists(sys.argv[1])):
			city = sys.argv[1]
		else:
			print('Invalid argument. Available arguments:')
			print('--update [CITY NAME]')
			print('[CITY NAME]')
			print('Make sure to type city name correct.')
			return 0

	else:
		try:
			city = get_city()
		except Exception as e:
			try:
				city = read_city()
			except Exception as e:
				city = input('[+] Enter the city you live in: ').lower()
				write_city_to_file(city)


	for i in range(2):

		url = "https://www.sabah.com.tr/json/getpraytimes/" + city + "?dayafter=1"
		try:
			response = requests.get(url)
		except:
			print("Connection error.")
			return 0
		
		data = str(response.content)

		data = data[2:]
		data = data.replace('xc4','').replace('xb0','').replace('xc3','').replace('x9c','').replace('xc5','').replace('x9e','')
		data = data[:-1]

		data = json.loads(data, encoding = "UTF-8")

		Imsak = int(data['List'][i]['Imsak'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
		Gunes = int(data['List'][i]['Gunes'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
		Ogle = int(data['List'][i]['Ogle'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
		Ikindi = int(data['List'][i]['Ikindi'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000
		Aksam = int(data['List'][i]['Aksam'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000  
		Yatsi = int(data['List'][i]['Yatsi'].replace("Date","").replace("(","").replace(")","").replace("/","")[:-1][1:]) / 1000

		in_secs = datetime.timestamp(datetime.now())

		if (in_secs < Imsak):
			inform_user(in_secs, Imsak, "Imsak")
			#inform_user(in_secs, Gunes, "Gunes")
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
