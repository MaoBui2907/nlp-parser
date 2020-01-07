# coding=utf-8

import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""
S -> NP[rn=?x] VP[rn=?x]

NP[rn=?x, jj=?y, in=?z] -> NN[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> NNP[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> PRP[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> UNN[rn=?x] NN[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> DET[] NP[rn=?x, jj=?y, in=?z]
NP[rn=?x, jj=?y, in=?z] -> CD[] NP[rn=?x, jj=?y, in=?z]

NP[rn=?x, jj=?y, in=?z] -> NP2[] CC[] NP[]
NP[rn=?x, jj=?y, in=?z] -> NP2[rn=?x,in=?z] PP[in=?z]
NP[rn=?x, jj=?y, in=?z] -> NP2[rn=?x, jj=?y, in=?z] JJ[jj=?y]
NP2[rn=?x, jj=?y, in=?z] -> NP1[rn=?x, in=?z] PP[in=?z]
NP2[rn=?x, jj=?y, in=?z] -> NP1[rn=?x, jj=?y, in=?z] JJ[jj=?y]
NP2[rn=?x, jj=?y, in=?z] -> NN[rn=?x, jj=?y, in=?z]
NP2[rn=?x, jj=?y, in=?z] -> NNP[rn=?x, jj=?y, in=?z]
NP2[rn=?x, jj=?y, in=?z] -> PRP[rn=?x, jj=?y, in=?z]
NP2[rn=?x, jj=?y, in=?z] -> UNN[rn=?x] NN[rn=?x, jj=?y, in=?z] 
NP2[rn=?x, jj=?y, in=?z] -> DET[] NP[rn=?x, jj=?y, in=?z]
NP1[rn=?x, jj=?y, in=?z] -> NN[rn=?x, jj=?y, in=?z]
NP1[rn=?x, jj=?y, in=?z] -> NNP[rn=?x, jj=?y, in=?z]
NP1[rn=?x, jj=?y, in=?z] -> PRP[rn=?x, jj=?y, in=?z]
NP1[rn=?x, jj=?y, in=?z] -> UNN[rn=?x] NN[rn=?x, jj=?y, in=?z] 
NP1[rn=?x, jj=?y, in=?z] -> DET[] NP[rn=?x, jj=?y, in=?z]


VP[rn=?x] -> VB[rn=?x]
VP[rn=?x] -> VP[rn=?x] VP[rn=?x]
VP[rn=?x] -> VB[rn=?x, rd=?y] NP[rn=?y]
VP[rn=?x] -> VP[rn=?x] PP[ri=?x]

PP[in=?z] -> IN[] NP[in=?z]

DET[] -> "các"

CC[] -> "và"
CC[] -> "cùng"
CC[] -> "với"

CD[] -> "một"

PRP[rn=nguoi] -> "tôi"
PRP[rn=nguoi] -> "chúng_tôi"

NNP[rn=nguoi] -> "Nam"
NNP[rn=nguoi] -> "Hoa"

UNN[rn=dong_vat] -> "con"
UNN[rn=dong_vat] -> "đàn"
UNN[] -> "chiếc"
UNN[] -> "bãi"
UNN[rn=do_vat] -> "căn"
UNN[] -> "bọn"
UNN[rn=nguoi] -> "ông"
UNN[rn=nguoi] -> "đứa"

NN[] -> "con"
NN[rn=mon_hoc] -> "toán"
NN[rn=dong_vat, in=nuoc] -> "cá"
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
NN[rn=do_vat, in="san"] -> "bóng"
NN[rn=am_thanh, in=phat_nhac] -> "nhạc"
NN[rn=do_vat, in=thuyen] -> "thuyền"
NN[rn=do_vat, in=noi] -> "nôi"
NN[rn=su_vat, in=nuoc] -> "ao"
NN[rn=su_vat, in=bo] -> "bờ"
NN[rn=su_vat] -> "nắng"
NN[rn=su_vat] -> "sân"
NN[rn=do_vat, in=nha] -> "nhà"
NN[rn=do_vat] -> "lá"
NN[rn=do_vat] -> "sản_phẩm"
NN[rn=do_vat] -> "ô_tô"
NN[rn=do_vat] -> "cửa_hàng"
NN[rn=dong_vat] -> "mèo"
NN[rn=dong_vat] -> "chuột"
NN[rn=dong_vat] -> "ngựa"
NN[rn=dong_vat, jj=nho] -> "kiến"
NN[rn=dong_vat] -> "chó"
NN[rn=dong_vat] -> "nai"
NN[rn=nguoi] -> "quân_đội"
NN[rn=su_vat] -> "kẻ_thù"

IN[] -> "của"
IN[] -> "trên"
IN[] -> "trong"
IN[] -> "ở"
IN[] -> "lên"

JJ[jj=mai] -> "mái"
JJ[jj=den] -> "đen"
JJ[jj=gay] -> "gầy"
JJ[jj=nho] -> "nhỏ"
JJ[jj=vang] -> "vàng"
JJ[jj=moi] -> "mới"

VB[] -> "học"
VB[] -> "ngủ"
VB[] -> "chơi"
VB[] -> "đi"
VB[rn=nguoi] -> "luyện_tập"
VB[] -> "bơi"
VB[rn=dong_vat] -> "bay"
VB[rn=vat_the] -> "mọc"
VB[] -> "nhảy"
VB[] -> "chạy"
VB[] -> "tắm"
VB[] -> "đuổi"
VB[] -> "bắt"
VB[] -> "đâm"
VB[] -> "vào"
VB[rn=do_vat] -> "rụng"
VB[rn=do_vat] -> "cháy"
VB[] -> "tấn_công"
VB[] -> "tiến_công"
VB[] -> "tiêu_diệt"
VB[rn=nguoi] -> "nghiên_cứu"
VB[rn=nguoi] -> "phát_triển"
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

sentences_6 = ["Nam đi học toán",
               "quân_đội tiến_công tiêu_diệt kẻ_thù",
               "chúng_tôi nghiên_cứu phát_triển một sản_phẩm mới",
               "mèo đuổi bắt chuột",
               "chiếc ô_tô đâm vào cửa_hàng"]

sentences = sentences_1 + sentences_2 + sentences_3 + \
    sentences_4 + sentences_5 + sentences_6

validates = ["tôi và Nam chơi bóng ở nhà",
             "con chó nhỏ nhảy lên thuyền",
             "ông lão chạy trên sân",
             "con mèo gầy chơi trên bãi cỏ",
             "Nam ngủ trong cửa_hàng",
             "chiếc ô_tô đen chạy trên sân",
             "tôi nghiên_cứu ở nhà",
             "cá vàng bơi trong ao",
             "Hoa câu cá",
             "chiếc lá vàng cháy trên cây",
             "mặt_trời bắt chuột",
             "gà mái bay",
             "mèo gầy tấn_công chuột",
             "con ngựa đen tắm nắng",
             "Nam nghe nhạc ở nhà",
             "vận_động_viên đuổi chuột trên sân",
             "tôi ngủ trên thuyền",
             "mèo vào cửa_hàng",
             "mèo đen tiêu_diệt chó nhỏ",
             "ngựa vàng kéo mặt_trời"]

for sent in validates:
    print(sent)
    words = sent.split()
    for tree in parser.parse(words):
        tree.draw()
