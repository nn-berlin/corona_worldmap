from db_credentials import db_engine


engine = db_engine()

engine.execute("""
CREATE TABLE IF NOT EXISTS daily_summary 
    (
        country VARCHAR(128),
        countrycode VARCHAR(2),
        slug VARCHAR(128),
        new_confirmed INTEGER,
        total_confirmed INTEGER,
        new_deaths INTEGER,
        total_deaths INTEGER,
        new_recovered INTEGER,
        total_recovered INTEGER,
        summary_ts TIMESTAMP,
        download_ts TIMESTAMP,
        CONSTRAINT fk_countries FOREIGN KEY (countrycode) REFERENCES countries(ISO2)
    );
""")
