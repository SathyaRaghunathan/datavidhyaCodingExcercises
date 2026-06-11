"Social Media PII Extraction Pyspark Solution"
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(input_df):
    df = input_df
    df = df.withColumn(
        "anon_phone",
        F.regexp_replace(F.col("phone"),
                         r"^\d{6}","******"))
    df = df.withColumn(
        "email_domain",
        F.regexp_extract(F.col("email"),r"@(.+)",1))
    output_df = df.select(
        "anon_phone","email_domain","user_id")
    return output_df.orderBy(F.col("anon_phone").asc())




    