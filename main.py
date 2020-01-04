# coding=utf-8

import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""
S -> NP[rn=?x] VP[rn=?x]

NP[rn=?x, jj=?y] -> NN[rn=?x, jj=?y]
NP[rn=?x, jj=?y] -> NNP[rn=?x, jj=?y]
NP[rn=?x, jj=?y] -> PRP[rn=?x, jj=?y]
NP[rn=?x, jj=?y] -> UNN[rn=?x] NN[rn=?x, jj=?y]

NP[rn=?x, jj=?y] -> NP1[rn=?x, jj=?y] JJ[rn=?x, jj=?y]
NP1[rn=?x, jj=?y] -> NN[rn=?x, jj=?y]
NP1[rn=?x, jj=?y] -> NNP[rn=?x, jj=?y]
NP1[rn=?x, jj=?y] -> PRP[rn=?x, jj=?y]
NP1[rn=?x, jj=?y] -> UNN[rn=?x] NN[rn=?x, jj=?y] 

VP[rn=?x] -> VB[rn=?x]
VP[rn=?x] -> VB[rn=?x, rd=?y] NP[rn=?y]

PRP[rn=nguoi] -> "tôi"

NNP[rn=nguoi] -> "Nam"

UNN[rn=dong_vat] -> "con"
UNN[rn=dong_vat] -> "đàn"

NN[rn=dong_vat] -> "cá"
NN[rn=dong_vat] -> "chim"
NN[rn=vat_the] -> "mặt_trời"
NN[rn=thuc_vat] -> "cỏ"
NN[rn=dong_vat] -> "voi"
NN[rn=do_vat] -> "xe"
NN[rn=do_vat] -> "xương"
NN[rn=dong_vat, jj=den] -> "mèo"
NN[rn=dong_vat, jj=gay] -> "ngựa"
NN[rn=dong_vat, jj=nho] -> "kiến"
NN[rn=dong_vat, jj=nho] -> "chó"
NN[rn=dong_vat, jj=vang] -> "nai"

JJ[jj=den] -> "đen"
JJ[jj=gay] -> "gầy"
JJ[jj=nho] -> "nhỏ"
JJ[jj=vang] -> "vàng"

VB[rn=nguoi] -> "ngủ"
VB[rn=nguoi] -> "chơi"
VB[rn=dong_vat] -> "bơi"
VB[rn=dong_vat] -> "bay"
VB[rn=vat_the] -> "mọc"
VB[rn=dong_vat, rd=dong_vat] -> "tấn_công"
VB[rn=dong_vat, rd=dong_vat] -> "ăn"
VB[rn=dong_vat, rd=do_vat] -> "kéo"
VB[rn=dong_vat, rd=do_vat] -> "gặm"
VB[rn=dong_vat, rd=thuc_vat] -> "ăn"
""")

parser = nltk.parse.FeatureChartParser(grammar)

sentences_1 = ["tôi ngủ",
               "cá bơi",
               "chim bay",
               "Nam chơi",
               "mặt_trời mọc"]

sentences_2 = ["đàn kiến nhỏ tấn_công con voi",
               "con mèo đen ăn cá",
               "con ngựa gầy kéo xe",
               "con chó nhỏ gặm xương",
               "con nai vàng ăn cỏ"]

tests = ["con chó nhỏ ăn cỏ"]

for sent in sentences_1:
    print(sent)
    words = sent.split()
    for tree in parser.parse(words):
        tree.draw()
