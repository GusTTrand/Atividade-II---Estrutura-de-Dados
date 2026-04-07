class No:
    def __init__(self, dado):
        #Cada 'No' guarda o seu valor e duas setas
        self.dado = dado
        self.anterior = None
        self.proximo = None

class Lista:
    def __init__(self):
        #A lista começa vazia e controlamos o tamanho para facilitar inserções
        self.inicio = None
        self.tamanho = 0

    def inserir(self, dado):
        # Método para inserir no final da lista
        novo_no = No(dado)
        
        #Primeiro Cenário, se a lista tá vazia. O nó aponta para ele mesmo
        if self.inicio == None:
            self.inicio = novo_no
            novo_no.proximo = novo_no
            novo_no.anterior = novo_no
        #Segundo Cenário, se tiver elemento encontra o ultimo e refaz o círculo
        else:
            ultimo = self.inicio.anterior
            
            novo_no.proximo = self.inicio
            novo_no.anterior = ultimo
            ultimo.proximo = novo_no
            self.inicio.anterior = novo_no
            
        self.tamanho = self.tamanho + 1

    def Inserir(self, posicao, dado):
        #Método para inserir em uma posição especifica
        
        if self.inicio == None or posicao > self.tamanho:
            self.inserir(dado)
            return
        
        novo_no = No(dado)
        
        #Primeiro cenário, - inserir na primeira posição
        if posicao <= 1:
            ultimo = self.inicio.anterior
            
            novo_no.proximo = self.inicio
            novo_no.anterior = ultimo
            ultimo.proximo = novo_no
            self.inicio.anterior = novo_no
            
            self.inicio = novo_no
            
        #Segundo cenário - inserir no meio
        else:
            atual = self.inicio
            contador = 1
            while contador < posicao - 1:
                atual = atual.proximo
                contador = contador + 1
                
            novo_no.proximo = atual.proximo
            novo_no.anterior = atual
            atual.proximo.anterior = novo_no
            atual.proximo = novo_no
        
        self.tamanho = self.tamanho + 1

    #Imprimir, vai percorrer tudo e vai imprimir no terminal
    def Imprimir(self):
        if self.inicio == None:
            print("Lista vazia.")
            return
            
        atual = self.inicio
        while True:
            print(atual.dado)
            atual = atual.proximo
            if atual == self.inicio:
                break

    #Serve para procurar um valor espeficico e apagar ele
    def remover(self, dado):
        if self.inicio == None:
            print("A lista esta vazia.")
            return
        
        atual = self.inicio
        while True:
            if atual.dado == dado:
                if self.tamanho == 1:
                    self.inicio = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                    if atual == self.inicio:
                        self.inicio = atual.proximo
                self.tamanho = self.tamanho - 1
                print("Dado removido com sucesso!")
                return
            
            atual = atual.proximo
            if atual == self.inicio:
                print("Dado nao encontrado na lista.")
                break

minha_lista = Lista()
opcao = 0

#Inicio da aplicação
print("=== TESTE DA QUESTAO 1 (Lista Circular) ===")

while opcao != 5:
    print("\n--- Menu da Lista ---")
    print("1. Inserir dado no final")
    print("2. Inserir dado em posicao especifica")
    print("3. Remover dado")
    print("4. Imprimir lista")
    print("5. Sair")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        valor = input("Digite o dado a ser inserido no final: ")
        minha_lista.inserir(valor)
        print("Dado inserido!")
        
    elif opcao == 2:
        pos = int(input("Digite a posicao numerica (ex: 1, 2, 3...): "))
        valor = input("Digite o dado a ser inserido: ")
        minha_lista.Inserir(pos, valor)
        print("Dado inserido!")
        
    elif opcao == 3:
        valor = input("Digite o dado a ser removido: ")
        minha_lista.remover(valor)
        
    elif opcao == 4:
        print("\n--- Conteudo da Lista ---")
        minha_lista.Imprimir()
        print("-------------------------")
        
    elif opcao == 5:
        print("Encerrando a aplicacao...")
        
    else:
        print("Opcao invalida. Tente novamente.")
