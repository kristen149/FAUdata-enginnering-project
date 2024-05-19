# Python standard libraries
import json
import os
import zipfile
import requests
# Python downloaded libaries
import numpy as np
import pandas as pd
import sqlalchemy as sql
from io import StringIO
# Python get kaggle data
from kaggle.api.kaggle_api_extended import KaggleApi

# ===================USEFUL FUNCTION =====================
def extract_data_from_kaggle (url, destination_path = ''):
    # Initialize Kaggle API
    api = KaggleApi()
     # Extract dataset name from the URL
    parts = url.split('/datasets/')
    dataset_name = parts[-1]
    # Download dataset
    api.dataset_download_files(dataset_name, path=destination_path, unzip=True)
    
    # Read CSV file
    csv_file = [f for f in os.listdir(destination_path) if f.endswith('.csv')][0]
    csv_path = os.path.join(destination_path, csv_file)
    df = pd.read_csv(csv_path)
    
    # Return the DataFrame
    return df

def extract_csv_data (url):
    response = requests.get(url)
    if response.status_code == 200:
        # Load CSV data
        print(f"CSV file downloaded successfully.")
        csv_data = StringIO(response.content.decode('utf-8'))
        df = pd.read_csv(csv_data, encoding='latin1')
        return df
    else:
        print(f"Failed to retrieve data from {url}, {response.status_code}")
        return None
    
def create_sqlite_database(database_name):
    # Ensure the /data directory exists:
    data_directory = './data'   
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    # Construct the full database path
    database_path = os.path.join(data_directory, database_name)
    if os.path.exists(database_path):
        os.remove(database_path)  # Remove existing file
    engine = sql.create_engine(f'sqlite:///{database_path}')
    return engine
    

############################################################################

    
def main():
    
    # Data source 1: SEA_extreme_weather_events
    ## DATA EXTRACTION:
    url_events = "https://data.vietnam.opendevelopmentmekong.net/dataset/a6232bd8-c77e-40f7-ab1b-5fe824de52ce/resource/d1b3b83a-4312-44e7-806d-8f16bf83ed3a/download/disaster_south_eastern_asia_en.csv"
    sqlite_db_path = 'database.sqlite'
    df_events = extract_csv_data(url_events)
    # print(df_events.head())
    
    ## DATA TRANSFORMATION:
    ### 1. Country name attribute need to be consistent with corresponding attribute in data source 2
    df_events["Country"] = df_events["Country"].replace("Lao People's Democratic Republic (the)", "Lao People's DR")
    df_events["Country"] = df_events["Country"].replace("Philippines (the)", "Philippines")
    # print(df_events["Country"].unique())
    
    ### 2. Drop columns with missing values and high correlated
    df_events = df_events.drop(['Order', # not relevant
                                'Dis No',
                                'Glide', 
                                'Disaster Subsubtype', 
                                'Continent',
                                'Region', # not informative, people know the data limited to Southeast Asian countries
                                'Associated Dis2', # too many missing values 
                                'OFDA Response', # not relevant
                                "Reconstruction Costs ('000 US$)", # too many missing values 
                                "Reconstruction Costs, Adjusted ('000 US$)", # too many missing values 
                                'River Basin',
                                'Start Year',
                                'Start Month',
                                'Start Day',
                                'End Year',
                                'End Month',
                                'End Day',
                                "Insured Damages ('000 US$)", # too many missing values
                                "Insured Damages, Adjusted ('000 US$)",
                                "Total Damages, Adjusted ('000 US$)",
                                'Adm Level', 
                                'Admin1 Code', 
                                'Admin2 Code', 
                                'Latitude',
                                'Longitude'], axis=1)
    
    ### 3. Change columns name
    if 'ISO' in df_events.columns:
        df_events.rename(columns={'ISO': 'Country Code'}, inplace= True)
    ## print(df_events.columns)
    
    ## DATA IMPUTATION
    df_events['No Injured'].interpolate(method='linear', inplace = True)
    df_events['No Injured'].fillna(method='bfill', inplace=True)
    df_events['No Affected'].interpolate(method='linear', inplace = True)
    df_events['No Affected'].fillna(method='bfill', inplace=True)
    df_events['No Homeless'].interpolate(method='linear', inplace = True)
    df_events['No Homeless'].fillna(method='bfill', inplace=True)
    df_events['Total Affected'].interpolate(method='linear', inplace = True)
    df_events['Total Affected'].fillna(method='bfill', inplace=True)
    df_events['CPI'].interpolate(method='linear', inplace = True)
    df_events["Total Damages ('000 US$)"].interpolate(method='linear', inplace = True)
    df_events["Total Damages ('000 US$)"].fillna(method='bfill', inplace=True)


    ## DATA LOADING:
    engine = create_sqlite_database(sqlite_db_path)
    df_events.to_sql('extreme_weather_events', con=engine, index=False)
    
    print('Data has been successfully written')
    
    # Data source 2: SEA_socioeconomics
    ## DATA EXTRACTION:
    url_socioeconomics = "https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank"
    data_directory = 'data'
    df_socioeconomics = extract_data_from_kaggle(url_socioeconomics, data_directory)
    ## DATA TRANSFORMATION:
    SEA_country = ["Thailand", "Vietnam", "Singapore", "Indonesia", "Malaysia", "Philippines", "Myanmar", "Cambodia", "Timor-Leste",
                             "Lao People's DR", "Brunei Darussalam"]
    SEA_country_code = ["THA", "VNM", "SGP", "IDN", "MYS", "PHL", "MMR", "KHM",  "TLS", "LAO", "BRN"]
    
    ### 1. Change columns name:
    #   'Country Name' => 'Country'
    if 'Country Name' in df_socioeconomics.columns:
        df_socioeconomics.rename(columns={'Country Name': 'Country'}, inplace= True)
    
    ## print(df_socioeconomics['Country'].unique())
    
    ### 2. Limit the dataset to only Southeast Asian countries
    df_SEA_socioeconomics =  df_socioeconomics[df_socioeconomics['Country Code'].isin(SEA_country_code)]
    ### 3. Drop Corruption column (because too many missing values)
    df_SEA_socioeconomics = df_SEA_socioeconomics.drop(["Corruption", 
                                                        "Region" # not so meaningful with one value
                                                        ], axis=1 )
    
    ## DATA IMPUTATION:
    df_SEA_socioeconomics['Prevelance of Undernourishment'].interpolate(method = 'linear', inplace = True)
    
    df_SEA_socioeconomics['Education Expenditure %'].interpolate(method='linear', inplace = True)
    df_SEA_socioeconomics['Education Expenditure %'].fillna(method='bfill', inplace=True)
    
    df_SEA_socioeconomics['Sanitation'].interpolate(method='linear', inplace = True)
    df_SEA_socioeconomics['Sanitation'].fillna(method='bfill', inplace=True)


    ## DATA LOADING:
    df_SEA_socioeconomics.to_sql('socioeconomics', con=engine, index=False)
    
    
    # Data source 3: SEA_disaster_risk
    ## DATA EXTRACTION:
    url_disaster_risk = "https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/3a2320fa-41b4-4dda-a847-3f397d865378/download/worldriskindex-trend.csv"
    df_disasater_risk = extract_csv_data(url_disaster_risk)
    
    ## DATA TRANSFORMATION:
    ### 1. Change columns name:
    # 'WRI.Country' => 'Country'
    df_disasater_risk.rename(columns={'WRI.Country': 'Country'}, inplace= True)
    # 'ISO3.Code' => 'Country Code'
    df_disasater_risk.rename(columns={'ISO3.Code': 'Country Code'}, inplace= True)
    # 'W' => 'World Risk Index'
    df_disasater_risk.rename(columns={'W': 'World Risk Index'}, inplace= True)
    # 'E' => 'Exposure'
    df_disasater_risk.rename(columns={'E': 'Exposure'}, inplace= True)
    # 'V' => 'Vulnerability'
    df_disasater_risk.rename(columns={'V': 'Vulnerability'}, inplace= True)
    # 'S' => 'Susceptibility'
    df_disasater_risk.rename(columns={'S': 'Susceptibility'}, inplace= True)
    # 'C' => 'Lack of Coping Capabilities'
    df_disasater_risk.rename(columns={'C': 'Lack of Coping Capabilities'}, inplace= True)
    # 'A' => 'Lack of Adaptive Capabilities'
    df_disasater_risk.rename(columns={'A': 'Lack of Adaptive Capabilities'}, inplace= True)


    ### 2. Drop unnecessary columns:
    df_disasater_risk = df_disasater_risk.drop([ "S_01","S_02","S_03","S_04","S_05","C_01","C_02","C_03","A_01","A_02","A_03","EI_01","EI_02","EI_03","EI_04","EI_05","EI_06","EI_07","SI_01","SI_02","SI_03","SI_04","SI_05","SI_06","SI_07","SI_08","SI_09","SI_10","SI_11","SI_12","SI_13","SI_14","CI_01","CI_02","CI_03","CI_04","CI_05","CI_06","CI_07","AI_01","AI_02","AI_03","AI_04","EI_01a_Norm","EI_01a_Base","EI_01b_Norm","EI_01b_Base","EI_01c_Norm","EI_01c_Base","EI_01d_Norm","EI_01d_Base","EI_01e_Norm","EI_01e_Base","EI_01f_Norm","EI_01f_Base","EI_02a_Norm","EI_02a_Base","EI_02b_Norm","EI_02b_Base","EI_02c_Norm","EI_02c_Base","EI_02d_Norm","EI_02d_Base","EI_02e_Norm","EI_02e_Base","EI_02f_Norm","EI_02f_Base","EI_03a_Norm","EI_03a_Base","EI_03b_Norm","EI_03b_Base","EI_03c_Norm","EI_03c_Base","EI_03d_Norm","EI_03d_Base","EI_03e_Norm","EI_03e_Base","EI_03f_Norm","EI_03f_Base","EI_04a_Norm","EI_04a_Base","EI_04b_Norm","EI_04b_Base","EI_04c_Norm","EI_04c_Base","EI_04d_Norm","EI_04d_Base","EI_04e_Norm","EI_04e_Base","EI_04f_Norm","EI_04f_Base","EI_05a_Norm","EI_05a_Base","EI_05b_Norm","EI_05b_Base","EI_05c_Norm","EI_05c_Base","EI_05d_Norm","EI_05d_Base","EI_05e_Norm","EI_05e_Base","EI_05f_Norm","EI_05f_Base","EI_06a_Norm","EI_06a_Base","EI_06b_Norm","EI_06b_Base","EI_06c_Norm","EI_06c_Base","EI_06d_Norm","EI_06d_Base","EI_06e_Norm","EI_06e_Base","EI_06f_Norm","EI_06f_Base","EI_07a_Norm","EI_07a_Base","EI_07b_Norm","EI_07b_Base","SI_01a_Norm","SI_01a_Base","SI_01b_Norm","SI_01b_Base","SI_02a_Norm","SI_02a_Base","SI_02b_Norm","SI_02b_Base","SI_03a_Norm","SI_03a_Base","SI_03b_Norm","SI_03b_Base","SI_04a_Norm","SI_04a_Base","SI_04b_Norm","SI_04b_Base","SI_05a_Norm","SI_05a_Base","SI_05b_Norm","SI_05b_Base","SI_06a_Norm","SI_06a_Base","SI_06b_Norm","SI_06b_Base","SI_07a_Norm","SI_07a_Base","SI_07b_Norm","SI_07b_Base","SI_08a_Norm","SI_08a_Base","SI_08b_Norm","SI_08b_Base","SI_09a_Norm","SI_09a_Base","SI_09b_Norm","SI_09b_Base","SI_10_Norm","SI_10_Base","SI_10a_Norm","SI_10a_Base","SI_10b_Norm","SI_10b_Base","SI_11_Norm","SI_11_Base","SI_12a_Norm","SI_12a_Base","SI_12b_Norm","SI_12b_Base","SI_13a_Norm","SI_13a_Base","SI_13b_Norm","SI_13b_Base","SI_14a_Norm","SI_14a_Base","SI_14b_Norm","SI_14b_Base","SI_15a_Norm","SI_15a_Base","SI_15b_Norm","SI_15b_Base","SI_15c_Norm","SI_15c_Base","SI_15d_Norm","SI_15d_Base","CI_01a_Norm","CI_01a_Base","CI_01b_Norm","CI_01b_Base","CI_02a_Norm","CI_02a_Base","CI_02b_Norm","CI_02b_Base","CI_03a_Norm","CI_03a_Base","CI_03b_Norm","CI_03b_Base","CI_04a_Norm","CI_04a_Base","CI_04b_Norm","CI_04b_Base","CI_05a_Norm","CI_05a_Base","CI_05b_Norm","CI_05b_Base","CI_06a_Norm","CI_06a_Base","CI_06b_Norm","CI_06b_Base","CI_07a_Norm","CI_07a_Base","CI_07b_Norm","CI_07b_Base","AI_01a_Norm","AI_01a_Base","AI_01b_Norm","AI_01b_Base","AI_01c_Norm","AI_01c_Base","AI_02a_Norm","AI_02a_Base","AI_02b_Norm","AI_02b_Base","AI_02c_Norm","AI_02c_Base","AI_03a_Norm","AI_03a_Base","AI_03b_Norm","AI_03b_Base","AI_03c_Norm","AI_03c_Base","AI_04a_Norm","AI_04a_Base","AI_04b_Norm","AI_04b_Base","AI_04c_Norm","AI_04c_Base","AI_05a_Norm","AI_05a_Base","AI_05b_Norm","AI_05b_Base"], axis=1)
    

    ### 3. Limit the dataset to only Southeast Asian countries
    df_disasater_risk =  df_disasater_risk[df_disasater_risk['Country Code'].isin(SEA_country_code)]
    
    ## DATA LOADING 
    df_disasater_risk.to_sql('disaster_risk', con=engine, index=False)
    

    


if __name__ == "__main__":
    main()

    