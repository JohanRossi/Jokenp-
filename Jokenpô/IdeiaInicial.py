import random
import time

# contagem regressiva para o começo da rodada
def contagem_regressiva(segundos):
    print("Iniciando a contagem regressiva...")
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)

# define a escolha do computador
def escolha_computador():
    return random.choice(["pedra", "papel", "tesoura"])


def escolha_jogador():
    escolha = ""
    while escolha not in ["pedra", "papel", "tesoura"]:
        escolha = input("Escolha entre pedra, papel ou tesoura: ").lower()
    return escolha


def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        return "jogador"
    else:
        return "computador"

def jogar_rodada():
    print("A rodada vai começar!")
    contagem_regressiva(5)  # Contagem regressiva de 20 segundos
    
    jogador = escolha_jogador()
    computador = escolha_computador()
    
    print(f"Você escolheu: {jogador}")
    print(f"O computador escolheu: {computador}")
    
    vencedor = determinar_vencedor(jogador, computador)
    
    if vencedor == "empate":
        print("Empate! A rodada será reiniciada.")
        return None
    else:
        print(f"O {vencedor} ganhou a rodada!")
        return vencedor

def jogar_fase(fase_numero):
    print(f"\nIniciando a Fase {fase_numero}!")
    vitorias_jogador = 0
    vitorias_computador = 0
    empates = 0
    
    while vitorias_jogador < 2 and vitorias_computador < 2:
        resultado = jogar_rodada()
        
        if resultado == "jogador":
            vitorias_jogador += 1
        elif resultado == "computador":
            vitorias_computador += 1
        else:
            empates += 1
    
    if vitorias_jogador > vitorias_computador:
        print(f"Você venceu a {fase_numero} Fase!")
        return True
    else:
        print(f"Você perdeu a {fase_numero} Fase.")
        return False

def jogo():
    print("Bem-vindo ao jogo de Jokenpô!")
    
    fase_1_vitoria = jogar_fase(1)
    
    if fase_1_vitoria:
        fase_2_vitoria = jogar_fase(2)
        
        if fase_2_vitoria:
            print("\nParabéns! Você venceu o jogo!")
            print("Palmeiras não tem mundial!")
        else:
            print("\nVocê não conseguiu vencer a segunda fase.")
    else:
        print("\nVocê não conseguiu vencer a primeira fase.")

if __name__ == "__main__":
    jogo()
