from DB.db_credentials import db_engine
import pandas as pd


engine = db_engine()

def to_DB(df):
    for row in range(len(df)):
        engine.execute(" \
            INSERT INTO daily_summary \
            (country, \
            countrycode, \
            slug, \
            new_confirmed, \
            total_confirmed, \
            new_deaths, \
            total_deaths, \
            new_recovered, \
            total_recovered, \
            summary_ts, \
            download_ts) \
            VALUES \
            ( \
            '"+str(df.loc[row, 'country'])+"', \
            '"+str(df.loc[row, 'countrycode'])+"', \
            '"+str(df.loc[row, 'slug'])+"', \
            '"+str(df.loc[row, 'new_confirmed'])+"', \
            '"+str(df.loc[row, 'total_confirmed'])+"', \
            '"+str(df.loc[row, 'new_deaths'])+"', \
            '"+str(df.loc[row, 'total_deaths'])+"', \
            '"+str(df.loc[row, 'new_recovered'])+"', \
            '"+str(df.loc[row, 'total_recovered'])+"', \
            '"+str(df.loc[row, 'summary_ts'])+"', \
            '"+str(df.loc[row, 'download_ts'])+"' \
            ); \
            ")

def old_files_to_DB(df):
    for row in range(len(df)):
        engine.execute(" \
            INSERT INTO daily_summary \
            (country, \
            countrycode, \
            slug, \
            new_confirmed, \
            total_confirmed, \
            new_deaths, \
            total_deaths, \
            new_recovered, \
            total_recovered, \
            summary_ts) \
            VALUES \
            ( \
            '"+str(df.loc[row, 'country'])+"', \
            '"+str(df.loc[row, 'countrycode'])+"', \
            '"+str(df.loc[row, 'slug'])+"', \
            '"+str(df.loc[row, 'new_confirmed'])+"', \
            '"+str(df.loc[row, 'total_confirmed'])+"', \
            '"+str(df.loc[row, 'new_deaths'])+"', \
            '"+str(df.loc[row, 'total_deaths'])+"', \
            '"+str(df.loc[row, 'new_recovered'])+"', \
            '"+str(df.loc[row, 'total_recovered'])+"', \
            '"+str(df.loc[row, 'summary_ts'])+"' \
            ); \
            ")