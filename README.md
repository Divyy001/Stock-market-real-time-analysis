Project Overview

This project demonstrates a real-time stock market analysis system designed to handle and process streaming data. The system utilizes Apache Kafka for data streaming, Apache Spark Streaming for real-time data processing, and MySQL for data storage. The final data is visualized using Power BI, providing dynamic and interactive insights into stock market trends.
Objectives

- Real-Time Data Ingestion: Stream stock market data from CSV files to Kafka.
- Real-Time Data Processing: Process the streaming data with Apache Spark to perform necessary transformations.
- Persistent Storage: Store the processed data in a MySQL database.
- Visualization: Create a real-time dashboard in Power BI to visualize the stock market trends.

Components
1. Apache Kafka

    Role: Acts as the data pipeline for real-time data streaming.
    Configuration: Topics are set up to handle incoming stock market data.

2. Apache Spark Streaming

    Role: Processes the incoming streaming data in real-time.
    Functionality: Transforms raw data from Kafka, extracts relevant fields, and processes it for storage.
    Operations: Data is parsed, cleaned, and formatted to fit the schema required for MySQL.

3. MySQL Database

    Role: Stores the processed data from Spark Streaming.
    Configuration: A dedicated database and table are created to accommodate the stock market data.

4. Power BI

    Role: Provides real-time visualization of the stock market data.
    Functionality: Connects to MySQL to fetch data and display it dynamically through interactive dashboards.

Implementation
Kafka Producer

The Kafka producer script reads stock market data from CSV files and publishes it to a Kafka topic. This script ensures that data is continuously pushed to Kafka for processing.

Key Script: kafka_producer.py

- Reads CSV files containing stock market data.
- Formats data into JSON and sends it to Kafka.
- Handles multiple CSV files by iterating through them and pushing each record to the Kafka topic.

Spark Streaming Application

The Spark Streaming application reads data from the Kafka topic, processes it, and writes the processed data to MySQL. It performs the following operations:

Key Script: spark_streaming.py

    Reads from Kafka using Spark's structured streaming API.
    Parses and processes the data, extracting fields such as timestamp, bank name, open price, high price, low price, close price, and volume.
    Formats the data and writes it to a MySQL table.

MySQL Database

The MySQL database is used to store the processed data for long-term storage and querying. The database schema is designed to match the processed data format.

Setup SQL:

sql

CREATE DATABASE stock_market;
USE stock_market;
CREATE TABLE stock_data (
    Timestamp DATETIME,
    Bank_Name VARCHAR(255),
    Open DECIMAL(10,2),
    High DECIMAL(10,2),
    Low DECIMAL(10,2),
    Close DECIMAL(10,2),
    Volume DECIMAL(10,2)
);

Power BI Dashboard

Power BI connects to the MySQL database to create a real-time dashboard. It visualizes key metrics such as stock prices and trading volume, providing interactive and insightful views into the data.

Key Steps:

    Connect to MySQL database from Power BI.
    Design interactive dashboards to display real-time stock market trends.
    Update dashboards dynamically as new data arrives.

Setup and Execution

    Start Kafka and Zookeeper:
        Initialize and start Kafka and Zookeeper services.

    Create Kafka Topics:
        Set up the necessary Kafka topics to handle the stock market data.

    Run the Kafka Producer:
        Execute the Kafka producer script to start streaming data.

    Run the Spark Streaming Application:
        Submit the Spark job to process the streaming data and store it in MySQL.

    Configure MySQL Database:
        Create the database and tables needed for storing the data.

    Set Up Power BI:
        Connect Power BI to the MySQL database and create real-time dashboards.

Conclusion

This project effectively demonstrates the ability to integrate multiple technologies for real-time data processing and visualization. It provides a comprehensive solution for analyzing stock market data in real-time, showcasing skills in data engineering, real-time streaming, and data visualization.

