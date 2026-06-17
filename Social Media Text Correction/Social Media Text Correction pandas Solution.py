import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(social_media):
    df = social_media
    df['text'] = df['text'].apply(
        lambda x: re.sub('Python','PySpark',str(x))
                                 )
    columns = ['comments','date','id','likes','platform',
              'shares','text']
    output = df[columns]
    return output.sort_values(by = ['comments']).reset_index(drop=True)
    return output

    