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

def symbol(sym):
    s = new_state()
    a = new_state()
    add_transition(s, sym, a)
    return (s, [a])

def union(frags):
    ns = new_state()
    na = new_state()
    for f in frags:
        add_transition(ns, 'ε', f[0])
        for ac in f[1]:
            add_transition(ac, 'ε', na)
    return (ns, [na])

def concat(f1, f2):
    for ac in f1[1]:
        add_transition(ac, 'ε', f2[0])
    return (f1[0], f2[1])

def star(f):
    ns = new_state(); na = new_state()
    add_transition(ns, 'ε', f[0]); add_transition(ns, 'ε', na)
    for ac in f[1]:
        add_transition(ac, 'ε', f[0]); add_transition(ac, 'ε', na)
    return (ns, [na])

def plus(f):
    return concat(f, star(f))
