-- Databricks notebook source
DROP TABLE IF EXISTS products;
CREATE TABLE products(ProductID int, Name string, ProductNumber string, Color string,	StandardCost double,	ListPrice double,	Size string,	Weight double,	ProductCategoryID int,	ProductModelID int,	SellStartDate timestamp,	SellEndDate timestamp,	DiscontinuedDate timestamp,	ThumbNailPhoto string,	ThumbnailPhotoFileName string,	rowguid string,	ModifiedDate timestamp) USING CSV OPTIONS (path '/dbfs/lab2_4/products.tsv', header 'true', sep '\t');
describe products;

-- COMMAND ----------

DROP TABLE IF EXISTS orderdetails;
CREATE TABLE orderdetails(SalesOrderID int, SalesOrderDetailID int,	OrderQty int,	ProductID int,	UnitPrice double, 	UnitPriceDiscount double,	LineTotal double,	rowguid string,	ModifiedDate timestamp) USING CSV OPTIONS (path "/dbfs/lab2_4/orderdetails.tsv", header "true", delimiter "\t");
describe orderdetails;

-- COMMAND ----------

select * from orderdetails

-- COMMAND ----------

select * from products

-- COMMAND ----------

SELECT ProductID, Name, double(Weight) from products where double(Weight) > 0 order by double(Weight) desc limit 15

-- COMMAND ----------

SELECT ProductCategoryID, count(ProductID) from products where ProductCategoryID is not NULL group by ProductCategoryID 

-- COMMAND ----------

SELECT count(distinct ProductModelID) from products

-- COMMAND ----------

select ProductModelID, count(ProductID) as total_products from products group by ProductModelID order by total_products desc limit 10

-- COMMAND ----------

select ProductID, Name, Color, Size, ListPrice from products where ProductModelID = 20

-- COMMAND ----------

select orderdetails.ProductID, sum(OrderQty) from orderdetails inner join products on products.ProductID = orderdetails.ProductID where ProductCategoryID = 20 group by orderdetails.ProductID
