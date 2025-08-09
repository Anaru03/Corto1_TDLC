from pprint import pprint

transitions = {} 
state_counter = 0

def new_state():
    global state_counter, transitions
    s = state_counter
    state_counter += 1
    transitions[s] = {}
    return s

def add_transition(s, sym, t):
    transitions.setdefault(s, {})
    transitions[s].setdefault(sym, [])
    if t not in transitions[s][sym]:
        transitions[s][sym].append(t)
