import nltk
grammar = nltk.grammar.FeatureGrammar.fromstring("""
S -> NP[rn=?x] VP[rn=?x]
S -> NP
NP[rn=?x] -> NN[rn=?x]
NP[rn=?x] -> NNP[rn=?x]
NP[rn=?x] -> DET NP[rn=?x]
NP[rn=?x] -> NP[rn=?x] JJ[rn=?x]

VP[rn=?x] -> VB[rn=?x, rd=?y] NP[rn=?y]


NN[rn=ynghi] -> 'ý_nghĩ'
NN[rn=bonghoa] -> 'bông_hoa'
NNP[rn=nguoi] -> 'Nam'

JJ[rn=nguoi] -> 'thơm'
JJ[rn=bonghoa] -> 'thơm'

JJ[rn=nguoi] -> 'khôn'
JJ[rn=ynghi] -> 'khôn'

VB[rn=nguoi, rd=bonghoa]-> 'có'
VB[rn=nguoi, rd=ynghi]-> 'có'
DET -> 'một'
""")

parser = nltk.parse.FeatureChartParser(grammar)

sentences=["Nam có một ý_nghĩ khôn", "Nam có một bông_hoa thơm", "Nam có một bông_hoa khôn", "bông_hoa thơm có Nam", "Nam có bông_hoa", "Nam", "bông_hoa"]

for sent in sentences:
	print(sent)
	words = sent.split()
	for tree in parser.parse(words):
		tree.draw()
		
