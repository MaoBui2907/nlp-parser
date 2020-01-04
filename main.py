# coding=utf-8

import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""
S -> NP[sub=?x] VP[sub=?x]

NP[sub=?x, jj=?y, in=?z] -> NN[sub=?x, jj=?y, in=?z]
NP[sub=?x, jj=?y, in=?z] -> NNP[sub=?x, jj=?y, in=?z]
NP[sub=?x, jj=?y, in=?z] -> 

NN[sub=nguoi] -> "tôi"
NN[sub=con_vat] -> "cá"
NN[sub=con_vat] -> "chim"
NN[sub=vat_the] -> "mặt_trời"

NNP[sub=nguoi] -> "Nam"

VP[sub=?x] -> VB[sub=?x]
VB[sub=nguoi] -> "ngủ"
VB[sub=nguoi] -> "ăn"
VB[sub=con_vat] -> "bơi"
VB[sub=con_vat] -> "bay"
VB[sub=vat_the] -> "mọc"
""")

parser = nltk.parse.FeatureChartParser(grammar)

sentences = ["tôi ngủ",
             "cá bơi",
             "chim bay",
             "Nam ăn", 
             "mặt_trời mọc"]

for sent in sentences:
    print(sent)
    words = sent.split()
    for tree in parser.parse(words):
        tree.draw()
