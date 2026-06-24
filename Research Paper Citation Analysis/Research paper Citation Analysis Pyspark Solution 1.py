from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(authors, research_papers):
    df = authors.join(research_papers,on ='paper_id',how = 'inner')
    window = W.partitionBy(F.col('paper_id')).orderBy(
        F.col('author_id').asc())
    df = df.withColumn('row_number',F.row_number().over(window))
    return df.select(
        F.col('author_id'),
        F.col('name'),F.col('paper_id'),F.col('row_number')
    )