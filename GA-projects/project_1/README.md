# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Exploring Climate Data of Singapore


## Introduction
Dengue fever is a mosquito-borne viral illness that is common in tropical and subtropical climates, transmitted through the bite of an infected Female Aedes mosquito (aka the vector). 

According to reserach, with global warming causing a change in climate, dengue transmission can possibly be exarcebated. Relative humidity, rainfall and temperature are some weather conditions that are associated with mosquito vector survival. The typical life cycle of Aedes Aegypti mosquito takes up to 4 weeks. Mean temperatures above 27.5 degree celcius are shown to be optimal for the survival of the mosquitoes and temperatures between 25 degree celcius to 32 degree celcius accelerates the life cycle of the mosquito vectors.

Dengue outbreaks have been reported in Singapore as early as 1901 and is still prevalent today, with NEA (National Environment Agency) monitoring multiple dengue clusters in Singapore and deinfining them into 3 categories - [Red Alert, Yellow Alert, Green Alert](https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters). There have also been outreach efforts by NEA to the public to reduce mosquito breeding via the BLOCK method and initiatives such as the creation of Gravitrap to trap the female Aedes mosquitoes which are looking for sites to lay their eggs and it prevents the eggs from hatching. 

Project Wolbachia Singapore is a project by NEA which studies the feasibility of using Wolbachia-carrying Aedes aegypti males to help suppress the population of these mosquitoes. Wolbachia are naturally-occuring bacteria present in more than 60% of insections. When female mosquitoes from the field, which do not carry Wolbachia, miate with males that carry Wolbachia,the eggs derived from these matings do not hatch. With a supressed population, the expected outcome is that dengue transmission will be reduced hence decreasing the number of dengue fever cases in the country.

![Alt text](image.png)
 

**Sources of information**
1. Research Articles:
    - [Drakou, K., Nikolaou, T., Vasquez, M., Petric, D., Michaelakis, A., Kapranas, A., Papatheodoulou, A., & Koliou, M. (2020). The Effect of Weather Variables on Mosquito Activity: A Snapshot of the Main Point of Entry of Cyprus. International journal of environmental research and public health, 17(4), 1403. https://doi.org/10.3390/ijerph17041403]("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7068582/)
    - [Ho SH, Lim JT, Ong J, Hapuarachchi HC, Sim S, Ng LC (2023) Singapore’s 5 decades of dengue prevention and control—Implications for global dengue control. PLoS Negl Trop Dis 17(6): e0011400. https://doi.org/10.1371/journal.pntd.001140](https://journals.plos.org/plosntds/article?id=10.1371/journal.pntd.0011400)
    - [Reinhold, J. M., Lazzari, C. R., & Lahondère, C. (2018). Effects of the Environmental Temperature on Aedes aegypti and Aedes albopictus Mosquitoes: A Review. Insects, 9(4), 158. https://doi.org/10.3390/insects9040158](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6316560/#B24-insects-09-00158)
2. Govenrment Websites relating to weather & Project Wolbachia
    - [Vector-Borne Diseases Research Programme](https://www.nea.gov.sg/corporate-functions/resources/research/vector-borne-diseases-research-programme)
    - [Wolbachia-Aedes Mosquito Suppression Strategy](https://www.nea.gov.sg/corporate-functions/resources/research/wolbachia-aedes-mosquito-suppression-strategy), 
    - [Climate in Singapore](https://www.weather.gov.sg/climate-climate-of-singapore/)
    - [Mosquito release schedule](https://www.nea.gov.sg/corporate-functions/resources/research/wolbachia-aedes-mosquito-suppression-strategy/wolbachia-aedes-release-schedule)
3.  Other sources regarding Project Wolbachia/ dengue-related information
    - ["Project Wolbachia: 300 million mosquitoes released but not a silver bullet to deal with dengue, says NEA"](https://www.channelnewsasia.com/singapore/project-wolbachia-mosquito-dengue-nea-facility-3773176)
    - [CNA Explains: Why is Singapore at risk of a surge in dengue cases?](https://www.channelnewsasia.com/singapore/dengue-clusters-surge-aedes-mosquito-toa-payoh-3753571)
    - [Singapore's dengue emergency](https://edition.cnn.com/2022/06/06/asia/health-dengue-singapore-emergency-climate-heat-intl-hnk/index.html)


## Problem Statement
High incidences of dengue fever is a persistent issue in Singapore despite measures taken by the government to curb it. For example, an increase in rainfall could lead to an increase in the population of mosquitoes, which in turn leads to higher incidences of dengue fever. 

With the implementation of Project Wolbachia, the drop in the number of dengue cases has been observed. However, the release of Wolbachia mosquitoes are currently carried out on a weekly basis, which could be resource intensive and have a negative ecological impact.

As mosquito activity is highly influenced by weather conditions, this project aims to analyse trends in Singapore weather and the number of dengue cases between 2014 to 2018. This analysis can be used to help NEA plan optimal time periods for the release of the male Wolbachia-Aedes mosquitoes into the environment to enhance effectiveness of Project Wolbachia. This can in turn curb dengue transmission to decrease the number of dengue cases.



## Datasets
The following data sets will be used for the project:
1. rainfall_monthly_number_rainydays.csv (original name was: rainfall-monthly-number-of-rain-days.csv, provided by GA)
    - contains the number of rainy days per month from 1982 to 2022
2. rainfall_monthly_total_mm.csv (original name was: rainfall-monthly-total.cs, provided by GA)
    - contains the number of rainy days per month from 1982 to 2022  
3. rel_humidity_monthly_mean.csv (taken from data.gov.sg)
    - contains the mean humidity for each month from 1982 to 2023
4. temp_monthly_mean.csv (taken from data.gov.sg)
    - contains the mean air temperature for each month from 1982 to 2023
5. weekly_numbers_dengue_fever_cases.csv (taken from data.gov.sg)
    - contains the number of cases of dengue and dengue haemorrhagic fever per week from 2014 to 2018

However for consistency and comparability across all data sets, the data from the period 2014 to 2018 will be used for analysis only.

 ### Data dictionary:
|Feature|Type|Dataset|Description|
|---|---|---|---|
|yearweek|datetime|dengue.csv|Date in YYYY-MM-DD|
|number|int|dengue.csv|Number of dengue cases during the specified week |
|date|datetime|weather.csv|Date in YYYY-MM-DD|
|rainfall|float|weather.csv|Total rainfall during the specified month in mm|
|raindays|int|weather.csv|Total number of days with rainfall during the specified month| 
|temp|float|weather.csv|Mean monthly temperature in SG (°C)|
|rh|float|weather.csv|Mean monthly relative humidity in SG| 


## Summary of Analysis
The 5 datasets were obtained in csv formats from GA (given to us) and from [data.gov.sg]("https://beta.data.gov.sg/"). 
There are 3 areas that we focus on:

1. First spike in dengue cases in mid 2014
- As weather conditions such as rainy days and total rainfall increased towards mid 2014, the increase in dengue cases was observed to peak during the similar period.

2. Second spike in dengue cases at the start of 2016
- Towards Nov 2015, rainfall and temperature spiked. The peak in the number of dengue cases was delayed by approximately 1 month after the peak of the respective weather conditions.
    - The peak of the rainfall and temperature values are observed to coincide with the start of the increase in number of dengue cases.
    
3. General trend after 2016
- From Oct 2016 onwards, the number of dengue cases dropped even though there were spikes/ drops in rainfall, temperature and relative humidity.
    - Despite the typical spike in rainfall/ temp occurring at the end of 2016, further analysis of the dengue cases profile did not suggest an increase in number of infections.
    - In fact, there was a drop in number of dengue cases from Oct 2016 (based on the line plots) .
    - Number of dengue cases also did not drastically increase despite spikes in weather conditions in December 2016, compared to prior of project launch.



## Conclusion & Recommendations
### Key Takeaways:
1. Given a known estimate of the weather conditions' profiles and their relationship with number of dengue cases, the spike in dengue cases could be determined:
    - Dengue cases spikes approximately 1 month after rainfall and temperature spikes (humidity will drop due to inverse relationship with temperature)
        - Peak/dips in weather profile suggests initial increase in dengue cases
    - According to available research, the optimal temperature for the survival of Aedes aegypti has a mean of 27.5 deg C, similar to the trend seen in the line plot.

2. The effectiveness of Project Wolbachia cannot be discounted as the launch of the project coincided not only with the reduction of dengue cases, but also in suppression of the spike of dengue cases in the same time frame. 


### Recommendations:
1. Propose for a time-specific release of Wolbachia mosquitoes to maximise cost-efficiency, optimize use of resources such as manpower while reducing ecological impact 

2. Release of Wolbachia mosquitoes are recommended to be 2-4 weeks before the spike in rainfall/ temperature profile 
    - Spikes in rainfall/temperature suggests initial increase in dengue cases
    - This is closely related to the life cycle of the Aedes mosquitoes and also taking into consideration the time NEA require to breed the mosquitoes

3. Prediction of profiles in spikes or drops in weather conditions is crucial in planning for mosquito release
    - Potential for higher precision in prediction of weather conditions from wide availability of past historical data for analysis
    - Partnership with meteorological services for minimal error in predictions can be explored
        - In view of this partnership, NEA can also continue to make use of the [GEOJSON maps]("https://beta.data.gov.sg/collections?query=dengue%20(cases)") that they have already been using to pinpoint clusters all around Singapore