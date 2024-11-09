import pygame
from random import randint

pygame.init()
relogio = pygame.time.Clock()

# Configurações da tela
tamanhoTela = (1280, 720)
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("Johenpô")

# Imagem dos personagens
folhaSpritesIdle = pygame.image.load("assets/Fighter/Idle.png").convert_alpha()
folhaSpritesHurt = pygame.image.load("assets/Fighter/Hurt.png").convert_alpha()
folhaSpritesAtk1 = pygame.image.load("assets/Fighter/Attack_1.png").convert_alpha()
folhaSpritesAtk2 = pygame.image.load("assets/Fighter/Attack_2.png").convert_alpha()
folhaSpritesAtk3 = pygame.image.load("assets/Fighter/Attack_3.png").convert_alpha()
folhaSpritesShield = pygame.image.load("assets/Fighter/Shield.png").convert_alpha()
folhaSpritesDead = pygame.image.load("assets/Fighter/Dead.png").convert_alpha()

folhaSpritesIdleS = pygame.image.load("assets/Samurai/Idle.png").convert_alpha()


# Imagens das escolhas
pedraimage = pygame.image.load("assets/1 Icons/Icons_14.png").convert_alpha()
tesouraimage = pygame.image.load("assets/1 Icons/Icons_09.png").convert_alpha()
papelimage = pygame.image.load("assets/1 Icons/Icons_25.png").convert_alpha()

# Imagem do background
Background = pygame.image.load("assets/game_background_1/game_background_1.png").convert_alpha()
Background = pygame.transform.scale(Background, (tamanhoTela))

# Inicializar variáveis de animação dos personagens
listFramesIdle = []
listFramesHurt = []
listFramesAtk1 = []
listFramesAtk2 = []
listFramesAtk3 = []
listFramesShield = []
listFramesDead = []

listFramesIdleS = []

# Redimensionar frames para animação
for i in range(6):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale2x(frame)
    listFramesIdle.append(frame)

for i in range(3):
    frame = folhaSpritesHurt.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale2x(frame)
    listFramesHurt.append(frame)

for i in range(4):
    frame = folhaSpritesAtk1.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale2x(frame)
    listFramesAtk1.append(frame)

for i in range(3):
    frame = folhaSpritesAtk2.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale2x(frame)
    listFramesAtk2.append(frame)

for i in range(4):
    frame = folhaSpritesAtk3.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale2x(frame)
    listFramesAtk3.append(frame)

for i in range(2):
    frame = folhaSpritesShield.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale2x(frame)
    listFramesShield.append(frame)

for i in range(3):
    frame = folhaSpritesDead.subsurface(i * 128, 0, 128, 128)
    frame = pygame.transform.scale2x(frame)
    listFramesDead.append(frame)

for i in range(6):
    frameS = folhaSpritesIdleS.subsurface(i * 128, 0, 128, 128)
    frameS = pygame.transform.scale2x(frameS)
    frameS = pygame.transform.flip(frameS, True, False)
    listFramesIdleS.append(frameS)

# Animações do personagem do usuario
indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 5
personagemRect = listFramesIdle[0].get_rect(midbottom=(480, 480))

indexFrameHurt = 0
tempoAnimacaoHurt = 0.0
velocidadeAnimacaoHurt = 5
personagemRect = listFramesHurt[0].get_rect(midbottom=(480, 480))

indexFrameAtk1 = 0
tempoAnimacaoAtk1 = 0.0
velocidadeAnimacaoAtk1 = 5
personagemRect = listFramesAtk1[0].get_rect(midbottom=(480, 480))

indexFrameAtk2 = 0
tempoAnimacaoAtk2 = 0.0
velocidadeAnimacaoAtk2 = 5
personagemRect = listFramesAtk2[0].get_rect(midbottom=(480, 480))

indexFrameAtk3 = 0
tempoAnimacaoAtk3 = 0.0
velocidadeAnimacaoAtk3 = 5
personagemRect = listFramesAtk3[0].get_rect(midbottom=(480, 480))

indexFrameShield = 0
tempoAnimacaoShield = 0.0
velocidadeAnimacaoShield = 5
personagemRect = listFramesShield[0].get_rect(midbottom=(480, 480))

indexFrameDead = 0
tempoAnimacaoDead = 0.0
velocidadeAnimacaoDead = 5
personagemRect = listFramesDead[0].get_rect(midbottom=(480, 480))

# Animações personagem computador
indexFrameIdleS = 0
tempoAnimacaoIdleS = 0.0
velocidadeAnimacaoIdleS = 5
personagemRectS = listFramesIdleS[0].get_rect(midbottom=(800, 480))

# Variáveis para a contagem regressiva
contagem_regressiva = 5  # Contagem regressiva em segundos
tempo_contagem = 0  # Contador de tempo para a contagem regressiva
contador_atual = 5  # Valor da contagem regressiva
escolha_usuario = None  # Armazena a escolha do jogador (1, 2 ou 3)
escolha_computador = None  # Armazena a escolha do computador (1, 2 ou 3)

# Variáveis para a pontuação
pontos_usuario = 0
pontos_computador = 0

# Fonte para exibir texto
fonte = pygame.font.SysFont("Arial", 40)

def escolha_computador_aleatoria():
    return randint(1, 3)

def resultado(esc_usuario, esc_computador):
    """Função que retorna o resultado do round."""
    if esc_usuario == esc_computador:
        return "Empate"
    elif (esc_usuario == 1 and esc_computador == 2) or (esc_usuario == 2 and esc_computador == 3) or (esc_usuario == 3 and esc_computador == 1):
        return "Jogador"
    else:
        return "Computador"

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Atualiza a tela com o fundo
    tela.blit(Background, (0, 0))

    listTeclas = pygame.key.get_pressed()
        
    # Atualizar a contagem regressiva
    tempo_contagem += relogio.get_time() / 1000  # Converte milissegundos para segundos
    if tempo_contagem >= 1:  # A cada 1 segundo
        contador_atual -= 1
        tempo_contagem = 0

    # Se a contagem regressiva acabou, exibe as opções de escolha
    if contador_atual > 0:
        # Exibe a contagem regressiva
        texto_contagem = fonte.render(f"Contagem: {contador_atual}", True, (255, 255, 255))
        tela.blit(texto_contagem, (tamanhoTela[0] // 2 - texto_contagem.get_width() // 2, 50))
    else:
        # Exibe as opções de escolha: Pedra, Tesoura, Papel
        texto_opcoes = fonte.render(f"Escolha: \n1 - Pedra \n2 - Tesoura \n3 - Papel", True, (255, 255, 255))
        tela.blit(texto_opcoes, (tamanhoTela[0] // 2 - texto_opcoes.get_width() // 1, 50))

        # Verifica se o jogador fez uma escolha
        if escolha_usuario is None:
            if listTeclas[pygame.K_1]:
                escolha_usuario = 1
            elif listTeclas[pygame.K_2]:
                escolha_usuario = 2
            elif listTeclas[pygame.K_3]:
                escolha_usuario = 3

        if escolha_usuario is not None:
            # O computador escolhe aleatoriamente
            escolha_computador = escolha_computador_aleatoria()

            # Exibe as escolhas dos jogadores na tela
            if escolha_usuario == 1:
                tela.blit(pedraimage, (tamanhoTela[0] // 3 - 40, tamanhoTela[1] // 2 - 150))  # Jogador escolheu pedra
            elif escolha_usuario == 2:
                tela.blit(tesouraimage, (tamanhoTela[0] // 3 - 40, tamanhoTela[1] // 2 - 150))  # Jogador escolheu tesoura
            elif escolha_usuario == 3:
                tela.blit(papelimage, (tamanhoTela[0] // 3 - 40, tamanhoTela[1] // 2 - 150))  # Jogador escolheu papel

            if escolha_computador == 1:
                tela.blit(pedraimage, (tamanhoTela[0] * 3 // 4.2 - 40, tamanhoTela[1] // 2 - 150))  # Computador escolheu pedra
            elif escolha_computador == 2:
                tela.blit(tesouraimage, (tamanhoTela[0] * 3 // 4.2 - 40, tamanhoTela[1] // 2 - 150))  # Computador escolheu tesoura
            elif escolha_computador == 3:
                tela.blit(papelimage, (tamanhoTela[0] * 3 // 4.2 - 40, tamanhoTela[1] // 2 - 150))  # Computador escolheu papel

            # Verifica o resultado e atualiza a pontuação
            vencedor = resultado(escolha_usuario, escolha_computador)
            if vencedor == "Jogador":
                if escolha_usuario == 1:
                    frame = listFramesAtk1[indexFrameAtk1]
                    tela.blit(frame, personagemRect)
                elif escolha_usuario == 2:
                    frame = listFramesAtk2[indexFrameAtk2]
                    tela.blit(frame, personagemRect)
                elif escolha_usuario == 3:
                    frame = listFramesAtk3[indexFrameAtk3]
                    tela.blit(frame, personagemRect)
                pontos_usuario += 1
                texto_resultado = fonte.render("Você ganhou o round!", True, (0, 255, 0))
            elif vencedor == "Computador":
                if pontos_computador < 1:
                    
                    frame = listFramesHurt[indexFrameHurt]
                    tela.blit(frame, personagemRect)
                    pontos_computador += 1
                    texto_resultado = fonte.render("O computador ganhou o round!", True, (255, 0, 0))
                else:
                    pontos_computador += 1
                    texto_resultado = fonte.render("O computador ganhou o round!", True, (255, 0, 0))
            else:
                frame = listFramesShield[indexFrameShield]
                tela.blit(frame, personagemRect)
                texto_resultado = fonte.render("Empate!", True, (255, 255, 0))

            tela.blit(texto_resultado, (tamanhoTela[0] // 2 - texto_resultado.get_width() // 2, 150))

            tela.blit(frame, personagemRect)
            tela.blit(frameS, personagemRectS)

            # Exibe a pontuação atual
            texto_pontos = fonte.render(f"Você: {pontos_usuario} | Computador: {pontos_computador}", True, (255, 255, 255))
            tela.blit(texto_pontos, (tamanhoTela[0] // 2 - texto_pontos.get_width() // 2, 200))

            # Verifica se alguém ganhou o jogo
            if pontos_usuario == 2:
                texto_vitoria = fonte.render("Parabéns, você ganhou!", True, (0, 255, 0))
                tela.blit(texto_vitoria, (tamanhoTela[0] // 2 - texto_vitoria.get_width() // 2, 250))
            elif pontos_computador == 2:
                frame = listFramesDead[indexFrameDead]
                tela.blit(frame, personagemRect)
                texto_vitoria = fonte.render("O computador ganhou!", True, (255, 0, 0))
                tela.blit(texto_vitoria, (tamanhoTela[0] // 2 - texto_vitoria.get_width() // 2, 250))

            # Pausa antes de reiniciar o jogo
            pygame.display.update()
            pygame.time.wait(2000)  # Pausa de 2 segundos para exibir o resultado

            # Reinicia o jogo se alguém tiver ganho
            if pontos_usuario == 2 or pontos_computador == 2:
                pontos_usuario = 0
                pontos_computador = 0

            # Resetando variáveis
            contador_atual = 5  # Resetando a contagem regressiva
            escolha_usuario = None  # Limpa a escolha do jogador
            escolha_computador = None  # Limpa a escolha do computador
    
    # Animações dos personagens
    tempoAnimacaoIdle += relogio.get_time() / 1000
    tempoAnimacaoIdleS += relogio.get_time() / 1000

    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        indexFrameIdle = (indexFrameIdle + 1) % len(listFramesIdle)
        tempoAnimacaoIdle = 0.0

    if tempoAnimacaoIdleS >= 1 / velocidadeAnimacaoIdleS:
        indexFrameIdleS = (indexFrameIdleS + 1) % len(listFramesIdleS)
        tempoAnimacaoIdleS = 0.0

    frame = listFramesIdle[indexFrameIdle]
    frameS = listFramesIdleS[indexFrameIdleS]

    tela.blit(frame, personagemRect)
    tela.blit(frameS, personagemRectS)

    # Atualiza a tela
    pygame.display.update()

    # Controla o tempo de cada frame
    dt = relogio.tick(60) / 1000
