from automathon import NFA

#Declaracao do automato

## Epsilon Transition is denoted by '' -> Empty string
q = {'q0', '0A', '1A', '2A', '3A', '4A', '0B', '1B', '2B', '3B', '4B'}
sigma = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'}
delta = {
    'q0' : {
            '' : {'0A', '0B'}
            },
    '0A' : {
            'A' : {'0A'},
            'B' : {'1A'},
            'C' : {'2A'},
            'D' : {'3A'},
            'E' : {'4A'},
            'F' : {'0B'},
            },
    '1A' : {
            '' : {'0A'},
            'A' : {'0A'}, 
            'B' : {'1A'},
            'C' : {'2A'},
            'D' : {'3A'},
            'E' : {'4A'}
            },
    '2A' : {
            '' : {'0A'},   
            'A' : {'0A'}, 
            'B' : {'1A'},
            'C' : {'2A'},
            'D' : {'3A'},
            'E' : {'4A'}
            },
    '3A' : {
            '' : {'0A'},
            'A' : {'0A'}, 
            'B' : {'1A'},
            'C' : {'2A'},
            'D' : {'3A'},
            'E' : {'4A'}
            },
    '4A' : {
            '' : {'0A'},
            'A' : {'0A'}, 
            'B' : {'1A'},
            'C' : {'2A'},
            'D' : {'3A'},
            'E' : {'4A'},
            'J' : {'4B'},
            },
    '0B' : {
            'F' : {'0B'},
            'G' : {'1B'},
            'H' : {'2B'},
            'I' : {'3B'},
            'J' : {'4B'},
            'A' : {'0A'},
            },
    '1B' : {
            '' : {'0B'},
            'F' : {'0B'},
            'G' : {'1B'},
            'H' : {'2B'},
            'I' : {'3B'},
            'J' : {'4B'}
            },
    '2B' : {
            '' : {'0B'},
            'F' : {'0B'},
            'G' : {'1B'},
            'H' : {'2B'},
            'I' : {'3B'},
            'J' : {'4B'}
            },
    '3B' : {
            '' : {'0B'},
            'F' : {'0B'},
            'G' : {'1B'},
            'H' : {'2B'},
            'I' : {'3B'},
            'J' : {'4B'}
            },
    '4B' : {
            '' : {'0B'},
            'F' : {'0B'},
            'G' : {'1B'},
            'H' : {'2B'},
            'I' : {'3B'},
            'J' : {'4B'},
            'E' : {'4A'},
            }
}
initial_state = 'q0'
f = {'0A', '0B'}

automata = NFA(q, sigma, delta, initial_state, f)

#Testes

# 0A  | A
print("Teste: A")
print(automata.accept("A"))


# 0A 0B 2B 1B 4B 4A 3A 0A | AFHGJEDA
print("Teste: AFHGJEDA")
print(automata.accept("AFHGJEDA"))


# 0A 2b | AH
print("Teste: AH")
print(automata.accept("AH"))


# 0B | B
print("Teste: B")
print(automata.accept("B"))


# 0B 1B 2B 0A| FGHA
print("Teste: FGHA")
print(automata.accept("FGHA"))


# 0B 1A 1A 0A 2B| FBBAH
print("Teste: FBBAH")
print(automata.accept("FBBAH"))


# 0B 1B 3B 4B 0B| FGIJF
print("Teste: FGIJF")
print(automata.accept("FGIJF"))


# 0A 3A 0B 2A 1A 0A 3A| ADFCBAD
print("Teste: ADFCBAD")
print(automata.accept("ADFCBAD"))

#Imagens do automato

# Automato Nao Deterministico com Movimento Vazio
automata.view(
        file_name="AFN-ε",
        node_attr={'fontsize': '20'},
        edge_attr={'fontsize': '20pt'}
        )

# Automato Nao Deterministico
automata_1 = automata.remove_epsilon_transitions()
automata_1.renumber()
automata_1.view(
        file_name="AFN",
        node_attr={'fontsize': '20'},
        edge_attr={'fontsize': '20pt'}
        )

# Automato Nao Deterministico para Automato Deterministico
automata_3 = automata.get_dfa()
automata_3.renumber()
automata_3.view(
        file_name="AFN_AFD",
        node_attr={'fontsize': '20'},
        edge_attr={'fontsize': '20pt'}
        )

# Automato Finito minimizado
automata_2 = automata.minimize()
automata_2.view(
        file_name="AF_minimizado",
        node_attr={'fontsize': '20'},
        edge_attr={'fontsize': '20pt'}
        )
