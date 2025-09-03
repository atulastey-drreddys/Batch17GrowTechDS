use mouse;

select * from employee;

/* alter statement
1) Rename
2) Add column
3) Remove Column
4) change Data Type
5) Drop 
*/

-- rename table name

alter table employee
rename new_emp_tab;

alter table mobile
rename telephone;

-- add column in my existing table

alter table new_emp_tab
add column Salary float not null;

-- add multiple column
alter table new_emp_tab
add column DOB date,
add column Designation varchar(50),
add column Department varchar(20);


-- drop existing from table

alter table new_emp_tab
drop column DOB;

-- drop multiple column

alter table student 
drop column Id, 
drop column Age;

-- drop the table
drop table student;

select * from laptop;

select * from world.city;

-- change the data type of existing column

alter table new_emp_tab
modify column Id float;

alter table new_emp_tab
modify column Name char(10),
modify column Age float;

-- Remaining topic
-- change the constraints of existing table
-- ALTER TABLE telephone DROP not null;


use world;

select * from city
where Population < 1000000;

select * from city
where Population < 100000;

select * from city
where Population > 1000000;

select * from city
where Population >=  1000000;

select * from city
where Population = 1000000;

select * from city
where Population = 500000;

select * from city
where Population != 500000;

select * from city
where Countrycode = "IND";

select * from city
where District = "Madhya Pradesh";

select * from city
where Name = "Indore";

-- and operator
select * from city
where Population > 5000000 and Countrycode = "Ind";

-- or operator
select * from city
where Population > 5000000 or Countrycode = "Ind";

select * from city
where Population > 500000 or 
(Countrycode = "Ind" and Countrycode = "NLD");

select * from city
where Population > 500000 and 
(Countrycode = "Ind" or Countrycode = "NLD");

-- not
select * from city;
 
select * from city
where not Countrycode = "AFG";

select * from city
where not 
(Countrycode = "AFG" or Countrycode = "NLD");

-- in operator
select * from city
where Countrycode in ("Ind","ARG");

-- not in operator
select * from city
where Countrycode not in ("Ind","ARG","AUS");

select * from city
where Countrycode not in ("Ind","ARG","AUS","CHN") 
and Population > 2000000;

-- between operator
select * from country
where LifeExpectancy between 50 and 75; 

/* like 
1) %
2) _
*/
use world;

select * from country
where Region like "C%";

select * from country
where Code like "A%";

select * from country
where Code like "%A";

select * from country
where Code like "%SA";

select * from country
where Continent like "%or%";

select * from country
where Name like "%ther%";

select * from country
where Code like "_RG";

select * from country
where Code like "_R_";

-- set and update statement
use mouse;

update laptop
set price = 45000;

update laptop
set SSD = "512GB";

update laptop
set SSD = "128GB"
where id = 2;

update laptop
set Model = "ASUS", Price = 56000
where id = 1;

select sum(population) from world.country;

select sum(population) from world.country
where Continent = "Asia";

select continent,sum(population) as total_population
from world.country
where Continent = "Asia";

select continent,sum(population) as total_population
from world.country
group by continent;


select continent,sum(population) as total_population
from world.country
group by continent;


select Region,sum(population) as total_population
from world.country
group by region;


select Region,sum(population) as total_population
from world.country
group by Region;

select Region,sum(population) as total_population,
avg(population) as avg_population
from world.country
group by Region;


SELECT countrycode, SUM(population) AS total_pop
FROM world.city
GROUP BY countrycode;

SELECT countrycode, SUM(population) AS total_pop
FROM world.city
GROUP BY countrycode
HAVING total_pop < 200000;

SELECT countrycode, SUM(population) AS total_pop
FROM world.city
GROUP BY countrycode
HAVING total_pop < 200000
ORDER BY countrycode ASC;

SELECT countrycode, SUM(population) AS total_pop
FROM world.city
GROUP BY countrycode
HAVING total_pop < 200000
ORDER BY countrycode DESC;


