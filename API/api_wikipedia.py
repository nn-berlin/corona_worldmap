from wikitables import import_tables
import pandas as pd


wiki_site = 'Liste_der_Staaten_der_Erde'
countrycode = 'de'
country_dict = {}

# getting tables from wiki-site
country_tables = import_tables(wiki_site, countrycode)

# fill dictionary with headers of first country_table
for i in country_tables[0].head:
    country_dict[i] = []

# fill data to dict
for j, k in country_dict.items():
    for row in country_tables[0].rows:
        k.append(row[j])

# create df
df = pd.DataFrame(country_dict)

# save raw data to .csv
df.to_csv('../data/countries_raw.csv')