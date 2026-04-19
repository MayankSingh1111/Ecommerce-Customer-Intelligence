-- create Database

CREATE DATABASE Ecommerce;

USE Ecommerce;

-- create tables --

-- customer_dim

CREATE TABLE customer_dim (
    customer_key VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100),
    contact_no VARCHAR(20),
    nid VARCHAR(20)
);
-- FACT_TABLE --

CREATE TABLE fact_table (
    payment_key VARCHAR(20),
    customer_key VARCHAR(20),
    time_key VARCHAR(20),
    item_key VARCHAR(20),
    store_key VARCHAR(20),
    quantity INT,
    total_price FLOAT
);

-- item_dim

CREATE TABLE item_dim (
    item_key VARCHAR(20) PRIMARY KEY,
    item_name VARCHAR(255),
    description VARCHAR(255),
    unit_price FLOAT,
    man_country VARCHAR(100),
    supplier VARCHAR(255),
    unit VARCHAR(50)
);

-- store_dim

CREATE TABLE store_dim (
    store_key VARCHAR(20) PRIMARY KEY,
    division VARCHAR(100),
    district VARCHAR(100),
    upazila VARCHAR(100)
);


-- time_dim

CREATE TABLE time_dim (
    time_key VARCHAR(20) PRIMARY KEY,
    full_date DATETIME,
    hour INT,
    day INT,
    week INT,
    month INT,
    quarter INT,
    year INT
);

-- trans_dim

CREATE TABLE trans_dim (
    payment_key VARCHAR(20) PRIMARY KEY,
    trans_type VARCHAR(50),
    bank_name VARCHAR(255)
);


select name from sys.tables;

select * from fact_table;


SELECT COUNT(*) FROM customer_dim;
SELECT COUNT(*) FROM fact_table;