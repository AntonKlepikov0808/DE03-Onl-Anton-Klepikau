-- Создание базы данных
CREATE DATABASE pharmacy_prices;
\c pharmacy_prices;

-- Таблица сырых данных (staging)
CREATE TABLE raw_data (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    source VARCHAR(50),
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed BOOLEAN DEFAULT FALSE,
    error_message TEXT
);

-- Измерения (core)
CREATE TABLE pharmacies (
    pharmacy_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    city VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(300) NOT NULL,
    category VARCHAR(100),
    manufacturer VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица фактов (core)
CREATE TABLE prices (
    id BIGSERIAL PRIMARY KEY,
    pharmacy_id VARCHAR(50) REFERENCES pharmacies(pharmacy_id),
    product_id VARCHAR(50) REFERENCES products(product_id),
    price DECIMAL(10,2) NOT NULL CHECK (price > 0),
    old_price DECIMAL(10,2),
    quantity INTEGER DEFAULT 0,
    discount_percent INTEGER DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_prices_pharmacy ON prices(pharmacy_id);
CREATE INDEX idx_prices_product ON prices(product_id);

-- Витрины (marts)
CREATE TABLE current_prices (
    pharmacy_id VARCHAR(50),
    pharmacy_name VARCHAR(200),
    city VARCHAR(100),
    product_id VARCHAR(50),
    product_name VARCHAR(300),
    category VARCHAR(100),
    manufacturer VARCHAR(200),
    price DECIMAL(10,2),
    old_price DECIMAL(10,2),
    quantity INTEGER,
    discount_percent INTEGER,
    updated_at TIMESTAMP
);

CREATE TABLE product_price_stats (
    product_id VARCHAR(50),
    product_name VARCHAR(300),
    category VARCHAR(100),
    pharmacy_count INTEGER,
    min_price DECIMAL(10,2),
    max_price DECIMAL(10,2),
    avg_price DECIMAL(10,2),
    total_stock INTEGER
);

CREATE TABLE pharmacy_stats (
    pharmacy_id VARCHAR(50),
    pharmacy_name VARCHAR(200),
    city VARCHAR(100),
    product_count INTEGER,
    avg_price DECIMAL(10,2),
    total_stock INTEGER
);