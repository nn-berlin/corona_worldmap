import pandas as pd
from datetime import datetime as dt


def to_transform(data, download_ts):
    summary = data['Countries']
    df = pd.DataFrame(summary)
    df['Date'] = df['Date'].map(lambda x: dt.strptime(x, '%Y-%m-%dT%H:%M:%SZ').strftime('%m-%d-%Y %H:%M:%S'))
    df['Country'] = df['Country'].apply(lambda x: x.replace("'", ''))
    df.loc[df[df.Country == 'Namibia'].index,'CountryCode'] = 'NA'
    df = df[df['CountryCode'] != 'RE']
    df = df[df['CountryCode'] != 'MO']
    df = df.reset_index(drop = True)
    df['download_ts'] = download_ts.strftime('%m-%d-%Y %H:%M:%S')
    df = df.rename(columns={"Country": "country", 
                            "CountryCode": "countrycode",
                            'Slug': 'slug', 
                            'NewConfirmed': 'new_confirmed',
                            'TotalConfirmed': 'total_confirmed',
                            'NewDeaths': 'new_deaths',
                            'TotalDeaths': 'total_deaths',
                            'NewRecovered': 'new_recovered',
                            'TotalRecovered': 'total_recovered',
                            'Date': 'summary_ts'
                            })
    df.drop(['Premium'], axis=1, inplace=True)
    return df
