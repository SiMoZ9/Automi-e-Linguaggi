class NFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3'}
        self.alfa = {'0', '1'}
        self.initial_state = self.states[0]
        self.current_state = self.initial_state
    
    def transition(self, chr):
        if chr == '0' and self.current_state == 'q0':
            self.current_state = 'q0'
        
        if chr == '1' and self.current_state == 'q0':
            self.current_state