import os
import pandas as pd
import sqlite3

def test_pipeline(database_path):
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(__file__)
        # Construct the full path to the database file
        full_db_path = os.path.join(script_dir, database_path)

        # Connect to the SQLite database
        conn = sqlite3.connect(full_db_path)

        # Check if tables exist
        tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        tables = [table[0] for table in tables]

        assert 'extreme_weather_events' in tables, "Table extreme_weather_events does not exist"
        assert 'socioeconomics' in tables, "Table socioeconomics does not exist"
        assert 'disaster_risk' in tables, "Table disaster_risk does not exist"
        
        # Check column names for extreme_weather_events
        df = pd.read_sql_query("PRAGMA table_info(extreme_weather_events)", conn)
        columns = df[['name', 'type']].values.tolist()
        expected_columns = [
            ['Year', 'BIGINT'], ['Seq', 'BIGINT'], ['Disaster Group', 'TEXT'], 
            ['Disaster Subgroup', 'TEXT'], ['Disaster Type', 'TEXT'], ['Disaster Subtype', 'TEXT'], 
            ['Event Name', 'TEXT'], ['Country', 'TEXT'], ['Country Code', 'TEXT'], 
            ['Location', 'TEXT'], ['Origin', 'TEXT'], ['Associated Dis', 'TEXT'], 
            ['Appeal', 'TEXT'], ['Declaration', 'TEXT'], ['Aid Contribution', 'FLOAT'], 
            ['Dis Mag Value', 'FLOAT'], ['Dis Mag Scale', 'TEXT'], ['Local Time', 'TEXT'], 
            ['Total Deaths', 'FLOAT'], ['No Injured', 'FLOAT'], ['No Affected', 'FLOAT'], 
            ['No Homeless', 'FLOAT'], ['Total Affected', 'FLOAT'], 
            ["Total Damages ('000 US$)", 'FLOAT'], ['CPI', 'FLOAT'], ['Geo Locations', 'TEXT']
        ]
        assert columns == expected_columns, f"Columns and types in extreme_weather_events do not match: {columns}"


        # Check data integrity for extreme_weather_events
        result = conn.execute("SELECT COUNT(*) FROM extreme_weather_events WHERE 'No Injured' IS NULL").fetchone()
        assert result[0] == 0, "There are NULL values in No Injured column"


        # Check column names for socioeconomics
        df = pd.read_sql_query("PRAGMA table_info(socioeconomics)", conn)
        columns = df[['name', 'type']].values.tolist()
        expected_columns = [
            ['Country', 'TEXT'], ['Country Code', 'TEXT'], ['IncomeGroup', 'TEXT'], 
            ['Year', 'BIGINT'], ['Life Expectancy World Bank', 'FLOAT'], 
            ['Prevelance of Undernourishment', 'FLOAT'], ['CO2', 'FLOAT'], 
            ['Health Expenditure %', 'FLOAT'], ['Education Expenditure %', 'FLOAT'], 
            ['Unemployment', 'FLOAT'], ['Sanitation', 'FLOAT'], ['Injuries', 'FLOAT'], 
            ['Communicable', 'FLOAT'], ['NonCommunicable', 'FLOAT']
        ]
        assert columns == expected_columns, f"Columns and types in socioeconomics do not match: {columns}"

        # Check data integrity for socioeconomics
        result = conn.execute("SELECT COUNT(*) FROM socioeconomics WHERE 'Education Expenditure %' IS NULL").fetchone()
        assert result[0] == 0, "There are NULL values in Education Expenditure % column"

        # Check column names and datatype for disaster_risk
        df = pd.read_sql_query("PRAGMA table_info(disaster_risk)", conn)
        columns = df[['name', 'type']].values.tolist()
        expected_columns = [
            ['Country', 'TEXT'], ['Country Code', 'TEXT'], ['Year', 'BIGINT'], 
            ['World Risk Index', 'FLOAT'], ['Exposure', 'FLOAT'], ['Vulnerability', 'FLOAT'], 
            ['Susceptibility', 'FLOAT'], ['Lack of Coping Capabilities', 'FLOAT'], 
            ['Lack of Adaptive Capabilities', 'FLOAT']
        ]
        assert columns == expected_columns, f"Columns and types in disaster_risk do not match: {columns}"

        # Check data integrity for disaster_risk
        result = conn.execute("SELECT COUNT(*) FROM disaster_risk WHERE 'World Risk Index' IS NULL").fetchone()
        assert result[0] == 0, "There are NULL values in World Risk Index column"


        print("All tests passed successfully!")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        if conn:
            conn.close()

# Assuming database_path is the path to the SQLite database
test_pipeline('../data/database.sqlite')
