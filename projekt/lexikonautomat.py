from collections import OrderedDict, defaultdict
from state import State
import graphviz, pickle

class LexiconAutomaton():

    def __init__(self, lexicon):
        self.lexicon = lexicon
        self.register = []
        self.final_states = []
        self.all_states = []
        self.language = []
        self.start_state = State(False, False, OrderedDict())
        self.all_states.append(self.start_state)
        self.alphabet = sorted({char for word in self.lexicon for char in word})
        
        for word in self.lexicon:
    
            commonPre, lastState = self.common_prefix(word)
            longestCommonPre = word[:commonPre]
            currentSuff = word[len(longestCommonPre):]
            if lastState.has_children():
                self.replace_or_register(lastState)
            self.add_suffix(lastState, currentSuff)

        self.replace_or_register(self.start_state)

    def add_suffix(self, state, suffix):
        for char in suffix:
            target = State(False, False, OrderedDict())
            state.add_transition(char, target)
            self.all_states.append(target)
            state = target
            if char == suffix[-1]:
                state.make_final()
                self.final_states.append(state)

                
    def common_prefix(self, word):
        i = 0
        current_state = self.start_state
        for char in word:
            if current_state.transition(char):
                current_state = current_state.transition(char)
                i += 1
            else:
                return i, current_state

    def replace_or_register(self, state):
        child = state.get_last_child()
        equiv_list = []
        if child.has_children():
            self.replace_or_register(child)
        equiv_state = None
        for q in self.register:
            if q.unique_repr() == child.unique_repr():
                equiv_list.append(child)
                equiv_state = q
        if equiv_state != None:
            self.all_states = [state for state in self.all_states if state not in equiv_list]
            label = state.get_last_label()
            state.add_transition(label, equiv_state)
        else:
            self.move_to_register(child)

    def move_to_register(self, state):
        state.is_in_register = True
        self.register.append(state)

    def delta_dict(self):
        delta = dict()
        for state in self.all_states:
            for char in self.alphabet:
                if state.transition(char):
                    target = state.transition(char)
                    delta.update({(state, char): target})
        return delta

    def recursive_search(self, state, memory=[]):
        if state.is_final:
            self.language.append("".join(memory))
    
        for label, next_state in state.transitions.items():
            memory.append(label)
            self.recursive_search(next_state)
            memory.pop()
        
        return self.language
    
    def get_language(self):
        return self.recursive_search(self.start_state)

    def get_register(self): 
        return sorted([state.ID for state in self.register])

    def get_final_states(self):
        return sorted([state.ID for state in self.final_states])
    
    def get_all_states(self):
       return sorted([state.ID for state in self.all_states])

    def get_delta(self):
        return {(start.ID, label, target.ID) for (start, label), target in self.delta_dict().items()}

    def draw_automaton(self):
        draw = graphviz.Digraph('Lexicon Automaton')
        draw.graph_attr['rankdir'] = 'LR'
        all_states = self.get_all_states()
        start_state = all_states[0]
        for state in all_states:
            if state in self.get_final_states():
                draw.attr('node',style='bold')
            if state == start_state:
                draw.node(str(state), label="-> " + str(state))
            else:
                draw.node(str(state))
            draw.attr('node',style='solid')
    
        for start, label, target in self.get_delta():
            draw.edge(str(start), str(target), label=" " + label+ " ")
    
        return draw.render('Lex_Automat.gv', view=True)