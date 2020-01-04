# coding=utf-8
import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""
S -> NP[sub=?x] VP[sub=?x]
S -> NP[jj=?x] ADJP[jj=?x]

NP[sub=?x, jj=?y, in=?z] -> NN[sub=?x, jj=?y, in=?z]
NP[sub=?x, jj=?y, in=?z] -> NNP[sub=?x, jj=?y, in=?z]
NP[sub=?x, jj=?y, in=?z] -> UNN[sub=?x, jj=?y] NN[sub=?x, jj=?y, in=?z]
NP[sub=?x, jj=?y] -> NP1[sub=?x, jj=?y] PP[]
NP[sub=?x, jj=?y] -> NP1[sub=?x, jj=?y] ADJP[jj=?y]

NP1[sub=?x, jj=?y, in=?z] -> NN[sub=?x, jj=?y, in=?z]
NP1[sub=?x, jj=?y, in=?z] -> NNP[sub=?x, jj=?y, in=?z]
NP1[sub=?x, jj=?y, in=?z] -> UNN[sub=?x, jj=?y] NN[sub=?x, jj=?y, in=?z]

VP[sub=?x] -> VB[sub=?x] VB[sub=?x]
VP[sub=?x] -> VB[sub=?x] PP[]

ADJP[jj=?x] -> JJ[jj=?x]
ADJP[jj=?x] -> RB[] JJ[jj=?x]

PP[] -> IN[in=?x] NP[in=?x]

NN[jj=kho, sub=nguoi] -> 'anh'
NN[jj=kho, sub=bai] -> 'toán'
NN[jj=moi, sub=bai] -> 'toán'
NN[jj=sang, sub=sang, in=sang] -> 'sáng'
NNP[jj=kho, sub=nguoi] -> 'Hoa'
VB[sub=nguoi] -> 'đi'|'học'
JJ[jj=kho] ->'khó'
JJ[jj=moi] ->'khó'
JJ[jj=moi] -> 'mới'
IN[in=sang] -> 'từ'
IN[] -> 'của'
UNN[jj=kho, sub=bai] -> 'bài'
UNN[jj=moi, sub=bai] -> 'bài'
RB[]->'rất'
""")

parser = nltk.parse.FeatureChartParser(grammar)

sentences=["anh của Hoa đi học", "anh đi từ sáng", "bài toán mới rất khó", "anh của Hoa khó rất khó", "bài toán của anh của Hoa rất mới", "anh của bài toán rất mới"]

for sent in sentences:
	print(sent)
	words = sent.split()
	for tree in parser.parse(words):
		tree.draw()
		
