# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:05:02 2020

@author: "mojtaba@heroleads.com"
"""

from pyspark.sql import SparkSession
import kafka

# Spark Session
spark = SparkSession.builder.appName('kafka').getOrCreate()
# .config('spark.jars', 'C:\\Users\\hero144\\Desktop\\e-learning\\apache-kafka\\First-Kafka-for-Beginners\\spark_app\\spark-sql-kafka-0-10_2.11-2.1.0.jar,C:\\Users\\hero144\\Desktop\\e-learning\\apache-kafka\\First-Kafka-for-Beginners//spark_app//kafka-clients-1.1.0.jar')\




df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "weather-report") \
  .load()

df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")


# df = spark.readStream.format('kafka').option("kafka.bootstrap.servers","localhost:9092").option('subscribe','weather-report').load() 


