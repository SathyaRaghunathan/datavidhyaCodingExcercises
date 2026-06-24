import pandas as pd
import numpy as np
import datetime
import json
import math
import re

def etl(ic_data_1, ic_data_2):
    #write your code here
    df = pd.concat([ic_data_1,ic_data_2],ignore_index =True)
    return df.sort_values(by =['age'],ascending = True)