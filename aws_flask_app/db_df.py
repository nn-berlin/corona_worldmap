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
        ROUND(100000 * CAST(daily_summary.new_confirmed AS DECIMAL) / countries.population2017) AS "New Confirmed", 
        ROUND(100000 * CAST(daily_summary.total_confirmed AS DECIMAL) / countries.population2017) AS "Total Confirmed", 
        ROUND(100000 * CAST(daily_summary.new_deaths AS DECIMAL) / countries.population2017) AS "New Deaths", 
        ROUND(100000 * CAST(daily_summary.total_deaths AS DECIMAL) / countries.population2017) AS "Total Deaths", 
        ROUND(100000 * CAST(daily_summary.new_recovered AS DECIMAL) / countries.population2017) AS "New Recovered", 
        ROUND(100000 * CAST(daily_summary.total_recovered AS DECIMAL) / countries.population2017) AS "Total Recovered" 
        FROM daily_summary INNER JOIN countries 
        ON daily_summary.countrycode = countries.iso2 
        WHERE summary_ts IN (SELECT summary_ts FROM daily_summary GROUP BY summary_ts ORDER BY summary_ts DESC LIMIT 7)
    '''
    df = pd.read_sql(query, engine, index_col = ['Country', 'ISO3', 'Date'])

    df_absolut, df_p100000 = df.iloc[:, :6], df.iloc[:, 6:]
    df = pd.concat([df_absolut, df_p100000], axis=0, keys=['absolut', 'per100000'], names=['kind']).reset_index()

    df['Date'] = df['Date'].apply(lambda x: x.strftime('%Y.%m.%d'))

    dates = {k: l for k,l in enumerate(list(df['Date'].sort_values().unique()))}

    return df, dates