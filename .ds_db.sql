-- MySQL script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS dish_share_db;
CREATE USER IF NOT EXISTS 'ds_user'@'localhost' IDENTIFIED BY 'adelelb15';
GRANT ALL PRIVILEGES ON dish_share_db.* TO 'ds_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'ds_user'@'localhost';