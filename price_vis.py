# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]

for y in years:
    
    fn = 'WECC/results/persistence/duals' + str(y) + '.csv'
    
    df = pd.read_csv(fn)
    
    fn2 = 'WECC/results/synthetic/duals' + str(y) + '.csv'
    
    df2 = pd.read_csv(fn2)
    
    buses = list(df['Bus'].unique())
    
    plt.figure()
    
    for b in buses:
        
        s = df.loc[df['Bus'] == b,'Value']
        s = s.reset_index(drop=True)
        
        s2 = df2.loc[df2['Bus'] == b,'Value']
        s2 = s2.reset_index(drop=True)
        
        d = s.values - s2.values
        
        plt.plot(d)

    plt.ylim(-4,4)    
    
    fn2 = str(y) + '.png'
    plt.savefig(fn2,dpi=200)