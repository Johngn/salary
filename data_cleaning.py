#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:36:54 2020

@author: john
"""
# %%
import pandas as pd

path = '/home/john/Desktop/salary/'

df = pd.read_csv('glassdoor_jobs_large.csv')

# salary parsing
# company name text only
# state field
# age of company
# parsing of job description
        
contains_comma = df['Location'].apply(lambda x: x.find(','))

df = df[contains_comma != -1]
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
is_state = df.job_state.apply(lambda x: len(x) == 3)
df = df[is_state]

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
salary_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

# calculate salary
df['min_salary'] = salary_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = salary_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary']+df['max_salary'])/2

df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)


df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

# age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - int(x))

# parse job description
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['r'] = df['Job Description'].apply(lambda x: 1 if ' r ' in x.lower() else 0)
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.to_csv(path + 'glassdoor_jobs_large_clean.csv', index=False)
