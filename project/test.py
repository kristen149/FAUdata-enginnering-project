import os
import pandas as pd
import sqlalchemy as sql
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
        columns = df['name'].tolist()
        expected_columns = ['Year', 'Seq', 'Disaster Group', 'Disaster Subgroup', 'Disaster Type', 'Disaster Subtype', 'Event Name', 'Country', 'Country Code', 'Location', 'Origin', 'Associated Dis', 'Appeal', 'Declaration', 'Aid Contribution', 'Dis Mag Value', 'Dis Mag Scale', 'Local Time', 'Total Deaths', 'No Injured', 'No Affected', 'No Homeless', 'Total Affected', "Total Damages ('000 US$)", 'CPI', 'Geo Locations']
        assert set(columns) == set(expected_columns), f"Columns in extreme_weather_events do not match: {columns}"

        # Check data integrity for extreme_weather_events
        result = conn.execute("SELECT COUNT(*) FROM extreme_weather_events WHERE 'No Injured' IS NULL").fetchone()
        assert result[0] == 0, "There are NULL values in No Injured column"

        # Check column names for socioeconomics
        df = pd.read_sql_query("PRAGMA table_info(socioeconomics)", conn)
        columns = df['name'].tolist()
        expected_columns = ['Country', 'Country Code', 'IncomeGroup', 'Year', 'Life Expectancy World Bank', 'Prevelance of Undernourishment', 'CO2', 'Health Expenditure %', 'Education Expenditure %', 'Unemployment', 'Sanitation', 'Injuries', 'Communicable', 'NonCommunicable']
        assert set(columns) == set(expected_columns), f"Columns in socioeconomics do not match: {columns}"

        # Check data integrity for socioeconomics
        result = conn.execute("SELECT COUNT(*) FROM socioeconomics WHERE 'Education Expenditure %' IS NULL").fetchone()
        assert result[0] == 0, "There are NULL values in Education Expenditure % column"

        # Check column names for disaster_risk
        df = pd.read_sql_query("PRAGMA table_info(disaster_risk)", conn)
        columns = df['name'].tolist()
        expected_columns = ['Country', 'Country Code', 'Year', 'World Risk Index', 'Exposure', 'Vulnerability', 
                            'Susceptibility', 'Lack of Coping Capabilities', 'Lack of Adaptive Capabilities']
        assert set(columns) == set(expected_columns), f"Columns in disaster_risk do not match: {columns}"

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
