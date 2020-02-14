-- Databricks notebook source
DROP TABLE IF EXISTS diamonds;
CREATE TABLE diamonds USING csv
OPTIONS (path "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv",  header "true");
describe diamonds;

-- COMMAND ----------

DROP TABLE IF EXISTS diamonds;
CREATE TABLE diamonds USING csv
OPTIONS (path "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv",  header "true", inferSchema "true");
describe diamonds;

-- COMMAND ----------

DROP TABLE IF EXISTS diamonds;
CREATE TABLE diamonds(_c0 String, carat double, cut String, color String, clarity String, depth double, dtable int, price double, x double, y double, z double) USING csv
OPTIONS (path "/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv",  header "true");
describe diamonds;

-- COMMAND ----------

select * from diamonds limit 5

-- COMMAND ----------

select distinct clarity from diamonds 

-- COMMAND ----------

select color, count(*) from diamonds group by color

-- COMMAND ----------

DROP TABLE IF EXISTS diamonds

-- COMMAND ----------

-- DROP TABLE IF EXISTS iot_devices;
-- CREATE TABLE iot_devices USING JSON OPTIONS (path "databricks-datasets/iot/iot-devices.json", inferSchema "true");
-- describe iot_devices;

-- COMMAND ----------

DROP TABLE IF EXISTS departuredelays;
CREATE TABLE departuredelays USING CSV OPTIONS (path "databricks-datasets/flights/departuredelays.csv", header "true");
describe departuredelays;


-- COMMAND ----------

DROP TABLE IF EXISTS airportcodes;
CREATE TABLE airportcodes USING CSV OPTIONS (path "databricks-datasets/flights/airport-codes-na.txt", header "true", delimiter "\t",  inferSchema "true");
describe airportcodes;

-- COMMAND ----------

SELECT substring(date, 0, 2) as month, avg(delay) as delay from departuredelays group by substring(date, 0, 2);

-- COMMAND ----------

SELECT * from (SELECT City, IATA, substring(date,0,2) as month, count(*) as arrivals_count from departuredelays join airportcodes on origin=IATA group by  City, IATA, substring(date, 0, 2)) natural join (SELECT City, IATA, substring(date,0,2) as month, count(*) as departures_count from departuredelays join airportcodes on destination=IATA group by City,IATA, substring(date, 0, 2))

-- COMMAND ----------

SELECT City, IATA, count(*) as total_flights from ((SELECT City, IATA, date from airportcodes join departuredelays on IATA=origin) union (SELECT City, IATA, date from airportcodes join departuredelays on IATA=destination)) where substring(date,0,2)='03' group by City, IATA order by total_flights desc limit 1;
