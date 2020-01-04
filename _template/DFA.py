import copy

class DFA:

	def __init__(self, states=[], input_symbols=[], transitions={}, initial_state=0, final_states=[]):
	
		self.states = states.copy()
		self.input_symbols = input_symbols.copy()
		self.transitions = copy.deepcopy(transitions)
		self.initial_state = initial_state
		self.final_states = final_states.copy()
	
	def	accept(self, inputs):
		curState = self.initial_state
		
		for input in inputs:
			try:
				curState = self.transitions[curState][input]
			except:
				return False
		return curState in self.final_states

	def create(self, s):
		i = 0
		letters = list(s)
		self.transitions = {}
		self.states = []
		self.states.append(i)
		self.input_symbols = []
		self.input_symbols.append(letters[i])
		
		j = len(letters)
		for l in letters:
			k = i+1			
			if j >= k:
				self.transitions.update({str(i):{l:str(k)}})
				self.states.append(str(k))
				if not (l in self.input_symbols):
					self.input_symbols.append(l)
			i=i+1
		self.initial_state = 0
		self.final_states = [j]
		
	def _multiply(self, M):
		self.input_symbols = list(set().union(self.input_symbols, M.input_symbols))
		self.initial_state = str(self.initial_state) + " " + str(M.initial_state)
		states = [self.initial_state]
		i = 0
		transitions = {}
		while i < len(states):
			for input in self.input_symbols:
				pos = states[i].split()
				s1 = pos[0]
				s2 = pos[1]
				e1 = "-1"
				e2 = "-1"
				
				if s1 != "-1":
					try:
						e1 = self.transitions[s1][input]
					except:
						e1 = "-1"

				if s2 != "-1":
					try:
						e2 = M.transitions[s2][input]
					except:
						e2 = "-1"
				
				if e1 != "-1" or e2 != "-1":
					key = s1 + " " + s2
					state = e1 + " " + e2
					try:
						trans = transitions[key]
					except:
						trans = {}
					trans.update({input:state})
					transitions.update({key:trans})
					states.append(state)
				
			i += 1
		self.states = states
		self.transitions = transitions

	def union(self, M):
		self._multiply(M)
		finals = []
		for s1 in self.final_states:
			for s2 in M.final_states:
				final = str(s1) + " " + str(s2)
				if final in self.states:
					finals.append(final)
		for s1 in self.final_states:
			final = str(s1) + " -1"
			if final in self.states:
				finals.append(final)
			
		for s2 in M.final_states:
			final = "-1 " + str(s2)
			if final in self.states:
				finals.append(final)
			
		self.final_states = finals

M1 = DFA (
	[0,1,2],
	['0','1'],
	{
		0:{'0':0,'1':1},
		1:{'0':1,'1':2},
		2:{'0':2,'1':0}
		},
	0,
	[1]
	)

print(M1.accept(list("01010100")))
print(M1.accept(list("010010011")))
	
M = DFA()
M.create(list("cats"))
MM = DFA()
MM.create(list("captains"))

M.union(MM)
print(M.accept(list("cat")))
print(M.accept(list("cats")))
print(M.accept(list("captains")))
print(M.accept(list("captain")))
