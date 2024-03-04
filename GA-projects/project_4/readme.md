<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 5px; height: 70px">

# Optimising Hospital Bed Occupancy through Machine Learning
**DSI-41 Group FWSG**: Muhammad Faaiz Khan, Sharifah Nurulhuda, Tan Wei Chiong, Gabriel Tan

---

#### Background and Introduction 
___

Singapore's public healthcare system has faced [hospital bed crunch issues since at least 2010](https://news.sma.org.sg/4203/In_Sight.pdf). This may be attributed at least in part to [Singapore’s aging population](https://www.todayonline.com/singapore/ageing-society-contributes-hospital-bed-crunch-gan).

A [sustained **Bed Occupancy Rate (BOR)** of less than 85% in the hospitals is generally recommended](https://www.moh.gov.sg/news-highlights/details/hospital-bed-occupancy-rate#:~:text=A%20sustained%20BOR%20of%20less,reduced%20access%20to%20hospital%20care) by academic communities and healthcare authorities alike to ensure patient safety. When such thresholds are crossed and when demand exceeds bed supply, there is an [increased chance of poorer outcomes](https://www.researchgate.net/publication/358972286_Machine_learning_based_forecast_for_the_prediction_of_inpatient_bed_demand), e.g.:
- Longer waiting times, compromising the quality of patient care and staff satisfaction
- Greater risk of avoidable mortality
- Lower satisfaction levels of both patients and hospital staff
- Other hospital costs related to stretched resources in managing the excess demand

It is imperative therefore to ensure that hospital capacity is adequately monitored and optimally managed.

To this end, the Ministry of Health in Singapore tracks BOR statistics for eight major public healthcare institutions in Singapore, namely: 
- Under the '**National University Health System' (NUHS)**' cluster: 
    
    1. _National University Hospital_ (NUH), 
    2. _Ng Teng Fong General Hospital_ (NTFGH), 
    3. _Alexandra Hospital_ (AH)
- Under the '**National Healthcare Group (NHG)**' cluster: 
    
    4. _Singapore General Hospital_ (SGH),
    5. _Changi General Hospital_ (CGH), 
    6. _Sengkang General Hospital_ (SKH)

- Under the '**Singapore Health Services (SingHealth)'** cluster:
    
    7. _Tan Tock Seng Hospital_ (TTSH), 
    8. _Khoo Teck Puat Hospital_ (KTPH)

The BOR statistics are [calculated based on the midnight bed census at each hospital](https://www.moh.gov.sg/resources-statistics/healthcare-institution-statistics/beds-occupancy-rate-(bor)#:~:text=The%20beds%20occupancy%20rate%20is,census%20taken%20at%200000hrs%20Tuesday%5D.).

As each healthcare cluster and their constituent hospitals operate relatively independently, [serving different regions in Singapore](https://www.channelnewsasia.com/singapore/healthiersg-regional-health-manager-healthcare-cluster-nuhs-nhg-singhealth-2965946), this project will focus exclusively on BOR predictions for **NUH**.

#### Objectives
___

**Problem Statement**:
To accurately predict the occupancy rate of the public hospital NUH, so as to guide efficient allocation of manpower and inventory for acute inpatient cases.

**Models**:

A series of machine-learning algorithms will be used to generate predictions for BOR for both hospitals: 
- Time series prediction: 
    - ARIMA-based modeling, 
    - Long Short-Term Memory (LSTM) Recurrent Neural Network  
- Regression modeling: 
    - Linear Regression
    - Random Forest

Evaluation for choice of the final model will be based on how closely predictions match the test data, using metrics such as _Root Mean Squared Error_ where relevant.

**Scope of study**:

We are aiming to predict future (up to 3-monthly) Bed Occupancy Rates for NUH, based on:`
- **Daily** BOR statistics between 2018 to 2023, retrieved from the [MOH website](https://www.moh.gov.sg/resources-statistics/healthcare-institution-statistics/beds-occupancy-rate-(bor)):

Other publicly-available statistics were also examined as potential features, as we hypothesise that seasonal fluctuations in the following may be reflected in hospitalisation patterns:
- Averaged daily infectious disease cases (i.e. dengue, acute respiratory tract infections, acute diarrhea), retrieved from [MOH website](https://www-moh-gov-sg-admin.cwp.sg/resources-statistics)
- Averaged daily weather data (i.e. wet bulb temperatures; rainfall), retrieved via webscraping from [Meteorological Service Singapore](https://www.weather.gov.sg/home/)
- Averaged daily road accident injuries (only monthly data available for 2018 to 2022), retrieved from the [Singapore Police Force website](https://www.police.gov.sg/-/media/4E82276DD8944CD798DCB65EEDFDCA7B.ashx)
- Public holidays, retrieved from the [Ministry of Manpower website](https://www.mom.gov.sg/employment-practices/public-holidays)

With the chosen algorithm, a dashboard application could be developed using such statistics from various Government bodies (and for future work: other hospital-specific data) to help the NUH hospital administration with better bed occupancy and utilisation forecasting.

**Importance of project**:

- Apart from the potential to deliver better outcomes for patients and hospital staff as described in the preceding sub-section, accurate bed forecasting will also allow optimisation of NUHS' running costs through improved manpower rostering and inventory planning (e.g. medical supplies). This is especially crucial in the public healthcare setting, where the accountability of taxpayer monies is important.


#### Data Dictionary
____
|Feature name|Type|Description|
|---|---|---|
|`date`|datetime64[ns]|The date for the respective data point|
|`year`|string|The year for the respective data point|
|`month`|string|The month for the respective data point|
|`day_of_week`|string|The day of the week for the respective data point|
|`is_holiday`|int|Whether the respective data point happens on a public holiday, as declared by the Ministry of Manpower|
|`total_rainfall`|float|The rainfall total for that day, in units of mm, as recorded by the Changi weather station|
|`wet_bulb_temperature`|float|The maximum wet bulb temperature for that day, in units of $^{\circ}\text{C}$, as recorded by the Changi weather station|
|`dengue`|int|The number of dengue cases on the day that the data point occurs in|
|`urti`|int|The number of Acute Upper Respiratory Tract infections on the day that the data point occurs in|
|`diarrhea`|int|The number of diarrhea cases on the day that the data point occurs in|
|`nuh`|float|The percentage of beds that are occupied in NUH on the day that the respective data point occurs in|

#### Model Evaluation
___

We ran the data through two types of modelling:
* Regression Models (Linear Regression, Ridge CV, Lasso CV, Random Forest)
* Time Series Models (SARIMA, SARIMAX, RNN LSTM + SARIMA)

**Regression Models**

The table below shows the results of our regression models.

|     Metrics    | Linear Regression | Ridge CV | Lasso CV | Random Forest |
|:--------------:|:-----------------:|:--------:|:--------:|----------------|
| Train R2 Score |       0.6462      |  0.6678  |  0.6435  |     0.8572     |
|  Test R2 Score |       0.3993      |  0.4296  |  0.4327  |     0.5363     |
|      RMSE      |       3.0788      |  3.0002  |  2.9922  |     2.7053     |

**Insight 1:**
All three models agree : time (specifically in months) affect the availability of hospital beds the most (has the largest coefficients)

After regularisation, 
* May is the month with the largest positive impact on occupancy
* January is the month with the largest negative impact on occupancy
* Public holidays and weekends tend to have lower occupancy rates

**Insight 2:** 
Based on the R2 scores above, we can see that there is evidence of overfitting in the model as there is a large difference between the train and test R2 scores.

**Insight 3:**
Decent RMSE values, showing around 2-3% error.

**Time Series Models**

The table below compares the Mean Absolute Percentage Error (MAPE) for the three time series models.
|     Metrics    | SARIMA only | SARIMAX only | RNN LSTM + SARIMA |
|:--------------:|:-----------------:|:--------:|:--------:|
| MAPE |       0.05      |  0.05  |  0.6435  |

**Insights (SARIMA) :**
- Predictions of test set matches closely with peaks of the actual test data
- There is a fairly uniform trend, likely a result of the autocorrelation. The trend carries on
even after leaving the test set.
- Optimal hyperparameters are `ARIMA(0,1,0)(2,0,2)[7]` with intercept 

**Insights (SARIMAX) :**
- Fits and looks almost identical to the model obtained by SARIMA
- Cannot make predictions outside of test set because of lack of $X$ for those
times
- Downsides to this approach: Errors propagate very quickly
- It seems like exogenous features are not too predictive in this context
- Model hyperparameters are `ARIMA(1,1,0)(2,0,2)[7]` with intercept
- Future work: Use SARIMA to individually predict each one of the $X$ features
past the test set, and then use those predicted $X$ values as $X$ input to SARIMAX

**Insights (RNN LSTM + SARIMA) :**
* As seen in the plot above, our autoregressive LSTM model appears to perform well on the unseen testing data. 
* However, we acknowledge that this model will face similar issues as the SARIMA model, where predictions beyond the near future may not be as accurate due to unstability when extrapolated further in time.


#### Cost-Benefit Analysis
___



| <ins>CY2024: Q3 to Q4</ins>                     |    |                                                                                                                                                               |                |
|-------------------------------------------------|----|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| **Costs**                                       |    | **<ins>Setup (6 months)</ins>**                                                                                                                               |                |
|                                                 | 1. | Model development (data acquisition and cleaning, model training)                                                                                             |       ($300,000) |
|                                                 | 2. | Development of dashboard app; implementation and integration with existing systems                                                                            |       ($200,000) |
|                                                 | 3. | Hardware and software acquisition                                                                                                                             |        ($40,000) |
|                                                 | 4. | Coordination, staff training and education costs                                                                                                              |        ($20,000) |
|                                                 |    |                                                                                                                                       **Sub-total for costs for month 1-12** |   **($560,000)** |
|                                                 |    |                                                                                                                                                               |                |
| <ins>CY2025: Q1 to Q2</ins>                     |    |                                                                                                                                                               |                |
| **Benefits**                                    |    | Assuming a **3% reduction in sub-optimal bed utilisation**, i.e. **36 beds in NUH**:                                                                            |                |
|                                                 |    | **<ins>Initial Implementation (6 months)</ins>**                                                                                                              |                |
|                                                 | 5. | Manpower savings from staffing optimisation                                                                                                                   |       $176,000 |
|                                                 |    | - Assuming bed ratio of 1 senior nurse to 4 beds, i.e. 9 nurses x 4-hour over-time shift/ day * 182.5 man days in 6 months                                                |                |
|                                                 | 6. | Cost savings from supply chain optimisation                                                                                                                   |       $262,800 |
|                                                 |    | - Assuming savings through inventory/medical supply procurement processes; in-patient meal catering, etc. - $40 cost savings per bed per day x 182.5 man-days in 6 months |                |
|                                                 |    |                                                                                                                            **Sub-total for benefits/savings for month 1-12** |   **$438,800** |
|                                                 |    |                                                                                                       **NET BENEFIT for month 1-12** (Savings minus Costs) | **($121,200)** |
|                                                 |    |                                                                                                                                                               |                |
| <ins>CY2025: Q3, Q4 to<br> CY2026: Q1, Q2</ins> |    |                                                                                                                                                               |                |
| **Costs**                                       | 7. | Maintenance and updates (e.g. software licences, storage solutions)                                                                                           |        ($30,000) |
|                                                 |    |                                                                                                                                       **Sub-total for costs** |    **($30,000)** |
| **Benefits**                                    | 8. | Assuming a **3% reduction in sub-optimal bed utilisation**, i.e. **36 beds in NUH**:                                                                            |                |
|                                                 |    | **<ins>Initial Implementation (6 months)</ins>**                                                                                                              |                |
|                                                 |    | Manpower savings from staffing optimisation                                                                                                                   |       $352,000 |
|                                                 |    | Cost savings from supply chain optimisation                                                                                                                   |       $525,600 |
|                                                 |    |                                                                                                                            **Sub-total for benefits/savings** |   **$937,600** |
|                                                 |    |                                                                                                         **NET BENEFIT for month 13-24** (Savings minus Costs) |   **$907,600** |
|                                                 |    |                                                                                                                                                               |                |
|                                                 |    |                                                                                                                      **NET BENEFIT OVER 24 MONTHS (2 YEARS)** |   **$786,400** |


<h6>Footnote/ References:  

- Nurse-to-bed ratio: https://www.moh.gov.sg/news-highlights/details/ensuring-adequate-rest-for-nurses/#:~:text=The%20typical%20nurse%2Dto%2Dbed,for%20more%20complex%20ICU%20cases
- Estimated OT man-hour rate for staff nurse (based on monthly base salary of $3,000/4 weeks/42hrs * 1.5 OT rate): https://www.hseu.org.sg/wps/wcm/connect/4bd241f4-d006-4edb-ba27-f7cec483954b/NUHS+Collective+Agreement+2022.pdf?MOD=AJPERES
- Other hospital running costs based on ballpark estimates

#### Assumptions and Limitations
___

The availability of public data for BOR was restricted to only 2018 onwards, which makes it challenging for us to identify potential longer term (seasonality) patterns in our exogenous (X) features.
- Compounding the problem is the fact that the data from 2020 to 2021 was highly anomalous - due to the [Covid-19 situation and nationwide efforts across healthcare institutions to contain the pandemic](https://www.nuhs.edu.sg/About-NUHS/Newsroom/Documents/NUHS-COVID-19-Commemorative-Book.pdf)
- Therefore data from 2020-2021 was **excluded** from our modeling, resulting in only the most recent 2022-2023 data being used. With more runway and post-pandemic 2024 data, our production algorithm is likely to be even more accurate
- Unlike BOR, daily data was also not available for certain features such as infectious diseases - an assumption was made to average the weekly data over 7 days for such features

### Conclusions and future work
___

The deep learning model (LSTM RNN) shows the greatest promise as a production algorithm for our BOR time series predictions. Despite the limitations around public-available statistics and the length of post-Covid BOR data, it shows a strong predictive ability on unseen data, with minimal requirement for supplementary features.

Upon commissioning, future work for the modeling could include **hospital data** to be supplied by NUH, such as:
- Emergency Department (ED) admissions data
- Length of stay data for different patient types and disease mix
- Discharge rates and patterns
- Readmission rates for specific conditions or patient groups
- Specific changes in work processes or innovations that could have had an impact patient care efficiency

One potential area of exploration is developing individual SARIMA for each predictive feature, before feeding these features to an overarching SARIMAX/LSTM model. This would allow us to extrapolate these models based on prior data, reducing reliance on current data.