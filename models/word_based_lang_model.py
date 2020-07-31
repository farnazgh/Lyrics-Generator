#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:55:36 2019

@author: gab
"""

from collections import *
import nltk
# nltk.download('punkt')

order=3 #----------------------------------------------
def train_char_lm( order):
    lm = defaultdict(Counter)
    
    
    with open('folk_country_clean.txt', encoding="UTF8") as content_file:
        data = content_file.read()

    len_data_train = int(len(data) * 0.8)
    train_data = data[0:len_data_train]
    test_data = data[len_data_train:len(data)]


    train_data = train_data.replace("\n", " * ") 
    tokens = nltk.word_tokenize(train_data)

    for i in range(len(tokens)-order):
        history, char = " ".join(tokens[i:i+order]), tokens[i+order]
        lm[history][char]+=1

    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.items()]

    outlm = {hist:normalize(chars) for hist, chars in lm.items()}

    return outlm

#####training the model
lm = train_char_lm( order)

#checking char prediction for order=10
# print(lm)


##-----Generating from model
from random import random

def generate_word(lm, out, order):
        history = out[-order:]
        dist = lm[" ".join(history)]
        x = random()
        for c,v in dist:
            x = x - v
            if x <= 0: return c

# import kenlm
import grammar_check
import string
from random import choice




tool = grammar_check.LanguageTool('en-GB')

def generate_text(lm, order, nwords=100):
    out = ["love", "in", "the"]
    # print(out)
    while len(out)<nwords:
        c = generate_word(lm, out, order)
        

        out.append(c)
        
        

    #grammar    
    text = " ".join(out)
    matches = tool.check(text)
    res = grammar_check.correct(text, matches)
    
    return res


print (generate_text(lm, order)) 

