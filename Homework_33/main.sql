CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    store_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price REAL
);

INSERT INTO Sales (product_id, store_id, sale_date, quantity, price)
VALUES
  (1, 1, '2024-01-01', 10, 20.5),
  (2, 2, '2024-01-02', 5, 15.0),
  (1, 1, '2024-01-03', 8, 18.0),
  (3, 3, '2024-02-01', 15, 25.5),
  (2, 2, '2024-02-02', 7, 16.0),
  (1, 1, '2024-02-03', 12, 22.0),
  (3, 3, '2024-03-01', 20, 30.0),
  (2, 2, '2024-03-02', 10, 17.5),
  (1, 1, '2024-03-03', 15, 25.0);
  

--1. Найти общее количество проданных товаров за весь период.
SELECT SUM(quantity) AS total_quantity
FROM Sales;


--2. Рассчитать общую сумму выручки за весь период.
SELECT SUM(price * quantity) AS total_revenue
FROM Sales;


--3. Найти среднее количество проданных товаров в одной транзакции.
SELECT AVG(quantity) AS average_quantity_per_transaction
FROM Sales;


--4. Определить самый популярный товар (товар с наибольшим количеством продаж).
SELECT product_id, SUM(quantity) AS total_quantity_sold
FROM Sales
GROUP BY product_id
ORDER BY total_quantity_sold DESC
LIMIT 1;


--5. Найти общее количество уникальных товаров, проданных в каждом магазине.
SELECT store_id, COUNT(DISTINCT product_id) AS unique_products_sold
FROM Sales
GROUP BY store_id;


--6. Рассчитать общее количество продаж по месяцам.
SELECT strftime('%m', sale_date) AS month, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY strftime('%m', sale_date);


--7. Найти месяц с наибольшим объемом продаж.
SELECT strftime('%m', sale_date) AS month, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY strftime('%m', sale_date)
ORDER BY total_quantity DESC
LIMIT 1;


--8. Рассчитать общую сумму выручки и количество проданных товаров для каждого магазина.
SELECT store_id, SUM(quantity) AS total_quantity, SUM(price * quantity) AS total_revenue
FROM Sales
GROUP BY store_id;


--9. Определить магазин с наибольшим и наименьшим объемом продаж.
-- для наибольшего объема продаж
SELECT store_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY store_id
ORDER BY total_quantity DESC
LIMIT 1;

-- для наименьшего объема продаж
SELECT store_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY store_id
ORDER BY total_quantity ASC
LIMIT 1;

-- для наименьшего объема продаж
SELECT store_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY store_id
ORDER BY total_quantity ASC
LIMIT 1;


--10. Рассчитать средний чек (среднюю сумму покупки) в каждом магазине.
SELECT store_id, AVG(price * quantity) AS average_transaction_amount
FROM Sales
GROUP BY store_id;


--11. Определить товары, проданные только в определенном магазине.
SELECT product_id
FROM Sales
GROUP BY product_id
HAVING COUNT(DISTINCT store_id) = 1;






