
"""
JARVIS - ASSISTENTE PESSOAL INTELIGENTE
Versão DEMO 1.0
Demonstração para GitHub

Esta versão demonstra as principais funcionalidades do projeto
original, utilizando simulações seguras.

Nenhum arquivo é alterado e nenhum comando do sistema é executado.
"""

import time
import random
from datetime import datetime


# ==========================================================
# CONFIGURAÇÕES
# ==========================================================

NOME = "JARVIS"
VERSAO = "DEMO 1.0"

AZUL = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
RESET = "\033[0m"
NEGRITO = "\033[1m"


# ==========================================================
# FUNÇÕES VISUAIS
# ==========================================================

def linha():
    print(AZUL + "=" * 60 + RESET)


def digitar(texto, velocidade=0.015):
    for caractere in texto:
        print(caractere, end="", flush=True)
        time.sleep(velocidade)
    print()


def resposta(texto):
    print(f"\n{VERDE}{NEGRITO}JARVIS:{RESET} {texto}")


def carregamento(texto):
    print(f"\n{AMARELO}{texto}", end="", flush=True)

    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print(RESET)


# ==========================================================
# INICIALIZAÇÃO
# ==========================================================

def inicializar():

    print("\n")

    linha()
    print(f"{AZUL}{NEGRITO}")
    print("       J.A.R.V.I.S")
    print("   ASSISTENTE PESSOAL")
    print("       INTELIGENTE")
    print(f"{RESET}")

    linha()

    print(f"Versão: {VERSAO}")
    print("Linguagem: Python")
    print("Modo: Demonstração")

    carregamento("Inicializando sistemas")

    resposta("Olá! Sou o JARVIS.")
    resposta("Sistema demonstrativo iniciado com sucesso.")
    resposta("Digite 'ajuda' para conhecer minhas funcionalidades.")

    linha()


# ==========================================================
# INTELIGÊNCIA ARTIFICIAL SIMULADA
# ==========================================================

def conversar(pergunta):

    pergunta = pergunta.lower()

    respostas = {

        "oi": [
            "Olá! Como posso ajudar?",
            "Saudações! Estou à disposição.",
        ],

        "olá": [
            "Olá! É um prazer falar com você.",
            "Como posso ajudar hoje?",
        ],

        "python": [
            "Python é uma linguagem de programação versátil.",
            "Python permite desenvolver automações, sistemas e aplicações de inteligência artificial.",
        ],

        "inteligência artificial": [
            "A inteligência artificial permite que sistemas executem tarefas que normalmente exigiriam capacidades humanas.",
            "A IA pode ser utilizada em assistentes virtuais, automação e análise de dados.",
        ],

        "seu nome": [
            "Meu nome é JARVIS, seu assistente pessoal.",
        ],

        "como você funciona": [
            "Na versão original, utilizo reconhecimento de voz, processamento de comandos e inteligência artificial.",
        ],
    }

    for palavra, opcoes in respostas.items():

        if palavra in pergunta:
            return random.choice(opcoes)

    return (
        "Entendi sua pergunta! Na versão completa, "
        "posso utilizar uma inteligência artificial "
        "para responder perguntas de diferentes assuntos."
    )


# ==========================================================
# APLICATIVOS
# ==========================================================

def abrir_aplicativo(nome):

    aplicativos = [
        "calculadora",
        "bloco de notas",
        "paint",
        "explorador de arquivos",
        "spotify",
        "youtube",
        "google",
    ]

    if nome in aplicativos:

        carregamento(f"Simulando abertura de {nome}")

        resposta(
            f"Solicitação demonstrativa: abertura de {nome}."
        )

    else:

        resposta("Aplicativo não encontrado na demonstração.")


# ==========================================================
# MÚSICAS
# ==========================================================

def reproduzir_musica(nome):

    carregamento(f"Pesquisando música: {nome}")

    resposta(f"Simulação de reprodução de '{nome}'.")

    print(f"{VERDE}♪ Música selecionada com sucesso!{RESET}")


def controlar_midia(comando):

    acoes = {
        "pausar": "Música pausada (simulação).",
        "continuar": "Reprodução continuada (simulação).",
        "proxima": "Próxima faixa selecionada (simulação).",
        "anterior": "Faixa anterior selecionada (simulação).",
    }

    resposta(acoes.get(comando, "Comando não reconhecido."))


# ==========================================================
# GERENCIAMENTO DE ARQUIVOS
# ==========================================================

def gerenciar_arquivos(acao, nome):

    acoes = {
        "criar": "criação",
        "excluir": "exclusão",
        "mover": "movimentação",
        "renomear": "renomeação",
        "pesquisar": "pesquisa",
    }

    if acao in acoes:

        carregamento(f"Demonstrando {acoes[acao]}")

        resposta(
            f"Operação de {acoes[acao]} do item '{nome}' demonstrada."
        )

        print(
            f"{AMARELO}[DEMO] Nenhum arquivo foi alterado.{RESET}"
        )


# ==========================================================
# MEMÓRIA DEMONSTRATIVA
# ==========================================================

memorias = []


def salvar_memoria(texto):

    if texto and texto not in memorias:

        memorias.append(texto)

        resposta("Informação adicionada à memória demonstrativa.")

    else:

        resposta("Essa informação já está armazenada.")


def mostrar_memorias():

    if not memorias:

        resposta("Ainda não tenho informações armazenadas.")

        return

    resposta("Estas são minhas memórias:")

    for indice, memoria in enumerate(memorias, 1):

        print(f"{indice}. {memoria}")


# ==========================================================
# DATA E HORA
# ==========================================================

def informar_hora():

    agora = datetime.now()

    resposta(
        f"Agora são {agora.strftime('%H:%M:%S')}."
    )


def informar_data():

    hoje = datetime.now()

    resposta(
        f"Hoje é {hoje.strftime('%d/%m/%Y')}."
    )


# ==========================================================
# MENU DE AJUDA
# ==========================================================

def ajuda():

    print(f"""
{AZUL}{NEGRITO}
             FUNCIONALIDADES DO JARVIS
{RESET}

{VERDE}[1] Conversar com a inteligência artificial
[2] Abrir aplicativos
[3] Reproduzir músicas
[4] Controlar mídia
[5] Gerenciar arquivos
[6] Salvar memórias
[7] Consultar memórias
[8] Consultar horário
[9] Consultar data
[10] Conhecer o projeto
[0] Encerrar demonstração
{RESET}

Comandos de texto também estão disponíveis.
""")


# ==========================================================
# SOBRE O PROJETO
# ==========================================================

def sobre():

    print(f"""
{AZUL}{NEGRITO}
============================================================
                    SOBRE O JARVIS
============================================================
{RESET}

O JARVIS é um assistente pessoal desenvolvido em Python.

O projeto original reúne diferentes tecnologias para
proporcionar interação entre o usuário e o computador.

PRINCIPAIS TECNOLOGIAS:

- Python
- Inteligência Artificial (Groq API)
- SpeechRecognition
- PyAudio
- pyttsx3
- PyAutoGUI
- yt-dlp
- Google APIs
- JSON

FUNCIONALIDADES DO PROJETO ORIGINAL:

- Reconhecimento de voz.
- Respostas com inteligência artificial.
- Abertura e fechamento de aplicativos.
- Controle de músicas e vídeos.
- Gerenciamento de arquivos.
- Memória personalizada.
- Integração com serviços Google.

Esta versão é exclusivamente demonstrativa.

============================================================
""")


# ==========================================================
# INTERPRETADOR DE COMANDOS
# ==========================================================

def executar(comando):

    comando = comando.lower().strip()

    if comando in ("sair", "0", "encerrar"):

        resposta("Encerrando a demonstração. Até logo!")

        return False

    elif comando in ("ajuda", "help"):

        ajuda()

    elif comando in ("sobre", "projeto", "10"):

        sobre()

    elif comando in ("hora", "8"):

        informar_hora()

    elif comando in ("data", "9"):

        informar_data()

    elif comando in ("abrir", "2"):

        nome = input("Qual aplicativo deseja demonstrar? ").lower()

        abrir_aplicativo(nome)

    elif comando in ("musica", "3"):

        nome = input("Digite o nome da música: ")

        reproduzir_musica(nome)

    elif comando in ("pausar", "continuar", "proxima", "anterior", "4"):

        if comando == "4":

            comando = input(
                "Digite pausar, continuar, proxima ou anterior: "
            ).lower()

        controlar_midia(comando)

    elif comando in ("arquivos", "5"):

        acao = input(
            "Digite criar, excluir, mover, renomear ou pesquisar: "
        ).lower()

        nome = input("Nome do arquivo: ")

        gerenciar_arquivos(acao, nome)

    elif comando in ("lembrar", "6"):

        texto = input("O que devo lembrar? ")

        salvar_memoria(texto)

    elif comando in ("memorias", "7"):

        mostrar_memorias()

    elif comando in ("conversar", "1"):

        pergunta = input("Você: ")

        carregamento("Processando pergunta")

        resposta(conversar(pergunta))

    else:

        carregamento("Analisando solicitação")

        resposta(conversar(comando))

    return True


# ==========================================================
# EXECUÇÃO PRINCIPAL
# ==========================================================

def main():

    inicializar()

    ajuda()

    while True:

        try:

            comando = input(
                f"\n{AZUL}Você > {RESET}"
            )

            if not executar(comando):

                break

        except KeyboardInterrupt:

            resposta("Demonstração encerrada.")

            break

        except Exception as erro:

            print(f"{VERMELHO}Erro: {erro}{RESET}")


if __name__ == "__main__":

    main()
