# access database
use sakila;

# ---- Part I: ---- #
-- SINGLE TABLE QUERIES --
# insert code

-- MULTI TABLE QUERIES --
# Query 1: Get a list of category names and a count of movies that fall into that category. 
# Name the category column “category” the count column “num_films”. Order the results alphabetically (ascending). 
# Use the WHERE clause to join the tables.
SELECT name as category, count(*) as num_films
FROM category, film, film_category
WHERE film_category.film_id = film.film_id AND film_category.category_id = category.category_id
GROUP BY name
ORDER BY name ASC;

# alternative option
SELECT name as category, count(film.film_id) as num_films
FROM category, film, film_category
WHERE film_category.film_id = film.film_id AND film_category.category_id = category.category_id
GROUP BY name
ORDER BY name ASC;

# Query 2: Repeat the query above using a JOIN clause instead of the WHERE clause.
SELECT name as category, count(*) as num_films
FROM film_category JOIN film ON film_category.film_id = film.film_id JOIN category ON film_category.category_id = category.category_id
GROUP BY name
ORDER BY name ASC;

# alternative option
SELECT name as category, count(film.film_id) as num_films
FROM film_category JOIN film ON film_category.film_id = film.film_id JOIN category ON film_category.category_id = category.category_id
GROUP BY name
ORDER BY name ASC;

# Query 3: Get a list of country names and a count of the cities that are in that country. 
# Name the count column “num_cities”. Order the results alphabetically (ascending). 
# Use the WHERE clause to join the tables.
SELECT country, COUNT(city) as num_cities
FROM country, city 
WHERE country.country_id = city.country_id
GROUP BY country
ORDER BY country ASC;

# Query 4: Repeat the query above using a JOIN clause instead of the WHERE clause
SELECT country, COUNT(city) as num_cities
FROM country JOIN city ON country.country_id = city.country_id
GROUP BY country
ORDER BY country ASC;

# Query 5: Get a list of each customer’s last name and first name and the number of rentals they have. Name the count column “num_rentals”. 
# Order the result by the number of rentals in descending order. 
# The highest number of rentals should be at the top. Sort any ties (same number of rentals) by last name (ascending). 
# Use the WHERE clause to join the tables.
SELECT last_name, first_name, COUNT(*) as num_rentals
FROM customer, rental
WHERE customer.customer_id = rental.customer_id
GROUP BY last_name, first_name, customer.customer_id
ORDER BY num_rentals DESC, last_name ASC;

# alternative option
SELECT last_name, first_name, COUNT(rental_id) as num_rentals
FROM customer, rental
WHERE customer.customer_id = rental.customer_id
GROUP BY last_name, first_name, customer.customer_id
ORDER BY num_rentals DESC, last_name ASC;

# Query 6: Repeat the query above using a JOIN clause instead of the WHERE clause.
SELECT last_name, first_name, COUNT(*) as num_rentals
FROM customer JOIN rental ON customer.customer_id = rental.customer_id
GROUP BY last_name, first_name, customer.customer_id
ORDER BY num_rentals DESC, last_name ASC;

# alternative option
SELECT last_name, first_name, COUNT(rental_id) as num_rentals
FROM customer JOIN rental ON customer.customer_id = rental.customer_id
GROUP BY last_name, first_name, customer.customer_id
ORDER BY num_rentals DESC, last_name ASC;

# Query 7: Get a list of each customer’s last name and first name and the amount of money they have spent on rentals. 
# Name the sum column “total_spent”. Order the result by the amount in descending order. 
# The highest amount of money spent should be at the top. Sort any ties (amount of money spent) by last name (ascending). 
# Use the JOIN clause for this query.
SELECT last_name, first_name, SUM(amount) as total_spent
FROM customer JOIN payment ON customer.customer_id = payment.customer_id
GROUP BY last_name, first_name, customer.customer_id
ORDER BY total_spent DESC, last_name ASC;

# Query 8: Get the number of actors in each film. 
# Order the results (ascending) by the film title. 
# Name the column with the actor count “num_actors”.
SELECT title, COUNT(actor.actor_id) as num_actors
FROM actor JOIN film_actor ON actor.actor_id = film_actor.actor_id JOIN film ON film_actor.film_id = film.film_id
GROUP BY title, film.film_id
ORDER BY title ASC;

# Query 9: Get the number of films each manager holds. Use only the manager staff id to identify the manager. 
# Name the column with the number of films “num_films”.


# QUery 10.Get the number of customers per manager. Use only the manager staff id to identify the manager. 
# Name the column with the number of films “num_customers”. Order by store id (ascending).