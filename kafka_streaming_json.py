import time

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName("Kafka_streaming") \
    .master("local") \
    .getOrCreate()

kafka_topic_name = "my-topic"
kafka_bootstrap_servers = "localhost:9092"

print(time.strftime("%Y-%m-%d %H:%M:%S"))

spark.sparkContext.setLogLevel("ERROR")

order_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
        .option("subscribe", kafka_topic_name) \
        .option("startingOffsets", "latest") \
        .load()

order_df.printSchema()

order_df1 = order_df.selectExpr("CAST(value AS STRING)", "timestamp")

orders_schema = StructType() \
    .add("order_id", StringType()) \
    .add("order_product_name", StringType()) \
    .add("order_card_type", StringType()) \
    .add("order_amount", StringType()) \
    .add("order_datetime", StringType()) \
    .add("order_country_name", StringType()) \
    .add("order_city_name", StringType()) \
    .add("order_ecommerce_website_name", StringType())

order_df2 = order_df1\
    .select(from_json(col("value"), orders_schema)\
            .alias("orders"), "timestamp")

order_df3 = order_df2.select("orders.*", "timestamp")
order_df3.printSchema()

order_df4 = order_df3.groupBy("order_country_name", "order_city_name") \
    .agg({'order_amount': 'sum'}) \
    .select("order_country_name", "order_city_name", col("sum(order_amount)") \
    .alias("total_order_amount"))

order_df4.printSchema()

order_agg_write_stream = order_df4 \
                        .writeStream \
                        .trigger(processingTime = '5 seconds') \
                        .outputMode("update") \
                        .option("truncate", "false") \
                        .format("console") \
                        .start()

order_agg_write_stream.awaitTermination()