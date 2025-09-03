-- drop, delete and truncate 

use mouse;

select * from laptop;

-- use delete for removing specific condition based value
delete from laptop
where Id = 4;

delete from laptop
where id = 2;

-- use truncate for remove all data from table
truncate table laptop;

truncate table new_emp_tab;

rollback;

select * from new_emp_tab;

-- use drop for remove table from database
drop table new_emp_tab;

truncate table actor;

select * from actor;


-- commit 
use amazon;

select * from newtable;

start transaction;

insert into newtable value
(5, "Iphone15", "UPI");

commit;

start transaction;

insert into newtable value
(7, "Iphone6", "UPI");

rollback;

start transaction;

delete from newtable
where id = 2;

rollback;

-- concat

use sakila;

select concat(first_name, last_name) from actor;

select first_name, last_name,
concat(first_name," ",last_name) from actor;

select first_name, last_name,
concat(first_name," ",last_name) as full_name 
from actor;

select lower(first_name), last_name from actor;

select trim("   hello world    ");

select left("machine learning",3);

select right("machine learning",3);

select price+500 from amazon.orders;


select * from amazon.orders;

select month(Orderdate) from amazon.orders;

select date(OrderDate) from amazon.orders;

select day(orderdate) from amazon.orders;

select year(orderdate) from amazon.orders;

select distinct(year(orderdate)) from amazon.orders;

select monthname(orderdate) from amazon.orders;

select dayname(orderdate) from amazon.orders;

select distinct(dayname(orderdate)) from amazon.orders;

select count(distinct(dayname(orderdate))) 
from amazon.orders;


select *, monthname(orderdate) as monthname 
from amazon.orders;

select substring_index(orderdate,"-",1) as year,
substring_index(substring_index(orderdate,"-",-2),"-",1) as month,
substring_index(orderdate,"-",-1) as day
from amazon.orders;

