
class Afd:
    def __init__(self, 
                number_of_states,
                inicial_state, 
                number_of_final_states,
                final_states, number_of_symbols, symbols, number_of_transitions, transitions):
        self.number_of_states = number_of_states
        self.inicial_state = inicial_state
        self.number_of_final_states = number_of_final_states
        self.final_states = final_states.strip().split()
        self.number_of_symbols = number_of_symbols
        self.symbols = symbols
        self.number_of_transitions = number_of_transitions
        self.transitions = self.__mount_transitions__(transitions)

    def check_input(self, input):
        current_state = self.inicial_state
        try:
            for char in input:
                current_state = self.transitions[current_state][char]
            if (current_state in self.final_states):
                return True
            # se chegou aqui é porque terminou a entrada e não encontrou um estado final.
            return False
        except:
            # se entrar aqui é porque tentou acessar uma entrada que não existe.
            return False        



    def __mount_transitions__(self, transitions):
        """
        receive transitions in string format and return dictionary.

        Args:
            transitions (str): a string containing all the transitions like '(q0 1 q1) (q1 1 q0) (q0 0 q2)'.

        Returns:
            dict: like \n
        { 
          q0: {
            1: q1,
            0: q2
          },
          q1: {
            1: q0
          }
        }
        """
        dicionario = {}
        pares = transitions.split(") (")        
        
        for par in pares:
            estado_origem, entrada, estado_destino = par.strip().strip("()").split()            
            if estado_origem not in dicionario:
                dicionario[estado_origem] = {}            
            dicionario[estado_origem][entrada] = estado_destino        
        return dicionario


if __name__ == '__main__':
    
    with open('./afd.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

        # Atribuindo cada linha a uma variável
        number_of_states = linhas[0].strip()            # 4
        inicial_state = linhas[1].strip()               # q0
        number_of_final_states = linhas[2].strip()      # 1
        final_states = linhas[3].strip()                # q0
        number_of_symbols = linhas[4].strip()
        symbols = linhas[5].strip()
        number_of_transitions = linhas[6].strip()

        transitions_str = ''
        for linha in linhas[7:-1]:
            transitions_str = f'{transitions_str} ({linha.strip()})'
        input = linhas[-1].strip()

        afd = Afd(number_of_states, inicial_state, number_of_final_states, final_states, number_of_symbols, symbols, number_of_transitions, transitions_str)
        print("######################################################################")
        print(f"É {'verdadeiro' if afd.check_input(input) else 'Falso' } que a entrada '{input}' está contida na Linguagem")
        print("######################################################################")

        # Imprimindo as variáveis para verificar se as linhas foram armazenadas corretamente
        arquivo.close()
