# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 15:40:51 2018

@author: Scott
"""

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

import pandas as pd

path = "C:\\_scott\\BootCamp\\03-Python\\Homework\\Generators\\PyBoss\\"
# employee_data1.csv

file = 'employee_data1.csv'

data = pd.read_csv(path + file)

#Emp ID,First Name,Last Name,DOB,SSN,State

data[['First Name','Last Name']] = data['Name'].str.split(' ',expand=True)
data[['SSN_1','SSN_2','SSN_3']] = data['SSN'].str.split('-',expand=True)
data['SSN_1'] = 'xxx-'
data['SSN_2'] = 'xx-'
data['SSN_out'] = data['SSN_1']  + data['SSN_2'] + data['SSN_3']
data['DOB_out_formated'] = pd.to_datetime(data.DOB).dt.strftime('%m/%d/%Y')
data['State_abv'] = data['State'].apply(lambda x:us_state_abbrev[x])
out = data[['Emp ID','First Name','Last Name','DOB_out_formated','SSN_out','State_abv']]
out.to_csv(path+'out.csv',index=False)
