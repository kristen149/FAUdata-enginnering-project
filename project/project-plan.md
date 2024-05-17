# Project Plan

<!-- Give your project a short title. -->
### Assessing the impacts of extreme weather events on the Socio-economics - A case study in Southeast Asia region
The objective of this data science project is analyzing the impact of extreme weather events on the economic trends of Southeast Asia from 1970 to 2021.

One of the most visible consequences of climate change is the increase in frequency and intensity of extreme weather events, typically typhoons, earthquake, droughts, and floods. By examining historical data, the project aims to uncover patterns and correlations between extreme weather events and economic indicators like GDP growth, agricultural output, and infrastructure damage. 

## Description: Reason for choosing Southeast Asia

Southeast Asia is nowadays a development and economic success story.

"Southeast Asia is one of the world’s regions most vulnerable to climate change impacts with low-lying land, more severe floods and droughts, larger populations, higher dependency on agriculture for the economic sector, and low resilience of communities."  https://www.usaid.gov/asia-regional/fact-sheets/confronting-climate-crisis-southeast-asia-regional-approach

 Therefore, a study on how future climate change will affect the economy in this region has been conducted. The results are provided in this data science project.

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->

## Main Question
<!-- Think about one main question you want to answer based on the data. -->

Some key questions will be answered by this project:
1. What are the patterns in the occurrence of extreme weather events and the socioeconomic status of Southeast Asian countries?
2. How do extreme weather events impact the socioeconomic status of Southeast Asian countries?
3. How can predictive analysis be employed to forecast the economic consequences of forthcoming extreme weather occurrences on Southeast Asian countries?

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Southeast Asian Extreme Weather Events
* Metadata URL: https://data.opendevelopmentmekong.net/dataset/disaster-in-southeast-asia-from-1900-to-2021
* Data URL: https://data.vietnam.opendevelopmentmekong.net/dataset/a6232bd8-c77e-40f7-ab1b-5fe824de52ce/resource/d1b3b83a-4312-44e7-806d-8f16bf83ed3a/download/disaster_south_eastern_asia_en.csv

* Data Type: CSV

License: [CC BY-SA 3.0 DEED License](https://creativecommons.org/licenses/by-sa/3.0/)

Overview:
From 1909 to 2021, 2737 extreme weather events have been recorded. 

The dataset consists of 53 regular attributes to these events, as sequence number, disaster coding code, year, disaster group, disaster type group, disaster type, event name, water, country, location, longitude, latitude, local time, start date, end date, total number of deaths, total losses...


### Datasource2: Southeast Asian Socioeconomics
* Metadata URL: https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank
* Data URL: https://www.kaggle.com/datasets/mjshri23/life-expectancy-and-socio-economic-world-bank
* Data Type: CSV
* License: [World Bank Dataset Terms of Use](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets)

The dataset includes 19 years data of multiple countries with the following features:
1. Country - 174 countries
2. Country Code - 3-letter code
3. Region - region of the world country is located in
4. IncomeGroup - country's income class
5. Year (2000-2019)
6. Life expectancy
7. Prevalence of Undernourishment (% of the population) 
8. Carbon dioxide emissions (kiloton)
9. Health Expenditure (% of GDP)
10. Education Expenditure (% of GDP)
11. Unemployment (% total labor force)
12. Corruption (CPIA rating)
13. Sanitation 
14. Disability-Adjusted Life Years (DALYs) due to Injuries
15. Disability-Adjusted Life Years (DALYs) due to Communicable diseases
16. Disability-Adjusted Life Years (DALYs) due to Non-Communicable diseases


### Datasource3: Southeast Asian Disaster Risk
* Metadata URL: https://www.kaggle.com/datasets/tr1gg3rtrash/global-disaster-risk-index-time-series-dataset
* Data URL: https://www.kaggle.com/datasets/tr1gg3rtrash/global-disaster-risk-index-time-series-dataset
* Data Type: CSV
* License: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

 Description:
 The dataset conceptually combines the exposure to extreme natural hazards with the societal vulnerability of individual countries. The exposure analysis takes into account earthquakes, cyclones, floods, droughts, and climate-induced sea-level rise. Societal vulnerability is divided into susceptibility to extreme natural events, lack of coping capacities, and lack of adaptive capacities. All components of the index are scaled from 0 to 100. A higher score on the WorldRiskIndex signifies a greater national disaster risk.


| Number |      Feature Name            |      Description                             |
|--------|------------------------------|----------------------------------------------|
|   0    |  Region                      |  Name of the region                          |
|   1    |  WRI                         |  World Risk Score of the region              |
|   2    |  Exposure                    |  Risk/exposure to natural hazards such as earthquakes, hurricanes, floods, droughts, and sea ​​level rise                          |
|   3    |  Vulnerability               |  Vulnerability depending on infrastructure, nutrition, housing situation, and economic framework conditions                        |
|   4    |  Susceptibility              |  Susceptibility depending on infrastructure, nutrition, housing situation, and economic framework conditions                        |
|   5    |  Lack of Coping Capabilities |  Coping capacities in dependence of governance, preparedness and early warning, medical care, and social and material security                                                                               |
|   6    |  Year (2011-2021)            |  Adaptive capacities related to coming natural events, climate change, and other challenges                                           |
|   7    |  WRI Category                |  Year data is being described                |
|   8    |  Lack of Coping Capabilities |  WRI Category for the given WRI Score                                                                                  |
|   9    |  Exposure Category           |  Exposure Category for the given Exposure Score                                                                                  |
|   10   |  Vulnerability Categoy       |  Vulnerability Category for the given Vulnerability Score                                                                    |
|   11   |  Susceptibility Category     |  Susceptibility Category for the given Susceptibility Score                                                                   |

### ETL Pipeline:
``` mermaid
flowchart TB
  
  A[Dataset 1:
    SEA_extreme_weather_events.csv] --data.opendevelopmentmekong.net--> SUB0 --> db1[("Storage: weather_events.sqlite")] --> G[Reporting & Analytics] 
  B[Dataset 2:
    SEA_societal_indicators.csv] --kaggle.com --> SUB1 
  C[Dataset 3:
    SEA_disaster_risk.csv] --kaggle.com --> SUB1
  SUB1 --> db2[("Storage: socialeconomic_risk.sqlite")] --> G[Reporting & Analytics]

subgraph SUB1[ETL Pipeline: pipeline.py]
 direction LR
    I(Extract)----> K(Transform)---->L(Load)
end
subgraph SUB0[ETL Pipeline: pipeline.py]
    direction LR
    D(Extract)----> E(Transform)----> F(Load)
end
```
## Limitation on the datasets:
* Although Vietnam is a very fast developing country, its information was somehow missing in the economy dataset. Thus readers have no insight to this country. 

## Conclusion

The findings reveals that Southeast Asian countries are vulnerable to climate-related disasters.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Searching for meaningful dataset [#1][i1]
2. Writing project plan and overview [#2]
3. Building ETL Pipeline for the datasets [#3]
4. Analyzing patterns and training predictive models [#4]
5. Drawing conclusion, suggesting for further research [#5]

[i1]: https://github.com/jvalue/made-template/issues/1
