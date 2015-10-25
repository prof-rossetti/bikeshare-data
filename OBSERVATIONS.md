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


```` sql
-- which companies operate the greatest number of bike-share networks?
SELECT
  nc.name AS company_name
  ,count(DISTINCT network_tag) AS network_count
FROM network_companies nc
GROUP BY 1
HAVING network_count > 4
ORDER BY 2 DESC
````

=>

company_name	|	network_count
--- | ---
Nextbike GmbH	|	108
Comunicare S.r.l.	|	99
Domoblue	|	43
Crispin Porter + Bogusky	|	23
Trek Bicycle Corporation	|	23
Humana	|	23
PBSC	|	13
DB Rent GmbH	|	13
Alta Bicycle Share, Inc	|	12
Mobilicidade Tecnologia LTD	|	12
Grupo Serttel LTDA	|	12
Brainbox Technology	|	11
Cyclopolis Systems	|	11
Smoove SAS	|	11
ClearChannel	|	5
