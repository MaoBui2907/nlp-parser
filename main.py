# coding=utf-8

import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""
S -> NP[rn=?x] VP[rn=?x]

NP[rn=?x, jj=?y, in=?z] -> NN[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> NNP[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> PRP[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> UNN[rn=?x] NN[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> NP[rn=?x, jj=?y, in=?z] JJ[jj=?y]

NP[rn=?x, jj=?y, in=?z] -> NP2[rn=?x, jj=?y, in=?z] JJ[jj=?y]
NP[rn=?x, jj=?y, in=?z] -> NP2[rn=?x] PP[]
NP[rn=?x, jj=?y, in=?z] -> NP2[rn=?x, jj=?y, in=?z] JJ[jj=?y]
NP2[rn=?x, jj=?y, in=?z] -> NP1[rn=?x] PP[]
NP2[rn=?x, jj=?y, in=?z] -> NP1[rn=?x, jj=?y, in=?z] JJ[jj=?y]
NP2[rn=?x, jj=?y, in=?z] -> NN[rn=?x, jj=?y, in=?z]
NP2[rn=?x, jj=?y, in=?z] -> NNP[rn=?x, jj=?y, in=?z]
NP2[rn=?x, jj=?y, in=?z] -> PRP[rn=?x, jj=?y, in=?z]
NP2[rn=?x, jj=?y, in=?z] -> UNN[rn=?x] NN[rn=?x, jj=?y, in=?z] 
NP1[rn=?x, jj=?y, in=?z] -> NN[rn=?x, jj=?y, in=?z]
NP1[rn=?x, jj=?y, in=?z] -> NNP[rn=?x, jj=?y, in=?z]
NP1[rn=?x, jj=?y, in=?z] -> PRP[rn=?x, jj=?y, in=?z]
NP1[rn=?x, jj=?y, in=?z] -> UNN[rn=?x] NN[rn=?x, jj=?y, in=?z] 


VP[rn=?x] -> VB[rn=?x]
VP[rn=?x] -> VB[rn=?x, rd=?y] NP[rn=?y]
VP[rn=?x] -> VP[rn=?x] PP[]

PP[] -> IN[in=?z] NP[in=?z]

PRP[rn=nguoi] -> "tôi"

NNP[rn=nguoi] -> "Nam"

UNN[rn=dong_vat] -> "con"
UNN[rn=dong_vat] -> "đàn"
UNN[rn=do_vat] -> "chiếc"
UNN[rn=thuc_vat] -> "bãi"
UNN[rn=do_vat] -> "căn"

NN[rn=dong_vat] -> "cá"
NN[rn=dong_vat] -> "chim"
NN[rn=vat_the] -> "mặt_trời"
NN[rn=dong_vat] -> "voi"
NN[rn=thuc_vat] -> "cỏ"
NN[rn=thuc_vat] -> "cây"
NN[rn=do_vat] -> "xe"
NN[rn=do_vat] -> "xương"
NN[rn=su_vat, in=ao] -> "ao"
NN[rn=su_vat, in=bo] -> "bờ"
NN[rn=do_vat] -> "nhà"
NN[rn=do_vat, jj=vang] -> "lá"
NN[rn=dong_vat, jj=den] -> "mèo"
NN[rn=dong_vat, jj=gay] -> "ngựa"
NN[rn=dong_vat, jj=nho] -> "kiến"
NN[rn=dong_vat, jj=nho] -> "chó"
NN[rn=dong_vat, jj=vang] -> "nai"

IN[] -> "của"
IN[] -> "trên"
IN[in=ao] -> "trong"
IN[in=bo] -> "lên"

JJ[jj=den] -> "đen"
JJ[jj=gay] -> "gầy"
JJ[jj=nho] -> "nhỏ"
JJ[jj=vang] -> "vàng"

VB[rn=nguoi] -> "ngủ"
VB[rn=dong_vat] -> "ngủ"
VB[rn=nguoi] -> "chơi"
VB[rn=dong_vat] -> "chơi"
VB[rn=dong_vat] -> "bơi"
VB[rn=dong_vat] -> "bay"
VB[rn=vat_the] -> "mọc"
VB[rn=dong_vat] -> "nhảy"
VB[rn=do_vat] -> "rụng"
VB[rn=do_vat] -> "cháy"
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

sentences_3 = ["con chó của tôi chơi trên bãi cỏ",
               "con cá trong ao nhảy lên bờ",
               "chiếc lá vàng trên cây rụng",
               "căn nhà của Nam cháy",
               "con mèo của tôi ngủ"]

tests = ["chiếc lá vàng trên cây rụng"]
tests2 = ["con cá trong ao nhảy lên bờ"]
for sent in sentences_3:
    print(sent)
    words = sent.split()
    for tree in parser.parse(words):
        tree.draw()
