class No:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir(self, dado):
        novo_no = No(dado)
        if self.inicio == None:
            self.inicio = novo_no
            novo_no.proximo = novo_no
            novo_no.anterior = novo_no
        else:
            ultimo = self.inicio.anterior
            novo_no.proximo = self.inicio
            novo_no.anterior = ultimo
            ultimo.proximo = novo_no
            self.inicio.anterior = novo_no
        self.tamanho = self.tamanho + 1

    def Inserir(self, posicao, dado):
        if self.inicio == None or posicao > self.tamanho:
            self.inserir(dado)
            return
        
        novo_no = No(dado)
        if posicao <= 1:
            ultimo = self.inicio.anterior
            novo_no.proximo = self.inicio
            novo_no.anterior = ultimo
            ultimo.proximo = novo_no
            self.inicio.anterior = novo_no
            self.inicio = novo_no
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

    def remover(self, dado):
        if self.inicio == None:
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
                return
            atual = atual.proximo
            if atual == self.inicio:
                break



print("=== TESTES DA QUESTAO 1 ===")

# 1. Criar a lista
minha_lista = Lista()
print("\nLista criada com sucesso.")

print("\n--- Testando inserir(dado) ---")
minha_lista.inserir(10)
minha_lista.inserir(20)
minha_lista.inserir(30)
print("Esperado: 10, 20, 30")
print("Resultado:")
minha_lista.Imprimir()

print("\n--- Testando Inserir(posicao, dado) ---")

print("Inserindo 5 na posicao 1...")
minha_lista.Inserir(1, 5)

print("Inserindo 15 na posicao 3...")
minha_lista.Inserir(3, 15)

print("Inserindo 99 na posicao 100 (maior que o tamanho)...")
minha_lista.Inserir(100, 99)

print("\nEsperado: 5, 10, 15, 20, 30, 99")
print("Resultado:")
minha_lista.Imprimir()

print("\n--- Testando remover(dado) ---")

print("Removendo o 5 (do inicio)...")
minha_lista.remover(5)

print("Removendo o 20 (do meio)...")
minha_lista.remover(20)

print("Removendo o 99 (do final)...")
minha_lista.remover(99)

print("\nEsperado: 10, 15, 30")
print("Resultado:")
minha_lista.Imprimir()

print("\n--- Testando remover um dado inexistente ---")
print("Tentando remover o 50...")
minha_lista.remover(50)
print("A lista deve continuar igual:")
minha_lista.Imprimir()