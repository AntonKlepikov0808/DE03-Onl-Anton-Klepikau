# refresh_marts.py
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='pharmacy_prices',
    user='postgres',
    password='postgres'
)
cur = conn.cursor()

# Витрина current_prices
cur.execute("""
    TRUNCATE TABLE current_prices;
    INSERT INTO current_prices
    SELECT
        ph.pharmacy_id, ph.name, ph.city,
        p.product_id, p.name, p.category, p.manufacturer,
        pr.price, pr.old_price, pr.quantity, pr.discount_percent,
        pr.updated_at
    FROM prices pr
    JOIN pharmacies ph ON pr.pharmacy_id = ph.pharmacy_id
    JOIN products p ON pr.product_id = p.product_id
    WHERE pr.updated_at >= NOW() - interval '1 day';
""")

# Витрина product_price_stats
cur.execute("""
    TRUNCATE TABLE product_price_stats;
    INSERT INTO product_price_stats
    SELECT
        p.product_id, p.name, p.category,
        COUNT(DISTINCT pr.pharmacy_id) as pharmacy_count,
        MIN(pr.price) as min_price,
        MAX(pr.price) as max_price,
        AVG(pr.price)::numeric(10,2) as avg_price,
        SUM(pr.quantity) as total_stock
    FROM prices pr
    JOIN products p ON pr.product_id = p.product_id
    GROUP BY p.product_id, p.name, p.category;
""")

# Витрина pharmacy_stats
cur.execute("""
    TRUNCATE TABLE pharmacy_stats;
    INSERT INTO pharmacy_stats
    SELECT
        ph.pharmacy_id, ph.name, ph.city,
        COUNT(DISTINCT pr.product_id) as product_count,
        AVG(pr.price)::numeric(10,2) as avg_price,
        SUM(pr.quantity) as total_stock
    FROM prices pr
    JOIN pharmacies ph ON pr.pharmacy_id = ph.pharmacy_id
    GROUP BY ph.pharmacy_id, ph.name, ph.city;
""")

conn.commit()
cur.close()
conn.close()