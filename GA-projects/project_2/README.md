# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2: Singapore Housing Data and Kaggle Challenge

## Introduction
Determining the true sale price of an HDB resale flat in Singapore can be a complex task, influenced by a myriad of factors, including but not limited to location, amenities, surrounding and future town developments, number of rooms and even government policies.

For Project 2, our task was to create a regression model based on the provided Singapore Housing Dataset on Kaggle (https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data). A linear regression prediction model will be created to predict HDB unit prices based on the attributes of the property. The dataset provided on Kaggle is exceptionally detailed with over 70 columns of different features relating to the HDB units, giving us a good starting base to explore trends and identify potential features to engineer.

As part of the process, we also interviewed a real estate agent to get real-world business insights and directions for where the model should point to. The following key attributes for HDB resale price were identified during the interview:
- Neighbourhood
- Proximity to amenities (MRT station, malls, etc)
- Remaining lease
- Floor level
- Fulfilment of ethnicity quota (unfortuately uncaptured by the dataset)

Features pertaining to these attributes shall be engineered (where necessary) for the linear regression model.

## Problem Statement
As part of the Kaggle challenge for Project 2, the task is to develop a predictive model for the resale cost of a HDB unit. The model will be trained on the train.csv dataset, to perform predictions for the test.csv dataset, both of which were obtained from Kaggle.

This model aims to predict the resale price for a given HDB unit and to identify the key features that affect the resale price. This analysis can be used to help prospective flat buyers and sellers in determining the valuation of a particular HDB unit of interest, given the attributes of the unit. Such analysis can provide flat owners insight on how to improve the valuation of their flat.

## Datasets
The following data sets will be used for the project:
1. train.csv (provided by Kaggle, https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data)
    - The HDB dataset on which the model will be trained.
2. test.csv (provided by Kaggle, https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data)
    - The HDB dataset for which the model will predict HDB unit resale prices. The predicted prices shall be submitted on Kaggle.
3. shopping_mall_coordinates.csv (taken from https://www.kaggle.com/datasets/karthikgangula/shopping-mall-coordinates)
    - Due to missing values in the `Mall_Nearest_Distance` column in train.csv, the values in the column shall be re-engineered by comparing the coordinates of each HDB unit and the coordinates of the shopping malls as described in shopping_mall_coordinates.csv.

 ### Data dictionary for engineered features:

|Feature|Type|Description|
|---|---|---|
|`mrt_score`|int|Minimum number of MRT stations to Central Business District; Uses Dijkstra's algorithm on `mrt_name`|
|`nearest_brand_pri_sch`|float|Uses the Haversine formula on `latitude`, `longitude`, and data from [The Children's Society](https://www.childrensociety.org.sg/wp-content/uploads/2022/07/Schools-and-Class-Divide_Research-Monograph-11_FINAL_24-Aug-2016v3.pdf)|
|`nearest_brand_sec_sch`|float|Uses the Haversine formula on `latitude`, `longitude`, and data from [The Children's Society](https://www.childrensociety.org.sg/wp-content/uploads/2022/07/Schools-and-Class-Divide_Research-Monograph-11_FINAL_24-Aug-2016v3.pdf)|
|`price_per_sqm`|float|`resale_price / floor_area_sqm`|
|`remaining_lease_years`|int|`99 - (tranc_year - lease_commence_date)`|
|`mall_nearest_distance`|float|Engineered from shopping_mall_coordinates.csv|

Additionally, the following categorical features from train.csv were converted to dummy features for the linear regression model:

|Feature|Description|
|---|---|
|`flat_model`|model of the unit|
|`town`|neighbourhood of the unit|
|`tranc_year`|year in which the resale occured|
|`tranc_month`|month in which the resale occured|

## Summary of Analysis

The data processing steps are as follows:

1. Data Cleaning

- Standardize all the column names to be fully lowercase and separated by underscores.
- We convert `tranc_year`, `tranc_month` to strings.

2. Feature Engineering

- Use Dijkstra's algorithm to get `mrt_score`. 
    - This uses `mrt_name`.
- Use the Haversine formula to get `nearest_brand_pri_sch`, `brand_pri_sch_within_1km`, `brand_pri_sch_within_2km`. `nearest_brand_sec_sch`, `brand_sec_sch_within_1km`, `brand_sec_sch_within_2km`. 
    - This uses `latitude`, `longitude`, `pri_sch_latitude`, `pri_sch_longitude`, `sec_sch_latitude`, `sec_sch_longitude`.
- Use the Haversine formula to imput `mall_nearest_distance`, `mall_within_500m`, `mall_within_1km`, `mall_within_2km`.
    - This uses `latitude` and `longitude`, along with a separate dataset `shopping_mall_coordinates.csv`.
- Change the target variable from `resale_price` to `price_per_sqm`.
    - This is computed as `resale_price / floor_area_sqm`.
- `hawker_within_500m`, `bus_stop_within_100m` and `mrt_within_500m` as indicators of "walking distance"
- Replace `full_flat_type` with dummies for `terrace`, `dbss`, `mansionette_loft`, `duxton_S1_S2`
- Calculate `remaining_lease_years` (`99 - (tranc_year - lease_commence_date)`)

3. Dropping Columns

There are two main reasons for dropping the following columns - either they are redundant or they are already engineered to a more useful variable.

<details>

|Column name(s)|Reason for dropping|
|---|---|
|`tranc_yearmonth`|info in `tranc_year` and `tranc_month` columns|
|`storey-range`|info in `lower`, `mid`, `upper` columns|
|`mid_storey`|exact same values as `mid`|
|`lower`, `upper`|highly correlated with `mid`|
|`residential`|only has one value|
|`floor_area_sqft`|dropped to prevent artificial dependency, use only `floor_area_sqm` instead|
|`address`, `block` and `street_name`|hard to interpret|
|`flat_type`|info in `full_flat_type`|
|`planning_area`, `postal`|highly correlated with `town`|
|`block`, `street_name`|hard to interpret|
|`year_completed`|high correlation with `lease_commence_date`|
|`total_dwelling_units`|sum of unit-related features - perfectly correlated|
|`hawker` columns, except for `hawker_within_500m`|keep that as a measure of "within walking distance"|

- Engineered columns to be dropped are
    - `mrt_name`
    - `bus_stop_name`
    - `pri_sch_name`, `pri_sch_nearest_distance`
    - `sec_sch_name`, `sec_sch_nearest_distance`
    - All columns with `latitude` and `longitude` (highly correlated because of the small range)
    - `resale_price` (can be recovered in test data using `price_per_sqm * floor_area_sqm`)
    - `hdb_age`, `lease_commence_date` (replace with `remaining_lease_years = 99 - (tranc_year - lease_commence_date)`)
    - `bus_stop_nearest_distance`, `mrt_nearest_distance` (replaced with dummies `~_within_100m/500m` as a measure of "within walking distance")
    - `full_flat_types` (replaced with dummies for `terrace`, `dbss`, `mansionette_loft`, `duxton_S1_S2`)
</details>


4. Pipelines

In order to shape our data to make the model as predictive as possible, we would need to split our variables up into a few categories:

#### Numeric Variables (either integer or float):

Our numeric variables are the remaining ones that are selected by `df.select_dtypes(np.number)`, excluding the following:
- `id`
- `resale_price`

Meanwhile, the rest of the numeric variables will undergo imputing with `SimpleImputer()`, and then scaling with `StandardScaler()`.

#### Categorical Variables

These are variables that take on a discrete finite set of non-numerical values. As one-hot encoding does not perform as well when there are too many categorical values in a variable, we partition them into two subsets - high-cardinality (>255 categories) and low-cardinality (<= 255 cardinalities). However, due to being difficult to interpret, the high-cardinality variables will be dropped.

The low-cardinality categorical variables are as follows:
- `town`
- `tranc_year`
- `tranc_month`

These will undergo one-hot encoding with `OneHotEncoder()`.

All variables will then go through a regression model.

The impact of each feature on the unit price is assessed by its corresponding coefficient based on the linear regression model. Using the Ridge regression model gives the following insights:

1. The features with the most positive relationship with unit price are as follows:
    - `floor_area_sqm`
    - `remaining_lease_years`
    - `mid`
    - `town_BUKIT TIMAH`

2. The features with the most negative relationship with unit price are as follows:
    - `3room_sold`
    - `multistorey_carpark_Y`	
    - `dist_to_nearest_brand_pri_sch`
    - `mrt_score`

## Conclusion & Recommendations
### Key Takeaways:
1. Remaining lease has a big impact on the unit cost, giving newer units a slight advantage over older units. Otherwise, older units have the advantages of a typically larger floor area and locations in established mature estates.
2. Homeowners could focus on internal improvements to shift their property into a higher flat type category if possible, thus improving the cost of the unit. Renovations that effectively utilize space could also be beneficial.
3. Location also has a significant impact on the unit price. Proximity to amenities such as malls and MRT will improve the price of the unit. For neighbourhoods, Bukit Timah, Marine Parade, Bishan, Queenstown have higher resale values, making them potentially good investment areas.



