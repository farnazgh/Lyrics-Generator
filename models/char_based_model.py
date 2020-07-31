#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:55:36 2019

@author: gab
"""


#------Unsmoothed Maximum Likelihood Character Level Language Model (https://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139)
from collections import *

order=10 #---------------------------------

def train_char_lm( order):
    lm = defaultdict(Counter)
    
    pad = "~" * order
    with open('folk_country_clean.txt', encoding="UTF8") as content_file:
        data = content_file.read()
    

    len_data_train = int(len(data) * 0.8)
    train_data = data[0:len_data_train]
    test_data = data[len_data_train:len(data)]


    train_data = pad + train_data 
    train_data = train_data.replace("\n", " * ")
    
    for i in range(len(train_data)-order):
        history, char = train_data[i:i+order], train_data[i+order]
        lm[history][char]+=1

    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.items()]

    outlm = {hist:normalize(chars) for hist, chars in lm.items()}
    return outlm

#####training the model
lm = train_char_lm( order)

#checking char prediction for order=10
#lm[' i know yo']


##-----Generating from model
from random import random

def generate_letter(lm, history, order):
        history = history[-order:]
        if history in lm:
            dist = lm[history]
        else:
            return "~" 
        x = random()
        for c,v in dist:
            x = x - v
            if x <= 0: return c

# import kenlm
import grammar_check
import string
from random import choice




tool = grammar_check.LanguageTool('en-GB')

def generate_text(lm, order, nletters=1000):
    history = "~" * order
    out = ["~"]* order
    
    while len(out)<nletters:
        c = generate_letter(lm, history, order) 

        
        out.append(c)
        history = "".join(out[-order:])
        	

    #grammar    
    text = "".join(out[order:])
    matches = tool.check(text)
    res = grammar_check.correct(text, matches)
    
    return res



print (generate_text(lm, order))  
