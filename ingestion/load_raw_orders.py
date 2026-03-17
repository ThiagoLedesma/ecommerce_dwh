import json
import psycopg2
from pathlib import Path

DB_CONFIG = {
    "dbname": "ecommerce_dwh",
    "user": "thiago",
    "password": "Thiago_2004",
    "host": "localhost",
    "port": 5432
}

def main():
    # Ruta al archivo JSON
    base_path = Path(__file__).resolve().parent.parent
    json_path = base_path / "data" / "raw" / "orders.json"

    # Leer JSON
    with open(json_path, "r") as f:
        orders = json.load(f)

    # Conexión a Postgres
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    insert_query = """
        INSERT INTO raw_orders (order_data)
        VALUES (%s)
    """

    for order in orders:
        cur.execute(insert_query, (json.dumps(order),))

    conn.commit()

    print(f"Inserted {len(orders)} orders into raw_orders.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
