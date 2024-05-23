# Project Plan

<!-- Give your project a short title. -->
### Assessing the impacts of extreme weather events on the Socioeconomics - A case study in Southeast Asia region
The objective of this data science project is analyzing the impact of extreme weather events on the socioeconomic trends of Southeast Asia.

One of the most visible consequences of climate change is the increase in frequency and intensity of extreme weather events, typically typhoons, earthquake, droughts, and floods. By examining historical data, the project aims to uncover patterns and correlations between extreme weather events and socioeconomic indicators as life expectancy, unemployment, corruption, sanitation, health expenditure, infrastructure damage etc. 

## Description: Reason for targeting on Southeast Asia

Southeast Asia is nowadays a development and economic success story. However, Southeast Asia is one of the world’s regions most vulnerable to climate change impacts with low-lying land, more severe floods and droughts, larger populations, higher dependency on agriculture for the economic sector, and low resilience of communities [[ref]][1]. Countries as the Philippines, Vietnam, Indonesia, and Thailand have experienced some of the most extreme weather events globally. Therefore, a study on how future climate change will affect the economy in this region has been conducted. The results are provided in this data science project.

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->

## Main Question
<!-- Think about one main question you want to answer based on the data. -->

Some key questions will be answered by this project:
1. What are the patterns in the occurrence of extreme weather events and the socioeconomic status of Southeast Asian countries?
2. How do extreme weather events impact the socioeconomic status of Southeast Asian countries?

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource 1: Southeast Asian Extreme Weather Events
* Metadata URL: https://data.opendevelopmentmekong.net/dataset/disaster-in-southeast-asia-from-1900-to-2021
* Data URL: https://data.vietnam.opendevelopmentmekong.net/dataset/a6232bd8-c77e-40f7-ab1b-5fe824de52ce/resource/d1b3b83a-4312-44e7-806d-8f16bf83ed3a/download/disaster_south_eastern_asia_en.csv

* Data Type: CSV

* License: [CC BY-SA 3.0 DEED License](https://creativecommons.org/licenses/by-sa/3.0/)

#### Data overview:
From 1909 to 2021, 2737 extreme weather events have been recorded. 
The dataset consists of 53 regular attributes to these events, as sequence number, disaster coding code, year, disaster group, disaster type group, disaster type, event name, water, country, location, longitude, latitude, local time, start date, end date, total number of deaths, total losses...

Among the 53 regular attributes in the dataset, the most important ones were chosen for this data science project as follows:
1. Year: The year the disaster occurred
2. Disaster Group: Category of the disaster (ex. natural or technological)
3. Disaster Subgroup: More specific category within the main disaster group (ex. geophysical, biological, meteoroligical...)
4. Disaster Type: Specific type of disaster (ex. epidemic, drought, flood, storm...)
5. Disaster Subtype: Further type of disaster (ex. drought, tsunami, landslide...)
6. Event Name: Name of the disaster event (ex. Winnie, MD-82, Dengue...)
7. Country: Country where the disaster occurred (ex. 11 countries including Singapore, Thailand, Vietnam...)
8. ISO: The country code (ex. Indonesia - IDN, Philippines - PHL, Thailand - THA...)
9. Location: General location affected by the disaster (values are not consistent, range from country, state, province, city...)
10. Origin: Reason for the disaster (ex. heavy rains, storm, overpassing....).
11. Associated Dis: Related disaster events (ex. rain, pollution, oil spill, cold wave...)
12. Appeal: International appeals for assistance (values are either yes, no, or NULL)
13. Declaration: Declarations made regarding the disaster (values are either yes, no, or NULL)
14. Aid Contribution: Amount of aid contributed (US dollars) regarding the disaster
15. Dis Mag Value: Numerical value measuring the magnitude of the disaster
16. Dis Mag Scale: Scale measuring the disaster’s magnitude, such as KPH, Richter, m3, Km2... 
17. Local Time: Local time when the disaster occurred
18. Total Deaths: Total number of deaths caused by the disaster
19. No Injured: Number of individuals injured due to the disaster
20. No Affected: Number of individuals affected due to the disaster
21. No Homeless: Number of individuals rendered homeless due to the disaster
22. Total Affected: Total of injured, affected, and homeless individuals
23. Insured Damages (‘000 US$): Estimated damages in thousands of US dollars covered by insurance
24. Total Damages (‘000 US$): Total estimated damages in thousands of US dollars due to the disaster
25. CPI: Consumer Price Index at the time of the disaster
26. Geo Locations: Specific location affected by the disaster



### Datasource 2: Southeast Asian Socioeconomics
* Metadata URL: https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank
* Data URL: https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank
* Data Type: CSV
* License: [World Bank Dataset Terms of Use](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets)

#### Data overview:
The dataset includes 19 years data of multiple countries with the following attributes:
1. Country - 174 countries
2. Country Code - 3-letter code
3. Region - region of the world country is located in
4. IncomeGroup - country's income class
5. Year (2000-2019)
6. Life expectancy: the average number of years a person is expected to live, based on current mortality rates
7. Prevalence of Undernourishment (% of the population): refers to the percentage of a population that does not have enough dietary energy intake to meet the minimum requirements for a healthy and active life 
8. Carbon dioxide emissions (kiloton): a mesure of the amount of CO2 released into the atmosphere, from fossil fuels, industrial processes...
9. Health Expenditure (% of GDP)
10. Education Expenditure (% of GDP)
11. Unemployment (% total labor force)
12. Corruption (CPIA rating)
13. Sanitation 
14. Disability-Adjusted Life Years (DALYs) due to Injuries
15. Disability-Adjusted Life Years (DALYs) due to Communicable diseases
16. Disability-Adjusted Life Years (DALYs) due to Non-Communicable diseases


### Datasource 3: Southeast Asian Disaster Risk
* Metadata URL: https://data.humdata.org/dataset/worldriskindex?
* Data URL: https://data.humdata.org/dataset/1efb6ee7-051a-440f-a2cf-e652fecccf73/resource/3a2320fa-41b4-4dda-a847-3f397d865378/download/worldriskindex-trend.csv
* Data Type: CSV
* License: [Creative Commons Attribution International](https://data.humdata.org/faqs/licenses)

#### Data overview:
 The dataset conceptually combines the exposure to extreme weather events with the societal vulnerability of individual countries. The exposure analysis takes into account earthquakes, cyclones, floods, droughts, and climate-induced sea-level rise. Societal vulnerability is divided into susceptibility to extreme natural events, lack of coping capacities, and lack of adaptive capacities. All components of the index are scaled from 0 to 100. A higher score on the WorldRiskIndex signifies a greater national disaster risk.


The dataset includes 11 years data of multiple countries with the following attributes:
1. Region: Name of the region 
2. WRI: World Risk Index measures a country's risk of disaster from extreme weather events. It combines indicators of exposure to extreme weather events (earthquakes, storms, floods, droughts...)    
3. Exposure: refers to the extent to which a country or region is physically exposed to extreme weather events (earthquakes, storms, floods, droughts...)
4. Vulnerability: refers to the susceptibility of a country to adverse impacts from extreme weather events, depending on infrastructure, nutrition, housing situation, economic, and the ability to recover from disasters
5. Susceptibility: refers to the likelihood of harm a country faces from extreme weather events, depending on infrastructure, nutrition, housing situation, economic, and the ability to recover from disasters
6. Lack of Coping Capabilities: refers to the immediate ability of a country to manage and respond to extreme weather events
7. Lack of Adaptive Capabilities: refers to the long-term ability of a country to adjust to and recover from extreme weather events
8. Year (2011-2021): Year data is being recorded
9. Exposure Category: Ordinal Measurement - Very High, High, Medium, Low, Very Low
10. Vulnerability Category: Ordinal Measurement - Very High, High, Medium, Low, Very Low
11. Susceptibility Category: Ordinal Measurement - Very High, High, Medium, Low, Very Low


### ETL Pipeline:
``` mermaid
flowchart TB
  
  A[Dataset 1:
    SEA_extreme_weather_events] --data.opendevelopmentmekong.net--> SUB0 --Sqlite database with 3 tables--> db1[("database.sqlite
     Table 1. extreme_weather_events
     Table 2. socioeconomics
     Table 3. disaster_risk")] --> G[Analytics and Reporting] 
  B[Dataset 2:
    SEA_socioeconomics] --kaggle.com --> SUB0 
  C[Dataset 3:
    SEA_disaster_risk] --data.humdata.org --> SUB0


subgraph SUB0[ETL Pipeline: pipeline.py]
    direction LR
    D(Extract)----> E(Transform)----> F(Load)
end
```
## Limitation on the datasets:
Many of the features have many missing/incomplete data, with seven columns in particular having > 90% of the features missing.
The timeline in datasets can also be inconsistent and non-standardized, particularly when it comes of the location of where a natural disaster occurred.
## Conclusion

The findings reveals that Southeast Asian countries are vulnerable to climate-related disasters.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Searching for meaningful dataset [#1][i1]
2. Writing project plan and overview [#2]
3. Building ETL Pipeline for the datasets [#3]
4. Analyzing patterns and training predictive models [#4]
5. Building CI pipeline [#4]
6. Drawing conclusion, suggesting for further research [#6]

[i1]: https://github.com/jvalue/made-template/issues/1

## References

[1]: https://www.usaid.gov/asia-regional/fact-sheets/confronting-climate-crisis-southeast-asia-regional-approach
1. https://www.usaid.gov/asia-regional/fact-sheets/confronting-climate-crisis-southeast-asia-regional-approach
