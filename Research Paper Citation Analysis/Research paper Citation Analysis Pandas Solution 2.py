import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(authors, research_papers):
    df = authors.merge(research_papers,on = 'paper_id',how = 'inner')
    df = df.sort_values(by =['paper_id','author_id'],ascending = [True,True])
    df['row_number'] = df.groupby('paper_id').cumcount() +1
    return df[['author_id','name','paper_id','row_number']]