SELECT
    id,
    ingestion_timestamp,
    order_data->>'order_id' AS order_id,
    order_data->>'customer' AS customer,
    (order_data->>'amount')::numeric AS amount
FROM raw_orders
