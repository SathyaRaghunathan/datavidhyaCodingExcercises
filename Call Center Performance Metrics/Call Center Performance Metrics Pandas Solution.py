import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(calls_df, customers_df):
    df = calls_df.merge(customers_df,on ='cust_id',how = 'inner')
    output = df.groupby('date').agg(
        num_customers = ('cust_id','nunique'),
        total_duration = ('duration','sum')
    )
    return output.reset_index(inplace =False)