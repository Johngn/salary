#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:34:54 2020

@author: john
"""

import salaryscraper as ss
import pandas as pd

path = '/home/john/Desktop/salary/'
slp_time = 2

df = ss.get_jobs('data scientist', 1000, False, path+'chromedriver', slp_time)

df.to_csv(path + 'glassdoor_jobs_large.csv', index=False)
