class No:
    def __init__(self, nome, prioritario):
        self.nome = nome
        self.prioritario = prioritario
        self.anterior = None
        self.proximo = None

class FilaHospital:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir(self, nome, prioritario):
        novo_no = No(nome, prioritario)
        
        if self.inicio == None:
            self.inicio = novo_no
        else:
            if prioritario == True:
                if self.inicio.prioritario == False:
                    novo_no.proximo = self.inicio
                    self.inicio.anterior = novo_no
                    self.inicio = novo_no
                else:
                    atual = self.inicio
                    while atual.proximo != None and atual.proximo.prioritario == True:
                        atual = atual.proximo
                    
                    novo_no.proximo = atual.proximo
                    novo_no.anterior = atual
                    atual.proximo = novo_no
                    if novo_no.proximo != None:
                        novo_no.proximo.anterior = novo_no
            else:
                atual = self.inicio
                while atual.proximo != None:
                    atual = atual.proximo
                atual.proximo = novo_no
                novo_no.anterior = atual
                
        self.tamanho = self.tamanho + 1

    def atender(self):
        if self.inicio == None:
            return None
        
        paciente_atendido = self.inicio
        self.inicio = self.inicio.proximo
        
        if self.inicio != None:
            self.inicio.anterior = None
            
        self.tamanho = self.tamanho - 1
        return paciente_atendido

    def exibir(self):
        if self.inicio == None:
            print("A fila esta vazia.")
            return
            
        atual = self.inicio
        while atual != None:
            if atual.prioritario == True:
                tipo = "PRIO"
            else:
                tipo = "COMUM"
            print("Nome:", atual.nome, "| Tipo:", tipo)
            atual = atual.proximo

    def buscar(self, nome):
        atual = self.inicio
        posicao = 0
        encontrado = False
        
        while atual != None:
            if atual.nome == nome:
                if atual.prioritario == True:
                    tipo = "PRIO"
                else:
                    tipo = "COMUM"
                print("Paciente:", atual.nome, "| Posicao:", posicao, "| Tipo:", tipo)
                encontrado = True
                break
            atual = atual.proximo
            posicao = posicao + 1
            
        if encontrado == False:
            print("Paciente nao encontrado na fila.")

# --- INICIO DA APLICACAO E TESTES ---
print("=== TESTE DA QUESTAO 3 (A Fila do Hospital Central) ===")
print("Para reproduzir o exemplo do PDF (Pagina 6), insira a seguinte sequencia:")
print("1. Inserir (1) -> Nome: Carlos  -> Prioritario? n")
print("2. Inserir (1) -> Nome: Ana     -> Prioritario? s")
print("3. Inserir (1) -> Nome: Beatriz -> Prioritario? n")
print("4. Inserir (1) -> Nome: Pedro   -> Prioritario? s")
print("5. Inserir (1) -> Nome: Silvia  -> Prioritario? n")
print("6. Exibir  (3) -> A ordem final devera ser: Ana, Pedro, Carlos, Beatriz, Silvia.\n")
print("-" * 65)

fila = FilaHospital()
opcao = 0

while opcao != 5:
    print("\n--- Sistema do Hospital Central ---")
    print("1. Inserir paciente")
    print("2. Atender paciente")
    print("3. Exibir fila")
    print("4. Buscar paciente")
    print("5. Sair")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        nome = input("Digite o nome do paciente: ")
        tipo_entrada = input("O paciente e prioritario? (s/n): ")
        if tipo_entrada == "s" or tipo_entrada == "S":
            prioritario = True
        else:
            prioritario = False
        fila.inserir(nome, prioritario)
        print("Paciente inserido na fila.")
        
    elif opcao == 2:
        paciente = fila.atender()
        if paciente != None:
            if paciente.prioritario == True:
                tipo = "PRIO"
            else:
                tipo = "COMUM"
            print("Paciente chamado para atendimento:", paciente.nome, "(", tipo, ")")
        else:
            print("Nao ha pacientes para atender.")
            
    elif opcao == 3:
        fila.exibir()
        
    elif opcao == 4:
        nome_busca = input("Digite o nome do paciente para buscar: ")
        fila.buscar(nome_busca)
        
    elif opcao == 5:
        print("Encerrando o sistema...")
        
    else:
        print("Opcao invalida. Tente novamente.")