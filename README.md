# Cyclistic Bike-Share: Data Analysis Case Study

## 1. Ask Phase

### Business Task
The primary objective of this analysis is to uncover how annual members and casual riders use Cyclistic bikes differently. These behavioral insights will be used to guide a data-driven marketing strategy aimed at converting casual riders into profitable, long-term annual members.

### Key Stakeholders
* **Lily Moreno:** Director of Marketing and project manager, responsible for the development of promotional campaigns.
* **Cyclistic Marketing Analytics Team:** A team of data analysts responsible for collecting, analyzing, and reporting data to guide Cyclistic's marketing strategy.
* **Cyclistic Executive Team:** The detail-oriented executive team who will review the insights and make the final decision on whether to approve the recommended marketing program.

## 2. Prepare Phase

### Data Source
This analysis leverages 12 months of historical bike trip data (September 2025 through August 2026). The dataset is public data provided by Motivate International Inc. under a specific license, enabling the exploration of how different customer types utilize the service. 

*Note: The raw datasets are too large to be hosted on GitHub (exceeding the 100MB limit). You can download the original `.csv` files directly from the [Divvy Tripdata AWS S3 Bucket](https://divvy-tripdata.s3.amazonaws.com/index.html).*

### Data Organization & Credibility
The dataset consists of structured CSV files detailing individual bike trips. The column names and formats have already been standardized in these recent datasets. Following the ROCCC framework, the data is:
* **Reliable:** Accurate and unbiased, reflecting actual logged bike trips.
* **Original:** First-party data collected directly by the company's internal operational systems.
* **Comprehensive:** Contains all necessary dimensions (start/end times, station names, user types) to evaluate the behavioral differences between casual riders and annual members.
* **Current:** Covers the most recent 12-month operational period (2025–2026).
* **Cited:** Sourced directly from the official Cyclistic historical trip datasets.

### Data Privacy
Due to strict data privacy constraints, all personally identifiable information (PII) of the riders has been excluded. It is impossible to connect pass purchases to credit card numbers to determine if casual riders live in the Cyclistic service area or if they have purchased multiple single passes.


## 3. Process Phase

### Tools Used
Python (Pandas library) was utilized to aggregate, clean, and transform the 12 individual monthly datasets into a single master dataframe for robust analysis.

### Data Cleaning & Transformation Steps
1. **Data Aggregation:** Read and concatenated 12 months of raw CSV files into one unified dataset.
2. **Data Reduction:** Dropped irrelevant columns (`start_lat`, `start_lng`, `end_lat`, `end_lng`) to optimize processing speed and isolate the necessary dimensions.
3. **Handling Missing Values:** Removed records containing missing `start_station_name` or `end_station_name` to ensure data integrity for geographic analysis.
4. **Data Transformation:** 
   * Converted `started_at` and `ended_at` strings into functional datetime objects.
   * Created a calculated column, `ride_length_mins`, to express trip duration consistently in minutes.
   * Extracted `day_of_week` and `month` into new columns to enable temporal and seasonal trend analysis.
5. **Data Filtering:** Removed logical outliers, specifically trips with negative/zero duration (typically maintenance or false starts) and trips exceeding 24 hours (potential unreturned bikes).


## 4. Analyze Phase

### Methodology
With the cleaned data, descriptive analysis was conducted to uncover the distinct behavioral patterns between casual riders and annual members[cite: 1]. The analysis focused on two primary metrics: total ride volume (to gauge demand) and average ride duration (to gauge engagement).

### Key Aggregations
Data was grouped and aggregated across three dimensions:
1. **Overall Usage:** Comparing total trips and average duration directly between user types.
2. **Weekly Trends:** Analyzing how usage fluctuates throughout the days of the week to identify commuting versus leisure patterns.
3. **Monthly Seasonality:** Tracking ride volumes across different months to observe the impact of weather and seasonal demand.

The output generated two highly aggregated summary datasets, engineered specifically to power efficient and responsive data visualizations in Tableau.


## 5. Share Phase

### Data Visualization
Tableau Public was utilized to synthesize the aggregated data into an interactive, executive-ready dashboard. The visualizations highlight the contrasting behavioral patterns between casual riders and annual members to support strategic decision-making.

**Key Findings:**
* **Commuting vs. Leisure:** Members exhibit peak usage during traditional commuting days (Monday-Friday), whereas casual riders peak on weekends.
* **Engagement Duration:** While members account for a higher total volume of rides, casual riders consistently demonstrate a significantly longer average ride duration.
* **Seasonal Sensitivity:** Both user segments follow a strong seasonal trend, peaking in summer and dropping in winter, though casual rider volume is more drastically affected by colder months.

**Interactive Dashboard:**
[View the Interactive Tableau Dashboard Here](https://public.tableau.com/app/profile/jorge.garcia.data/viz/CyclisticBike-ShareUserBehaviorAnalysis_17907228305600/CyclisticBike-ShareUserBehaviorAnalysis2025-2026)


## 6. Act Phase

### Top 3 Recommendations
Based on the insights gathered, the following recommendations are proposed to design a marketing strategy that converts casual riders into annual members:

1. **Weekend Conversion Campaigns:** Since casual riders peak on weekends for leisure, Cyclistic should launch weekend-specific promotions or a "Weekend-Only Membership" tier as an intermediary step to full annual membership.
2. **Seasonal Discounts:** Casual ridership drops significantly in the winter. Offering early-bird or discounted annual memberships right before the peak summer season (April/May) would capitalize on their seasonal engagement.
3. **Ride Length Incentives:** Casual riders ride for longer durations. Introducing a "rewards program" for annual members that offers perks for longer rides could attract casual riders who are already accustomed to long trips.