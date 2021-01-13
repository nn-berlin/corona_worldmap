from db_credentials import db_engine
import pandas as pd


engine = db_engine()
path = './../data/countries.csv'

df = pd.read_csv(path, index_col=False)
df.loc[df[df.country == 'Namibia'].index,'ISO2'] = 'NA'

for row in range(len(df)):
    engine.execute("INSERT INTO countries \
    (ISO2, country, population2017, ISO3) VALUES \
    ('"+str(df.loc[row, 'ISO2'])+"', \
    '"+str(df.loc[row, 'country'])+"', \
    '"+str(df.loc[row, 'population2017'])+"', \
    '"+str(df.loc[row, 'ISO3'])+"');")


    # ISO2 VARCHAR(2) PRIMARY KEY,
    # country VARCHAR(128),
    # population2017 INTEGER,
    # ISO3 VARCHAR(3)