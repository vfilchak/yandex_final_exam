# SQL-запросы

## Задание 1
SELECT c.login, COUNT(o.id)
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery"
GROUP BY c.login;

## Задание 2
SELECT 
    track,
    CASE
        WHEN finished THEN 2
        WHEN cancelled THEN -1
        WHEN "inDelivery" THEN 1
        ELSE 0 
    END AS status
FROM "Orders";