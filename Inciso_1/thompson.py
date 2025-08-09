# Inicso 1 AFN para letter - 0.5 pts
## Utilice el algoritmo de Thompson y muestre todo su procedimiento

from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

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

letters = [symbol(x) for x in ['A','B','a','b']]
letter_frag = union(letters)

print("letter start:", letter_frag[0], "accepts:", letter_frag[1])
print("Transiciones:")
pprint(transitions)

start = letter_frag[0]
accepts = set(letter_frag[1])

# Crear grafo dirigido
G = nx.DiGraph()
for s, mapping in transitions.items():
    for sym, dests in mapping.items():
        for d in dests:
            G.add_edge(s, d, label=sym)

# Dibujar grafo
pos = nx.spring_layout(G)  # Layout automático
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'))

nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='green', node_size=700)
nx.draw_networkx_nodes(G, pos, nodelist=list(accepts), node_color='orange', node_size=700)

plt.title("AFN de 'letter'")
plt.axis('off')
plt.show()