SELECT * FROM public.customer
ORDER BY customer_id ASC 


select first_name || ' ' || last_name AS full_name
from customer


select distinct create_date from customer;

select * from customer
order by first_name ASC;


select film_id, title, description, release_year, rental_rate from film
order by rental_rate ASC;


select address, phone from address
where district = 'Texas';

select * from film
where film_id=15 or film_id=150;

select film_id, title, description, length from film 
where title = 'Titanic'

select film_id, title, description, length from film 
where title like 'Ti%'


select * from film
order by rental_rate ASC
limit 10;


select * from film
order by rental_rate ASC
limit 10 offset 10;

select customer.customer_id, customer.first_name, customer.last_name, payment.payment_date, payment.amount
from customer inner join payment on payment.customer_id = customer.customer_id
order by customer.customer_id ASC;

select * from film join inventory on film.film_id=inventory.film_id where film.film_id not in (inventory.film_id);

select city.city, country.country from city join country on city.country_id = country.country_id;