from db_credentials import db_engine


engine = db_engine()

engine.execute("""
    CREATE TABLE IF NOT EXISTS countries 
        (
        ISO2 VARCHAR(2) PRIMARY KEY,
        country VARCHAR(128),
        population2017 INTEGER,
        ISO3 VARCHAR(3)
        );
""")
