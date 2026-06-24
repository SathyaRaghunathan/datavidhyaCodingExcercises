import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(authors, research_papers):
    df = authors.merge(research_papers,on = ['paper_id'],how = 'inner')
    df['row_number'] = (df.groupby('paper_id')['author_id'].rank(method='first',ascending=True).astype(int) )
    return df[['author_id','name','paper_id','row_number']]