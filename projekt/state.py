class State():
    
    next_ID = 0
    
    def __init__(self,is_final,is_in_register,transitions):
        self.is_final = is_final
        self.ID = State.next_ID
        State.next_ID += 1
        self.is_in_register = False
        self.transitions = transitions
        
    def unique_repr(self):
        return ("F" if self.is_final else "N") \
        + "".join([str(label) + str(target.ID) for label,target in self.transitions.items()])
    
    def add_transition(self,label,target_state):
        self.transitions[label] = target_state
        
    def transition(self,label):
        if label in self.transitions.keys():
            return self.transitions[label]
        
    def remove_transition(self,label):
        del self.transitions[label]
        
    def get_last_child(self):
        for state in reversed(self.transitions.values()):
            return state
    
    def get_last_label(self):
        for label in reversed(self.transitions.keys()):
            return label

    def has_children(self):
        if len(self.transitions) == 0:
            return False
        else:
            return True
    
    def make_final(self):
        self.is_final = True