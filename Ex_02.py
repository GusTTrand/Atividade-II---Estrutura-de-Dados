class No:
    def __init__(self, nome, tempo_necessario):
        self.nome = nome
        self.tempo_necessario = tempo_necessario
        self.tempo_restante = tempo_necessario
        self.tempo_espera = 0
        self.tempo_retorno = 0
        self.anterior = None
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir(self, nome, tempo_necessario):
        novo_no = No(nome, tempo_necessario)
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

    def remover(self, no_remover):
        if self.inicio == None:
            return
        if self.tamanho == 1:
            self.inicio = None
        else:
            no_remover.anterior.proximo = no_remover.proximo
            no_remover.proximo.anterior = no_remover.anterior
            if no_remover == self.inicio:
                self.inicio = no_remover.proximo
        self.tamanho = self.tamanho - 1

# --- INICIO DA APLICACAO E TESTES ---
print("=== TESTE DA QUESTAO 2 (O Grande Colapso de Synthetica) ===")
print("Para reproduzir o relatorio do PDF, insira os seguintes dados passo a passo:")
print("1. Quantos processos: 4")
print("2. Nome: SemaforoCtrl | Tempo: 8")
print("3. Nome: HospitalLife | Tempo: 4")
print("4. Nome: EnergyGrid   | Tempo: 9")
print("5. Nome: TransportAl  | Tempo: 5")
print("6. Fatia de tempo (quantum): 3\n")
print("-" * 50)

lista_processos = Lista()
lista_finalizados = Lista()

qtd_processos = int(input("Quantos processos deseja inserir? "))
contador = 0
while contador < qtd_processos:
    print("\nProcesso", contador + 1)
    nome = input("Nome do processo: ")
    tempo = int(input("Tempo necessario: "))
    lista_processos.inserir(nome, tempo)
    contador = contador + 1

if lista_processos.tamanho > 0:
    quantum = int(input("\nFatia de tempo (quantum): "))
    
    tempo_atual = 0
    atual = lista_processos.inicio
    
    while lista_processos.tamanho > 0:
        if atual.tempo_restante <= quantum:
            tempo_atual = tempo_atual + atual.tempo_restante
            atual.tempo_restante = 0
            atual.tempo_retorno = tempo_atual
            atual.tempo_espera = atual.tempo_retorno - atual.tempo_necessario
            
            # Salvar na lista de finalizados para gerar o relatorio depois
            lista_finalizados.inserir(atual.nome, atual.tempo_necessario)
            ultimo_finalizado = lista_finalizados.inicio.anterior
            ultimo_finalizado.tempo_espera = atual.tempo_espera
            ultimo_finalizado.tempo_retorno = atual.tempo_retorno
            
            proximo_no = atual.proximo
            lista_processos.remover(atual)
            atual = proximo_no
        else:
            tempo_atual = tempo_atual + quantum
            atual.tempo_restante = atual.tempo_restante - quantum
            atual = atual.proximo

    # --- RELATORIO ---
    print("\nRELATORIO FINAL - ARIA Recovery Module")
    print("Fatia de tempo (quantum):", quantum, "unidades\n")
    
    soma_espera = 0
    atual = lista_finalizados.inicio
    contador = 0
    
    while contador < lista_finalizados.tamanho:
        print("Processo:", atual.nome, "| Tempo Total:", atual.tempo_necessario, "u | Tempo Espera:", atual.tempo_espera, "u | Tempo Retorno:", atual.tempo_retorno, "u")
        soma_espera = soma_espera + atual.tempo_espera
        atual = atual.proximo
        contador = contador + 1
        
    media_espera = soma_espera / lista_finalizados.tamanho
    print("\nMedia de tempo de espera:", media_espera, "u")