create table item (
id int primary key,
desk varchar(50),
price float
);

create table custumer (
id int primary key,
first_name varchar(50),
last_name varchar(50)
);

insert into item (id, desk, price) values
(1, 'small desk', 100),
(2, 'large desk', 300),
(3, 'fan', 80);

insert into custumer (id, first_name, last_name) values
(1, 'Greg', 'Jones'),
(2, 'Sandra', 'Jones'),
(3, 'Scott', 'Scott'),
(4, 'Trevor', 'Green'),
(5, 'Melanie', 'Johnson');

select * from item;

select * from item where price > 80;

select * from item where price < 300;

select * from custumer where last_name = 'Smith';

select * from custumer where last_name = 'Jones';

select * from custumer where first_name != 'Scott';