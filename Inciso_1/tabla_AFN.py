# Ejercicio 1 — Construcción AFN y otras expresiones

from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

# -------------------------
# Estructuras y funciones base
# -------------------------
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

def epsilon_frag():
    s = new_state()
    a = new_state()
    add_transition(s, 'ε', a)
    return (s, [a])

def optional(f):
    ns = new_state(); na = new_state()
    add_transition(ns, 'ε', f[0]); add_transition(ns, 'ε', na)
    for ac in f[1]:
        add_transition(ac, 'ε', na)
    return (ns, [na])

# -------------------------
# Inciso 1 — letter = A|B|a|b
# -------------------------
letters = [symbol(x) for x in ['A','B','a','b']]
letter_frag = union(letters)

print("letter start:", letter_frag[0], "accepts:", letter_frag[1])
print("Transiciones:")
pprint(transitions)

# Graficar AFN de letter
start = letter_frag[0]
accepts = set(letter_frag[1])

G = nx.DiGraph()
for s, mapping in transitions.items():
    for sym, dests in mapping.items():
        for d in dests:
            G.add_edge(s, d, label=sym)

pos = nx.spring_layout(G)  
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))

nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='green', node_size=700)
nx.draw_networkx_nodes(G, pos, nodelist=list(accepts), node_color='orange', node_size=700)

plt.title("AFN de 'letter'")
plt.axis('off')
plt.show()

# -------------------------
# Inciso 2 — digit y digits
# -------------------------
digits_syms = [symbol(str(i)) for i in range(10)]
digit_frag = union(digits_syms)
digits_frag = plus(digit_frag)  # digit+

print("digit start:", digit_frag[0], "accepts:", digit_frag[1])
print("digits (digit+) start:", digits_frag[0], "accepts:", digits_frag[1])

# -------------------------
# Inciso 3 — id = letter (letter|digit)*
# -------------------------
letter_or_digit = union([letter_frag, digit_frag])
letter_or_digit_star = star(letter_or_digit)
id_frag = concat(letter_frag, letter_or_digit_star)
print("id start:", id_frag[0], "accepts:", id_frag[1])

# -------------------------
# Inciso 4 — number
# -------------------------
dot = symbol('.')
plus_s = symbol('+')
minus_s = symbol('-')
sign_union = union([plus_s, minus_s])
sign_opt = optional(sign_union)

fractional_opt = optional(concat(dot, digits_frag))
E_sym = symbol('E')
exponent_core = concat(E_sym, concat(sign_opt, digits_frag))
exponent_opt = optional(exponent_core)

number_frag = concat(digits_frag, concat(fractional_opt, exponent_opt))
print("number start:", number_frag[0], "accepts:", number_frag[1])

# -------------------------
# Tabla AFN (ε-closure y δ)
# -------------------------
def epsilon_closure(states, transitions):
    stack = list(states)
    closure = set(states)
    while stack:
        s = stack.pop()
        for t in transitions.get(s, {}).get('ε', []):
            if t not in closure:
                closure.add(t)
                stack.append(t)
    return closure

def move(states, symbol, transitions):
    res = set()
    for s in states:
        for dest in transitions.get(s, {}).get(symbol, []):
            res.add(dest)
    return res

all_states = list(transitions.keys())
alphabet = [str(i) for i in range(10)] + ['A','B','a','b','.', 'E', '+', '-']

for s in all_states:
    ecl = epsilon_closure({s}, transitions)
    print("Estado", s, "ε-closure:", ecl)
    for a in alphabet:
        m = move({s}, a, transitions)
        m_cl = epsilon_closure(m, transitions)
        if m_cl:
            print(f"  δ({s}, {a}) -> {m_cl}")
