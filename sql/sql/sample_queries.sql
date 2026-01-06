SELECT COUNT(*) AS total_rows FROM transactions;

SELECT
  name,
  SUM(amount) AS total_amount
FROM transactions
GROUP BY name;
