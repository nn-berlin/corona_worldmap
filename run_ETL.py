from API.api_covid19api import download_data
from datamanagement.transform_data import to_transform
from filemanagement.save_data import to_file
from filemanagement.s3_interaction import s3_upload
from DB.fill_tb_dailysummary import to_DB


# fetch data of covid19api.com
data, ts = download_data()

# save raw data (structure dict) to data-folder
path = '/home/ec2-user/corona_worldmap/data/'
kind = 'raw'
filename = to_file(data, ts, path, kind)

# upload to s3-bucket
bucket = 'berlincoronabucket'
#s3_upload(path + filename, bucket, filename)

# transform data (dict -> dataframe)
df = to_transform(data, ts)

# fill DB-table daily_summary
to_DB(df)

