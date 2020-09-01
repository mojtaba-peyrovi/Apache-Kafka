# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:05:02 2020

@author: "mojtaba@heroleads.com"
"""

from pyspark.sql import SparkSession
import kafka

# # Spark Session
# spark = SparkSession.builder.master("local[*]").appName('mykafka').getOrCreate()
# # .config('spark.jars', 'C:\\Users\\hero144\\Desktop\\e-learning\\apache-kafka\\First-Kafka-for-Beginners\\spark_app\\spark-sql-kafka-0-10_2.11-2.1.0.jar,C:\\Users\\hero144\\Desktop\\e-learning\\apache-kafka\\First-Kafka-for-Beginners//spark_app//kafka-clients-1.1.0.jar')\




# df = spark \
#   .readStream \
#   .format("kafka")\
#   .option("kafka.bootstrap.servers", "localhost:9092") \
#   .option("subscribe", "weather-report") \
#   .load()

# df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")


# df = spark.readStream.format('kafka').option("kafka.bootstrap.servers","localhost:9092").option('subscribe','weather-report').load() 


from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json





sc = SparkContext(appName="PythonSparkStreamingKafka_RM_02")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 5)

kafkaStream = KafkaUtils.createStream(ssc, "locahost:2181","weather-report")

parsed = kafkaStream.map(lambda v: json.loads(v[1]))

print(parsed)


