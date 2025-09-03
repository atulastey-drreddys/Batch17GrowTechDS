use mouse;

show tables;

create table Student
(Id int Not null,
Name varchar(40),
Age int,
City varchar(40));

create table Mobile
(Id int primary key,
Model varchar(40) not null,
price int not null);

-- insert data into table
insert into Student values
(1,"David",29,"Indore");

select * from Student;

insert into Student values
(2,"Backham",43,"Ujjain");

insert into Student values
(3,"ved",20,"Guna"),
(4,"Jaina",45,"Bhopal"),
(5,"Vikra",44,"Sihor");


insert into Student (Id,Name,City) values
(11,"Rohit","Gwalior");

insert into Student values
(30,"ved",45,"Guna");

create table Laptop
(Id int primary key auto_increment,
Model varchar(40) unique,
price int not null,
SSD varchar(40) default "128GB");

select * From  Laptop;

insert into Laptop values
(1,"Delli7", 60000,"512GB");

insert into Laptop(Model, Price) values
("HPCorei3",70000);

insert into Laptop(Model, Price) values
("HPCorei5",60000);

create table Employee
(Id int Not null,
Name varchar(40),
Age int,
City varchar(40),
check (Age >= 18));

insert into Employee values
(1,"ved",20,"Guna"),
(2,"Jaina",45,"Bhopal"),
(3,"Virat",12,"Delhi"),
(4,"Vikra",44,"Sihor");

insert into Employee values
(1,"ved",20,"Guna"),
(2,"Jaina",45,"Bhopal"),
(3,"Virat",38,"Delhi"),
(4,"Vikra",44,"Sihor");

select * from Employee;

create table Mobile
(Id int primary key,
Model varchar(40) not null,
price int not null);

