from datetime import datetime as dt
import json
import pandas as pd

def to_file(data, download_ts, path, kind_of_file = 'summary'):
	ts = download_ts.strftime('%Y%m%d')
	if isinstance(data, dict):
		filetype = '.txt'
		filename = ts + '_' + kind_of_file + filetype
		with open(path + filename, 'w') as write:
			json.dump(data, write)
	elif isinstance(data, pd.DataFrame):
		filetype = '.csv'
		filename = ts + '_' + kind_of_file + filetype
		data.to_csv(path + filename)
	else:
		print('Wrong data type, data not stored!')
	return filename
