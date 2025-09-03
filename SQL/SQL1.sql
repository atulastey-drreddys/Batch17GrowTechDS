-- SIngle line commnets
-- Create database

create database GrowTech;

create database Mouse;

use Growtech;

use world;

-- retrieve the table from database
select * from city;

select * from country;

select * from sakila.category;

select District, Population from city;

select District, Population from world.city;


/* Aggregate function
1) Min
2) Max
3) Count
4) Sum
5) Avg */

select min(population) from city;

select max(population) from city;

select sum(population) from city;

select count(population) from city;

select avg(population) from city;

select min(population), max(population) 
from city;

select min(population), 
max(population),
count(population), 
sum(population),
avg(population) 
from city;

-- as keyword 
select min(population) as Min_Population 
from city;

select min(population) as Min_Pop
from city;

select min(population) as Min_pop, 
max(population) as Max_pop,
count(population) as TotalCount, 
sum(population) as Total_Pop,
avg(population) as Average_pop
from city;

select * from growtech.student_performance;

-- table creation

