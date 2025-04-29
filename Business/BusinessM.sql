create database Business;
use Business;
create table Records
(DOE date primary key,
Name varchar(30),
Employee_ID int,
DOP date,
DOR date,
Material varchar(30),
Amount int);
desc Records;
select*from Records;
