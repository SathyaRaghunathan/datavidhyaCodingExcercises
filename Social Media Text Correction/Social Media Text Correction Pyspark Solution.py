from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(social_media):
    # Write code here
    df = social_media
    df = df.withColumn('text',F.regexp_replace(F.col('text'),'Python','PySpark')
                      )
    output = df.select('comments','date','id','likes','platform',
                      'shares','text')
    return output.orderBy('comments')