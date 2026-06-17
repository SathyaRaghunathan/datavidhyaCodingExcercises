from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(calls_df, customers_df):
    join_df = calls_df.join(customers_df,how = 'inner',
                           on ='cust_id')
    join_df = join_df.select(F.col('date').cast('date'),
                            F.col('cust_id').cast('int'),
                            F.col('duration').cast('int'))
    output = join_df.groupBy(F.col('date')).agg(
    F.countDistinct('cust_id').alias("num_customers")
    ,F.sum('duration').alias('total_duration'))
    
    return output.orderBy('date')

    