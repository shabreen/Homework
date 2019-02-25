use sakila; 
##Q1a##
select first_name,last_name
from actor;
##Q1b##
select concat(first_name,' ',last_name) as Actor_Name
from actor;
##Q2a##
Select actor_id, first_name, last_name 
from actor 
where first_name = "Joe";
##Q2b##
select actor_id, first_name, last_name
from actor
where last_name like '%GEN%';
##Q2c##
select last_name, first_name
from actor
where last_name like '%LI%'
order by last_name, first_name;
##Q2d##
select country_id, country
from country
where country in ('Afghanistan','Bangladesh','China');
##Q3a##
select * from actor;
alter table actor
add column description BLOB after last_name;
##Q3b##
select * from actor;
alter table actor
drop column description;
##Q4a##
Select last_name, count(*) as `Count`
from actor
group by last_name;
##Q4b##
Select last_name, count(*) as `Count`
from actor
group by last_name
having count > 1;
##Q4c##
update actor
set first_name = 'Harpo'
where first_name = 'Groucho' and last_name = 'Williams';
##Q4d##
update actor
set first_name = 'Groucho'
where first_name = 'Harpo' and last_name = 'Williams';
##Q5a##
describe sakila.address;
##Q6a##
Select s.first_name, s.last_name, a.address
from staff s left join address a on s.address_id = a.address_id;
##Q6b##
select s.first_name, s.last_name, sum(p.amount) as 'Total'
from staff s inner join payment p on s.staff_id = p.staff_id
where p.payment_date like '2005-08%'
group by s.first_name, s.last_name;
##Q6c##
select f.title, count(a.actor_id) as 'Number of Actors'
from film f inner join film_actor a on f.film_id = a.film_id
group by f.title;
##Q6d##
select f.title, count(i.inventory_id) as 'Number of Copies'
from film f inner join inventory i on f.film_id = i.film_id 
where title = 'HUNCHBACK IMPOSSIBLE';
##Q6e##
select c.first_name, c.last_name, sum(p.amount) as 'Total Amount Paid'
from customer c inner join payment p on c.customer_id = p.customer_id
group by c.first_name, c.last_name
order by c.last_name;
##Q7a##
select title
from film
where (title like 'K%' OR title like 'Q%') 
and language_id = (select language_id from language where name='English');
##Q7b##
select first_name, last_name
from actor 
where actor_id
	in (select actor_id from film_actor where film_id 
		in (select film_id from film where title='ALONE TRIP'));
##Q7c##
select cu.first_name, cu.last_name, cu.email 
from customer cu
join address a on (cu.address_id = a.address_id)
join city cty on (cty.city_id = a.city_id)
join country on (country.country_id = cty.country_id)
where country.country= 'Canada';
##Q7d##
select title
from film f
join film_category fc on (f.film_id = fc.film_id)
join category c on (fc.category_id = c.category_id)
where (select c.category_id where name = 'Family');
##Q7e##
select f.title, count(rental_id) as 'Times Rented'
from rental r
join inventory i on (r.inventory_id = i.inventory_id)
join film f on (i.film_id = f.film_id)
group by f.title
order by `Times Rented` DESC;
##Q7f##
select s.store_id, sum(amount) as 'Revenue' 
from store s
join staff st on s.store_id = st.store_id 
join payment p on p.staff_id = st.staff_id 
group by s.store_id;
##Q7g##
select s.store_id, c.city, co.country
from store s
join address a on (s.address_id = a.address_id)
join city c on (a.city_id = c.city_id)
join country co on (c.country_id = co.country_id);
##Q7h##
select c.name as 'Genre', sum(p.amount) as 'Gross Revenue' 
from category c
join film_category fc on (c.category_id = fc.category_id)
join inventory i on (fc.film_id = i.film_id)
join rental r on (i.inventory_id = r.inventory_id)
join payment p on (r.rental_id = p.rental_id)
group by c.name order by 'Gross Revenue' LIMIT 5;
##Q8a##
create view Top_Five as
select c.name as 'Genre', sum(p.amount) as 'Gross Revenue' 
from category c
join film_category fc on (c.category_id = fc.category_id)
join inventory i on (fc.film_id = i.film_id)
join rental r on (i.inventory_id = r.inventory_id)
join payment p on (r.rental_id = p.rental_id)
group by c.name order by 'Gross Revenue' LIMIT 5;
##Q8b##
select * from Top_Five;
##Q8c##
drop view Top_Five;



































































