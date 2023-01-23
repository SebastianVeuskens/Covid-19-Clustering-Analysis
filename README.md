# Clustering Analysis of countries using the COVID-19 cases dataset 
*University-based extended paper reproduction and analysis* 

# General information 
## Context
- University course *Machine Learning Systems for Data Science*
- Project timeframe from December 2022 until January 2023
- Reproduction of Paper Analysis

## Authors
- Alberto Trashaj
- Manuel Rech
- Sebastian Benno Veuskens

## Institution
[University of Bologna](https://www.unibo.it/en)

# Data overview
All data are collected in accordance with the paper procedure from the John-Hopkins University website. The raw data is available [here](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6). 

## Datasets
- [Absolute cases from the first day with cases recorded](data/Coronavirus_Data_Cases_1a.%20Per%20day.csv)  
- [Absolute cases from the 22nd of January until 4th of April 2020](data/Coronavirus_Data_Cases_1b.%20Per%20date.csv)
- [Absolute cases per 1 million population from the first day with cases recorded](data/Coronavirus_Data_Cases_2a.%20Per%20day_population.csv)  
- [Absolute cases per 1 million population from the 22nd of January until 4th of April 2020](data/Coronavirus_Data_Cases_2b.%20Per%20date_population.csv)
- [Absolute cases per 1 million population per area from the first day with cases recorded](data/Coronavirus_Data_Cases_5a.%20Per%20day_popul_surf.csv)  
- [Absolute cases per 1 million population per area from the 22nd of January until 4th of April 2020](data/Coronavirus_Data_Cases_5a.%20Per%20date_popul_surf.csv)

# Methods and Analysis

## Selection criteria 
30 countries are selected for each dataset, based on one of the two selection critera, respectively:
- The countries with the highest number of cases on the 4th of April 2020
- The countries where cases occured first 

## Agglomerative Clustering
Based on these datasets and selected countries, an agglomerative clustering algorithm is applied.

## Extension
Based on the outcome of the clustering algorithm, the countries are embedded into a world map. Their cluster membership is made visually available within the context of all countries. 

# References
The referenced paper is available [here](https://www.sciencedirect.com/science/article/pii/S2352340920306818?via%3Dihub). The description for the university course in Machine Learning can be found [here](https://www.unibo.it/en/teaching/course-unit-catalogue/course-unit/2022/444067). 