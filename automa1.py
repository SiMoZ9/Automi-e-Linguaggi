class DFA:
	def __init__(self):
		#states: q0, q1, q2
		#DFA M = (states, alfa, transition, initial state, accepter state)
		self.states = ('q0', 'q1', 'q2')
		self.alfa = ('0', '1')
		self.init_state = self.states[0]
		self.current_state = self.init_state
		self.accepter = self.init_state
	
	def transition(self, character):
		#@param character: character to transition
		#@return char

		######################## q0 ########################
		if character == self.alfa[0] and self.current_state == 'q0':
			self.current_state = 'q0'

		elif character == self.alfa[1] and self.current_state == 'q0':
			self.current_state = 'q1'
		
		######################## q1 ########################
		elif character == self.alfa[0] and self.current_state == 'q1':
			self.current_state = 'q2'

		elif character == self.alfa[1] and self.current_state == 'q1':
			self.current_state = 'q0'
		
		######################## q2 ########################
		elif character == self.alfa[0] and self.current_state == 'q2':
			self.current_state = 'q1'

		elif character == self.alfa[1] and self.current_state == 'q2':
			self.current_state = 'q2'
	
	def is_accepting(self):
		return self.current_state == self.accepter

def main():
	d = DFA()
	string = bin(int(input("Enter a number: ")))
	string = str(string)

	for i in string:
		d.transition(i)
	
	if d.is_accepting() == True:
		return True
	
	else:
		return False
	
if __name__ == '__main__':
	print(main())