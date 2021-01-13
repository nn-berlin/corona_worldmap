import requests
from datetime import datetime as dt


URL = 'https://api.covid19api.com/summary'

def download_data(url = URL):
	download_ts = dt.now()
	return requests.get(url).json(), download_ts
