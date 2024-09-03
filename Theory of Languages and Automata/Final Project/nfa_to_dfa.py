def make_final_state(final, dfa_dict):
    
    new_finales = []

    for init_final_state in final:                  #init_final_state   in['A']
        for state in dfa_dict.keys():
            if init_final_state in state:
                new_finales.append(state)
    return new_finales


def accesible_states(dfa_dict):    

    temp = []
    for state in dfa_dict:
        for x in dfa_dict[state]:
            if (x not in dfa_dict.keys()) and x:
                temp.append(x)
    return temp
    



def inAll():
    dfa_result_dict = {}
    states_to_examine = []
    alphabet = []
    rules = []

    nfa_input = [['5'],
                 ['ab'],
                 ['0'],
                 ['4'],
                 ['0b2'],['01'],['1a0'],['1a4'],['13'],['12'],['01'],['2b4'],['3a4'],['43']]

    count = 0
    states_num = 0
    initial_state = ''
    final_states = ''

    for row in nfa_input:                  # line
        if count == 0:
            states_num = int(row[0])       
        elif count == 1:
            alphabet = list(row[0])        
        elif count == 2:
            initial_state = str(row[0])    
        elif count == 3:
            final_states = (str(row[0]))   
        else:
            rules.append(row[0])           # rules
        count += 1


    final_states = list(final_states)

    states_to_examine.append(initial_state)         #A

    while True:
        for state in states_to_examine:              # all state in dfa
            
                                                    # states result for every input
        
            result = []
            i = 0
            for letter in alphabet:
                res = ''
                for a in state:
                    for idx in rules:
                        if idx[0] == str(a) and idx[1] == letter:
                            if idx[2] not in res:
                                res += idx[2]
                result.append(''.join(sorted(res)))
                i += 1
            dfa_result_dict[state] = result
        
            
            
            states_to_examine = accesible_states(dfa_result_dict).copy()
            
        if not states_to_examine:
            break

    final_states = (make_final_state(final_states, dfa_result_dict)).copy()


    print(f"Number of states is {len(dfa_result_dict)}")
    
    list_alphabet = ''
    for symbol in alphabet:
        list_alphabet+=symbol
        
    lentgh_alphabet = len(alphabet)
    print('{0}:is symbols-->{1} symbols in the alphabet\n'.format(list_alphabet,lentgh_alphabet))
    
    print('start state is : {0}'.format(initial_state))
    
    list_final = ''
    for symbols_state in final_states:
        list_final+=symbols_state+' '
    print('Final state is :{0}'.format(list_final))

    for state in dfa_result_dict:
        counter = 0
        for result in dfa_result_dict[state]:
            if state == '':
                state = '_'
            if result == '':
                result = '_'
            print("{0} {1} {2}".format(state,alphabet[counter],result))
            print(f"From  {state} state with {alphabet[counter]} to ===>  {result} state \n")
            counter += 1

    print(f"\n{dfa_result_dict}")


inAll()
