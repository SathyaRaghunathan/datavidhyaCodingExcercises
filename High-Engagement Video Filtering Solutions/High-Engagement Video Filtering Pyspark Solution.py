'Pyspark Solution'
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(video_stream_df):
    df1 = video_stream_df
    current_year = F.year(F.current_date())
    df2 = df1.filter( (F.col('view_count')>1000000) &
                    (F.col('release_year') > current_year -8)
                    )
    output_df = df2.select('duration','genre','release_year',
                          'title','video_id','view_count')
    return output_df.orderBy(F.col('duration').asc())