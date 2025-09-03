create database Amazon;

use Amazon;

create table Orders
(Id Int Primary key,
Name varchar(50) not null,
Price float,
OrderDate Date); 

create table Payment
(Id Int Primary key auto_increment,
PaymantMode varchar(50),
PaymentDate date);

insert into Orders values
(1,"VivoV20", 25000,"2025-08-20"),
(2,"SamSung s24", 100000, "2025-03-25"),
(3,"Iphone16", 125000, "2025-02-22"),
(4,"Realme",20000, "2025-03-15"),
(6,"Xiomi",26000, "2025-05-20");

insert into Payment values
(2,"UPI","2025-08-25"),
(3,"Cash","2025-03-29"),
(4,"Cash","2025-02-28"),
(5,"Cash","2025-05-12");

-- join
select orders.id,orders.name,
payment.paymantmode
from orders
join payment
on orders.id = payment.id;

select *
from orders
join payment
on orders.id = payment.id;

create table NewTable 
(select orders.id,orders.name,
payment.paymantmode
from orders
join payment
on orders.id = payment.id);

-- inner join
select orders.id,orders.name,
payment.paymantmode
from orders
inner join payment
on orders.id = payment.id;

-- left 
select orders.id,orders.name,
payment.paymantmode
from orders
left join payment
on orders.id = payment.id;

select orders.id,orders.name,
payment.paymantmode
from orders
right join payment
on orders.id = payment.id;

select *
from orders
right join payment
on orders.id = payment.id;

select orders.id,orders.name,
payment.paymantmode
from orders
cross join payment
on orders.id = payment.id;






use world;
select city.countrycode,
countrylanguage.language
from city
join countrylanguage
on city.countrycode = countrylanguage.countrycode;

use world;

select city.countrycode,
countrylanguage.language,
country.surfacearea
from city
join countrylanguage
on city.countrycode = countrylanguage.countrycode
join country on city.countrycode = country.code;

select city.countrycode,
countrylanguage.language,
country.surfacearea
from city
join countrylanguage
on city.countrycode = countrylanguage.countrycode
join country on city.countrycode = country.code
where country.code = "IND";

select country.code, country.surfacearea,
countrylanguage.language
from country
join countrylanguage
on country.code = countrylanguage.countrycode
where country.code = "Ind";

-- limit and offset

select * from country;

select * from country
limit 5;

select * from country
limit 5 offset 1;

select * from country
limit 5 offset 2;

select * from country
order by population desc
limit 5;

select * from country
order by population desc
limit 5; 

select * from country
order by population desc
limit 2;
select * from country
order by population desc
limit 1 offset 1;

select * from country
order by population desc
limit 2;
select * from country
order by population asc
limit 10;

select * from country
order by population desc
limit 2;


select * from country
order by population asc
limit 1 offset 1;

select * from country
where population > 0
order by population asc
limit 1;

select * from country
where population > 0
order by population asc
limit 1 offset 1;

select Continent, sum(population) as total_pop
from country
group by continent
order by total_pop desc;

select Continent, sum(population) as total_pop
from country
group by continent
order by total_pop desc
limit 1 offset 1;

select Continent, sum(population) as total_pop
from country
group by continent
order by total_pop asc
limit 1 offset 1;

-- subquery

select continent, avg(population) as avg_pop
from country
group by continent
order by avg_pop desc;

select avg(population) 
from country;

select Name, population
from country
where population > (select avg(population) 
from country);

select continent, population
from country
where population > (select avg(population) 
from country);

select Name,Population
from city
where population > (select max(population) 
from city where countrycode = "Aus");

select Name,Population
from city
where population > (select max(population) 
from city where countrycode = "Ind");

select * from city
where countrycode = "Ind";

select countrycode, count(language) from countrylanguage
group by countrycode 
having count(language) in  
			(select count(language) from countrylanguage
			group by countrycode
			having count(language) > 10);
            
            
-- case statement

select countrycode,avg(population) from city
group by countrycode;

select countrycode, population, 
case 
when population > 600000 then "Higher Population"
when population < 600000 then "Lower Population"
else "Average Population"
end "Population Category"
from city;

