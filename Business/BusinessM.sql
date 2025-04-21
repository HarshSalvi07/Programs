create database Business;
use Business;
create table Records
(Employee_ID int primary key,
Name varchar(30),
DOJ date,
DOP date,
DOR date,
Material varchar(30),
Amount int);
desc Records;
select*from Records;

insert into Records
(Employee_ID,Name,DOJ,DOP,DOR,Material,Amount)
values(001,"Patil","2025-05-01","2025-05-01","2025-05-03","Beads",5);
select*from Records;
show databases;

update Records set DOR = "2025-05-06" where Employee_ID = 1 ;