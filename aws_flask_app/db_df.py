from db_credentials import db_engine
import pandas as pd
import numpy


def get_df():
    engine = db_engine()
    query = '''
        SELECT 
        daily_summary.country as "Country",
        countries.iso3 as "ISO3", 
        DATE(daily_summary.summary_ts) as "Date", 
        daily_summary.new_confirmed AS "New Confirmed", 
        daily_summary.total_confirmed AS "Total Confirmed", 
        daily_summary.new_deaths AS "New Deaths", 
        daily_summary.total_deaths AS "Total Deaths", 
        daily_summary.new_recovered AS "New Recovered", 
        daily_summary.total_recovered AS "Total Recovered", 

        ROUND(100000 * CAST(daily_summary.new_confirmed AS DECIMAL) / countries.population2017) AS "New Confirmed p100000", 
        ROUND(100000 * CAST(daily_summary.total_confirmed AS DECIMAL) / countries.population2017) AS "Total Confirmed p100000", 
        ROUND(100000 * CAST(daily_summary.new_deaths AS DECIMAL) / countries.population2017) AS "New Deaths p100000", 
        ROUND(100000 * CAST(daily_summary.total_deaths AS DECIMAL) / countries.population2017) AS "Total Deaths p100000", 
        ROUND(100000 * CAST(daily_summary.new_recovered AS DECIMAL) / countries.population2017) AS "New Recovered p100000", 
        ROUND(100000 * CAST(daily_summary.total_recovered AS DECIMAL) / countries.population2017) AS "Total Recovered p100000" 

        FROM daily_summary INNER JOIN countries 
        ON daily_summary.countrycode = countries.iso2 
        WHERE summary_ts IN (SELECT summary_ts FROM daily_summary GROUP BY summary_ts ORDER BY summary_ts DESC LIMIT 7)
    '''
    df = pd.read_sql(query, engine)
    df['Date'] = df['Date'].apply(lambda x: x.strftime('%Y.%m.%d'))
    dates = list(set(df['Date']))
    dates.sort()
    global datelist
    global datesdict
    global df_absolut
    global df_p100000
    datelist = []
    datesdict = {}
    for s,t in zip(dates, range(len(dates))):
        datesdict[t] = s
        datedict = {}
        datedict['label'] = s
        datedict['value'] = s
        datelist.append(datedict)
    df_absolut = df[['Country', 
                    'ISO3', 
                    'Date', 
                    'New Confirmed', 
                    'Total Confirmed', 
                    'New Deaths', 
                    'Total Deaths', 
                    'New Recovered', 
                    'Total Recovered']]
    df_p100000 = df[['Country', 
                    'ISO3', 
                    'Date', 
                    'New Confirmed p100000', 
                    'Total Confirmed p100000', 
                    'New Deaths p100000', 
                    'Total Deaths p100000', 
                    'New Recovered p100000', 
                    'Total Recovered p100000']]
    df_p100000 = df_p100000.rename(columns={
                            'New Confirmed p100000': 'New Confirmed', 
                            'Total Confirmed p100000': 'Total Confirmed', 
                            'New Deaths p100000': 'New Deaths', 
                            'Total Deaths p100000': 'Total Deaths', 
                            'New Recovered p100000': 'New Recovered', 
                            'Total Recovered p100000': 'Total Recovered'
                            })

    integer_columns = []
    for l in list(df_absolut.columns):
        if isinstance(df_absolut.loc[0, l], numpy.int64):
            integer_columns.append(l)

    # creating list of dicts for dropdown
    columnlist = []
    for s in integer_columns:
        coldict = {}
        coldict['label'] = s
        coldict['value'] = s
        columnlist.append(coldict)
    return df, dates, datelist, datesdict, df_absolut, df_p100000, integer_columns, columnlist