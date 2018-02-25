# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 15:32:59 2018

@author: Scott
"""

import pandas as pd

data1 = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident - a blot of black upon a world of crimson and gold."

path = 'C:\\_scott\\BootCamp\\03-Python\\Homework\\Instructions\\PyParagraph\\raw_data\\paragraph_1.txt'

print(path)
data_line = []
with open(path) as fp:
    for line in fp:
        data_line.append(line)
      
#data = data1
data = data_line[0]
print(len(data))

num_sent = data.count('.') + data.count('?')
num_spaces = data.count(' ')
num_special_char = data.count("'") + data.count('-')+data.count(':')+data.count(',')
len_string = len(data)

#print('number of special char is ' + str(num_special_char))
letter_count = len_string-num_special_char-num_sent
word_count = num_sent + num_spaces + data.count(',')

print('Approximate word count is '+str(num_spaces))
print('Approximate sentence count is '+str(num_sent))
print('Approximate letter count (per word) is '+str(letter_count/word_count))
print('Average sentence length (in words)is '+str(word_count/num_sent))