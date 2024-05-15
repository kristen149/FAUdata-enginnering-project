# Project Plan

## Title
<!-- Give your project a short title. -->
### Assessing Economic Resilience: The Impact of Extreme Weather Events on the South East Asian (ASEAN) Economy from 1970 to 2021
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
1. What are the patterns in the occurrence of extreme weather events and the economic status of Southeast Asian countries?
2. How do extreme weather events impact the economic trends of Southeast Asian countries?
3. How can predictive analysis be employed to forecast the economic consequences of forthcoming extreme weather occurrences on Southeast Asian countries?

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Southeast Asia Extreme Weather Events
* Metadata URL: https://data.opendevelopmentmekong.net/dataset/disaster-in-southeast-asia-from-1900-to-2021
* Data URL: https://data.vietnam.opendevelopmentmekong.net/dataset/a6232bd8-c77e-40f7-ab1b-5fe824de52ce/resource/d1b3b83a-4312-44e7-806d-8f16bf83ed3a/download/disaster_south_eastern_asia_en.csv

* Data Type: CSV

License: Creative Commons Attribution Share-Alike. [CC BY-SA 3.0 DEED License](https://creativecommons.org/licenses/by-sa/3.0/)

Overview:
From 1909 to 2021, 2737 disaster events have been recorded. 

The dataset consists of 53 regular attributes to these events, as sequence number, disaster coding code, year, disaster group, disaster type group, disaster type, event name, water, country, location, longitude, latitude, local time, start date, end date, total number of deaths, total losses...


### Datasource2: Southeast Asia Economy Indicators
* Metadata URL: https://www.kaggle.com/datasets/prasad22/global-economy-indicators

* Data URL: https://www.kaggle.com/datasets/prasad22/global-economy-indicators

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
