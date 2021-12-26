# surfs_up
## Overview
The purpose of this project is to provide temperature statistics from the island of Oahu that will be used for analysis in determining if Oahu is a possible location
for a surf & ice cream business. The statistics provided are within the years 2010 to 2017 and include:
- Temperature statistics from the month of June
- Temperature statistics from the month of December


## Results
The code written to gather and calculate the stats, is included in the following file: [Surfs Up Stats](/SurfsUp_Challenge.ipynb)

The following 2 Deliverables were produced. 
-  **June Statistics**
   - ![June Stats](/Resources/june_temperature_stats.png)  
-  **December Statistics**
   - ![December Stats](/Resources/december_temperature_stats.png) 

Three major points from these deliverables include:
1) Only about 4 degrees separates June from December in terms of average temperature
   - This means that December is not that much colder on average than June.  
2) Both June's and December's 50th percentile are above 70 degrees
   - This means that both June and December averages 50% of their days above 70 degrees, which seems like a great temperature for both surfing and eating ice cream.
3) December's 25th percentile is 69 degrees, meaning only 25% of December days are lower than 69%
   - If you take the 25th percentile and December's minimum of 56 degrees, the implication is December provides good opportunity for active surfing based on air temperature.
    

## Summary
Based on temperatures, Oahu is an ideal location to open a surf and ice-cream shop since the temperatures are warm enough year round based on temperatures in both June and December. 

However, it would be prudent to perform additional analysis to make sure there aren't other situations that could impact a business. Two additional queries that should also be run and analyzed include:
1) Gathering precipitation statistics for the month of June
   - ![June Precipitation](/Resources/june_precip_query.png)
2) Gathering precipitation statistics for the month of December
   - ![December Precipitation](/Resources/dec_precip_query.png)

In addition to gathering air temperature, it would also be prudent to gather and analyze:
- Average water temperature for the months of June and December
- Ideal and/or popular water temperature for surfing
- Ideal and/or popular air temperature for eating ice cream
