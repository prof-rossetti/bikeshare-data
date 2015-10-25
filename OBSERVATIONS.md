# Bike-share Data Observations

```` sql
-- which 20 networks have the most stations, and how many does each have?
SELECT
 top_networks.*
 ,n.city
 ,n.country
 ,n.feed_url
 ,n.system_type
 ,n.feed_format
FROM (
    SELECT network_tag, count(DISTINCT id) AS station_count
    FROM stations
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 20
) top_networks
JOIN networks n ON n.tag = top_networks.network_tag
````
