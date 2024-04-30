# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:43:54 2023

@author: jkern
"""

import pandas as pd
import datetime
from datetime import datetime

df = pd.read_csv('openweather.csv',header=0)

pd.to_datetime(df['dt'],unit='d')