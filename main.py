# coding=utf-8

import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""
S -> NP[rn=?x] VP[rn=?x]

NP[rn=?x, jj=?y, in=?z] -> NN[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> NNP[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> PRP[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> UNN[rn=?x] NN[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> DET[] NP[rn=?x, jj=?y, in=?z]

NP[rn=?x, jj=?y, in=?z] -> NP2[] CC[] NP[]
NP[rn=?x, jj=?y, in=?z] -> NP2[rn=?x] PP[rn=?x]
NP[rn=?x, jj=?y, in=?z] -> NP2[rn=?x, jj=?y, in=?z] JJ[jj=?y]
NP2[rn=?x, jj=?y, in=?z] -> NP1[rn=?x] PP[rn=?x]
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
VP[rn=?x, rd=?y] -> VP[rn=?x, rd=?y] PP[rn=?x]

PP[rn=?x] -> IN[ri=?x, in=?z] NP[in=?z]

DET[] -> "các"

CC[] -> "và"
CC[] -> "cùng"
CC[] -> "với"

PRP[rn=nguoi] -> "tôi"

NNP[rn=nguoi] -> "Nam"
NNP[rn=nguoi] -> "Hoa"

UNN[rn=dong_vat] -> "con"
UNN[rn=dong_vat] -> "đàn"
UNN[rn=do_vat] -> "chiếc"
UNN[] -> "bãi"
UNN[rn=do_vat] -> "căn"
UNN[] -> "bọn"
UNN[rn=nguoi] -> "ông"
UNN[rn=nguoi] -> "đứa"

NN[] -> "con"
NN[rn=mon_hoc] -> "toán"
NN[rn=dong_vat] -> "cá"
NN[rn=nguoi] -> "trẻ"
NN[rn=nguoi] -> "bé"
NN[rn=nguoi] -> "lão"
NN[rn=nguoi] -> "mẹ"
NN[rn=nguoi] -> "vận_động_viên"
NN[rn=dong_vat] -> "chim"
NN[rn=dong_vat] -> "voi"
NN[rn=dong_vat] -> "gà"
NN[rn=vat_the] -> "mặt_trời"
NN[rn=thuc_vat] -> "cỏ"
NN[rn=thuc_vat, in=cay] -> "cây"
NN[rn=do_vat] -> "xe"
NN[rn=do_vat] -> "xương"
NN[rn=do_vat] -> "bóng"
NN[rn=am_thanh] -> "nhạc"
NN[rn=do_vat, in=thuyen] -> "thuyền"
NN[rn=do_vat, in=noi] -> "nôi"
NN[rn=su_vat, in=ao] -> "ao"
NN[rn=su_vat, in=bo] -> "bờ"
NN[rn=su_vat] -> "nắng"
NN[rn=su_vat] -> "sân"
NN[rn=do_vat] -> "nhà"
NN[rn=do_vat] -> "lá"
NN[rn=dong_vat] -> "mèo"
NN[rn=dong_vat] -> "ngựa"
NN[rn=dong_vat, jj=nho] -> "kiến"
NN[rn=dong_vat] -> "chó"
NN[rn=dong_vat] -> "nai"

IN[] -> "của"
IN[ri=nguoi] -> "trên"
IN[] -> "trong"
IN[] -> "ở"
IN[in=bo] -> "lên"

JJ[jj=mai] -> "mái"
JJ[jj=den] -> "đen"
JJ[jj=gay] -> "gầy"
JJ[jj=nho] -> "nhỏ"
JJ[jj=vang] -> "vàng"

VB[] -> "học"
VB[] -> "ngủ"
VB[] -> "chơi"
VB[rn=nguoi] -> "luyện_tập"
VB[] -> "bơi"
VB[rn=dong_vat] -> "bay"
VB[rn=vat_the] -> "mọc"
VB[] -> "nhảy"
VB[] -> "chạy"
VB[] -> "tắm"
VB[rn=do_vat] -> "rụng"
VB[rn=do_vat] -> "cháy"
VB[] -> "tấn_công"
VB[rn=dong_vat, rd=do_vat] -> "kéo"
VB[rn=dong_vat, rd=do_vat] -> "gặm"
VB[] -> "ăn"
VB[rn=nguoi, rd=dong_vat] -> "câu"
VB[rd=am_thanh] -> "nghe"
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

sentences_4 = ["bọn trẻ chơi ở nhà",
               "đứa bé ngủ trong nôi",
               "các vận_động_viên luyện_tập trên sân",
               "con chó chạy trên bãi cỏ",
               "ông lão câu cá trên thuyền"]

sentences_5 = ["tôi và Nam nghe nhạc",
               "đứa bé cùng mẹ chơi bóng",
               "chó với mèo chạy trên sân",
               "gà mái cùng đàn con tắm nắng",
               "tôi và Hoa học toán"]

tests = ["ông lão câu cá trên thuyền"]
tests2 = ["con cá trong ao nhảy lên bờ"]
for sent in sentences_5:
    print(sent)
    words = sent.split()
    for tree in parser.parse(words):
        tree.draw()
