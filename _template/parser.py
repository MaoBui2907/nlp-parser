import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> CD NP
NP -> UNN NN
NP -> NN JJ
NP -> NP PP
NP -> NN
PP -> IN NP
PP -> IN PP
VP -> VB PP
NP -> PRP
VP -> VP PP
VP -> VB NP
NP -> ADJP NP

CD -> 'một'
UNN -> 'con'
NN -> 'mèo' | 'nhựa' | 'bàn' | 'thẻ' | 'nhà'
IN -> 'bằng' | 'ở' | 'trên' | 'của'
JJ -> 'đỏ' | 'nhiều'
RB -> 'rất'
VB -> 'nằm' | 'mua' | 'là' | 'ở' | 'có'
PRP -> 'họ'

""")
parser = nltk.ChartParser(grammar)
sentences = ["một con mèo bằng nhựa đỏ nằm ở trên bàn",
"họ mua con mèo bằng thẻ",
"họ có rất nhiều thẻ ở nhà",
"thẻ của họ là thẻ bằng nhựa",
"họ ở nhà"]
for sentence in sentences:
	words = [w for w in sentence.split()]
	print("Kết quả phân tích ")
	print(words)
	for tree in parser.parse(words):
		print(tree)
		tree.draw()
	