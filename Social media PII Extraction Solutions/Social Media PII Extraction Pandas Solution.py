"Social Media PII Extraction Pandas Solution"
import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(input_df):
    # Write code here
    df = input_df
    df['anon_phone'] = df['phone'].astype(str).apply(lambda x: '******' + x[-4:])
    df['email_domain'] = df['email'].str.split('@').str[1]
    output_df = df[['anon_phone','email_domain','user_id']]
    return output_df.sort_values(by = ['anon_phone'],ascending = True)