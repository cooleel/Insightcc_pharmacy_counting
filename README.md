# Insightcc_pharmacy_counting
My solution for Insight Data Engineering code challenge
### Notes:  
1. Large input load should be considered, therefore no sorting or any other operations on raw data will be better.  
2. In output file, number format should be clarified.  
3. The data structure used for counting is dictionary, with drug_name as the key, and unique prescriber name set and drug_cost as the value list.  


#solution in sql
SELECT drug_name, count(distinct prescriber_last_name,presriber_first_name) as num_prescriber, sum(drug_cost) as total_cost  
FROM input_table  
GROUP BY drug_name  
ORDER BY total_cost DESC,drug_name;
