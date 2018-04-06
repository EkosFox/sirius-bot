import datetime
import json
import urllib.request


def time_converter(time):
	converted_time = datetime.datetime.fromtimestamp(
		int(time)
	).strftime('%I:%M %p')
	return converted_time


def url_builder(city_id,s = 1):
	searches = {1:"Name Search",2:"Zip Code",3:"Geo Coords"}
	#if s == 1:
	user_api = '03d5049ab587b7976c7c2e6caa57265f'  # Obtain yours form: http://openweathermap.org/
	unit = 'metric'  # For Fahrenheit use imperial, for Celsius use metric, and the default is Kelvin.
	api = 'http://api.openweathermap.org/data/2.5/forecast'
	if s == 1:
		api += "?q="
	elif s == 2:
		api += "?zip="
	
	full_api_url = api + str(city_id) + '&mode=json&units=' + unit + '&APPID=' + user_api
	return full_api_url


def data_fetch(full_api_url):
	try:
		url = urllib.request.urlopen(full_api_url)
		output = url.read().decode('utf-8')
		raw_api_dict = json.loads(output)
		url.close()
	except IOError:
		return -1
	return raw_api_dict


def data_organizer(raw_api_dict):
	if raw_api_dict == -1:
		return raw_api_dict
	else:
		returnList = []
		a = raw_api_dict.get('list')
		returnList.append(raw_api_dict.get('city').get('name'))
		for az in a:
			list_ = []
			aa = az['main']
			list_.append(datetime.datetime.fromtimestamp(int(az['dt'])).strftime('%d/%m/%Y %H:%M:%S'))
			list_.append(aa['temp_min'])
			list_.append(aa['temp_max'])
			list_.append(az['weather'][0]['main'] + " | " + az['weather'][0]['description'])
			returnList.append(list_)
			del list_
		return returnList


if __name__ == '__main__':
	try:
		print(data_organizer(data_fetch(url_builder(input("")))))
	except IOError:
		print('no internet')