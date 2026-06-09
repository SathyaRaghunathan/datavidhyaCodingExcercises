'Pandas Solution'
import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(video_stream_df):
    curr_year = pd.Timestamp.now().year
    df1 = video_stream_df
    df1 = df1[ (df1['view_count']>1000000) &
    (df1['release_year']>= curr_year -8)]
    output_df = df1[['duration','genre','release_year',
              'title','video_id','view_count']].sort_values(
        by = ['duration'],ascending = True
              )
    
    return output_df
