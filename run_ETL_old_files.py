import os
import pandas as pd
from datamanagement.transform_data import old_files_to_transform
from DB.fill_tb_dailysummary import old_files_to_DB


path = '/home/ec2-user/corona_2punkt0/data/summary/'
files = os.listdir(path)

for i in files:
    data = pd.read_csv(path + i)
    df = old_files_to_transform(data)
    old_files_to_DB(df)

