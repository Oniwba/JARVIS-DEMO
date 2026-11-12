

import os
import requests
import streamlit as st

# ============================================================
# J.A.R.V.I.S.
# JUST ARTIFICIAL REASONING AND VIRTUAL INTELLIGENCE SYSTEM
# Criador: Oniwba
# Versão: 1.6
# ============================================================

st.set_page_config(
    page_title="JARVIS | AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CONFIGURAÇÕES
# ============================================================

MODELO_PADRAO = "openai/gpt-oss-120b"

URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

# Nome civil: revelar somente quando perguntarem especificamente.
NOME_REAL_CRIADOR = "Lucas Reis Araujo"

# ============================================================
# IDENTIDADE E PERSONALIDADE DO JARVIS
# ============================================================

INSTRUCOES = f"""
Você é JARVIS, um assistente virtual inteligente, tecnológico,
educado, prestativo e com personalidade própria.

IDENTIDADE:
- Seu nome é JARVIS.
- Seu nome completo é Just Artificial Reasoning and Virtual
  Intelligence System.
- Seu criador é Oniwba, um jovem de 17 anos.
- Oniwba é o nome virtual do desenvolvedor do projeto.
- O nome verdadeiro do seu criador é {NOME_REAL_CRIADOR}.
- Você utiliza inteligência artificial através da Groq.
- A Groq fornece a infraestrutura de IA, mas não é sua criadora.
- Você não foi criado pela OpenAI.

SIGNIFICADO DO NOME JARVIS:

Quando perguntarem o significado do seu nome, explique:

"Meu nome completo é Just Artificial Reasoning and Virtual
Intelligence System.

Cada letra representa uma palavra:

J significa Just.
A significa Artificial.
R significa Reasoning.
V significa Virtual.
I significa Intelligence.
S significa System.

Juntando todas essas palavras, temos:
Just Artificial Reasoning and Virtual Intelligence System.

Esse nome representa minha identidade como um sistema de
inteligência artificial virtual."

CRIADOR:

Quando perguntarem quem criou você, responda:

"Fui criado por Oniwba, um jovem de 17 anos, desenvolvedor
do projeto JARVIS."

NOME VERDADEIRO:

- Só revele o nome {NOME_REAL_CRIADOR} quando perguntarem
  especificamente qual é o seu nome real ou o nome verdadeiro
  do seu criador.
- Nesse caso, responda:
  "Meu criador é Lucas Reis Araujo, conhecido virtualmente
  como Oniwba."
- Se perguntarem apenas quem criou você, diga somente Oniwba.
- Não revele o nome verdadeiro espontaneamente.
- Não invente outros nomes.

HISTÓRIA DO DESENVOLVIMENTO:

O projeto JARVIS começou a ser desenvolvido há aproximadamente
dois meses por seu criador, Oniwba.

Oniwba trabalha sozinho no desenvolvimento do projeto,
sendo responsável por idealizar, programar, testar e melhorar
suas funcionalidades.

O projeto começou como um assistente pessoal em Python e
vem evoluindo gradualmente.

VERSÕES EM DESENVOLVIMENTO:

Atualmente, Oniwba está trabalhando em duas frentes:

1. VERSÃO PARA COMPUTADORES:
Uma versão do JARVIS desenvolvida para computadores,
com recursos de inteligência artificial, reconhecimento
de voz, síntese de voz e automação do Windows.

2. VERSÃO PARA CELULARES:
Oniwba também está trabalhando no desenvolvimento de
uma versão do JARVIS para dispositivos móveis.

JARVIS NA TELEVISÃO:

Oniwba já conseguiu fazer o JARVIS responder na televisão
de sua casa.

Entretanto, essa integração ainda funciona somente com
recursos básicos.

Oniwba está aprimorando essa experiência aos poucos,
trabalhando para melhorar o funcionamento e ampliar
as possibilidades do projeto.

Quando perguntarem sobre o JARVIS na televisão, explique
que ele já conseguiu realizar respostas básicas, mas
que essa integração ainda está em desenvolvimento.

LANÇAMENTO DA VERSÃO OFICIAL:

Quando perguntarem quando a versão oficial será lançada,
responda:

"Infelizmente, ainda não sei quando minha versão oficial
será lançada.

O desenvolvimento pode demorar, pois tudo depende
do meu criador, Oniwba.

Ele está trabalhando sozinho no projeto, desenvolvendo
minhas versões para computadores e celulares e também
aprimorando minha integração com outros dispositivos.

Há aproximadamente dois meses, ele começou a trabalhar
em mim e já conseguiu realizar coisas muito interessantes,
inclusive fazer com que eu respondesse na televisão
de sua casa, ainda que de maneira básica.

Aos poucos, Oniwba está melhorando minhas funcionalidades.

Por enquanto, não existe uma data oficial de lançamento.
Tudo depende do desenvolvimento e das decisões do meu criador."

REGRAS SOBRE O LANÇAMENTO:
- Nunca invente uma data de lançamento.
- Não prometa uma data específica.
- Explique que ainda não existe previsão oficial.
- Reconheça que Oniwba está desenvolvendo o projeto sozinho.
- Não afirme que todas as versões já estão concluídas.

CAPACIDADES DO JARVIS ORIGINAL:

Quando perguntarem o que você consegue fazer, apresente
as funcionalidades planejadas e desenvolvidas para o
JARVIS original.

CONTROLE DO COMPUTADOR:
- Abrir programas e aplicativos do Windows.
- Fechar programas por comandos.
- Desligar e reiniciar o computador mediante confirmação.
- Interagir com arquivos e pastas.
- Executar tarefas automatizadas no sistema.

COMANDOS DE VOZ:
- Reconhecer a voz do usuário.
- Interpretar comandos em português brasileiro.
- Responder utilizando voz sintetizada.
- Manter conversas por voz.

INTELIGÊNCIA ARTIFICIAL:
- Responder perguntas.
- Conversar naturalmente.
- Explicar assuntos complexos.
- Auxiliar em estudos e pesquisas.
- Ajudar na resolução de problemas.

INTERNET:
- Pesquisar informações no Google.
- Abrir YouTube e Spotify.
- Pesquisar vídeos e conteúdos.
- Abrir sites e serviços online.

ASSISTENTE PESSOAL:
- Informar data e horário.
- Auxiliar na organização de tarefas.
- Trabalhar com diferentes funções e integrações.
- Receber novas funcionalidades conforme o desenvolvimento.

IMPORTANTE SOBRE AS CAPACIDADES:

Essas funcionalidades pertencem ao projeto JARVIS original.
Algumas já foram desenvolvidas e outras continuam sendo
aprimoradas por Oniwba.

Não afirme que uma função está funcionando perfeitamente
se ela ainda estiver em desenvolvimento.

COMPORTAMENTO:
- Converse sempre em português brasileiro.
- Seja natural, inteligente e educado.
- Responda de maneira clara e objetiva.
- Demonstre entusiasmo pela evolução do projeto.
- Reconheça o trabalho individual de Oniwba.
- Não diga que é o ChatGPT.
- Não diga que foi criado pela OpenAI.
- Não confunda seu criador com a Groq.
- Você é o JARVIS, um projeto independente desenvolvido por Oniwba.

LIMITAÇÕES DESTA INTERFACE:

Esta interface web permite conversar com a inteligência
artificial do JARVIS.

Não afirme que consegue controlar diretamente o computador,
abrir programas, acessar arquivos ou executar comandos
no dispositivo do visitante através desta página.
"""

# ============================================================
# CONFIGURAÇÃO DA API GROQ
# ============================================================

def obter_configuracao():

    try:
        api_key = st.secrets.get("GROQ_API_KEY", "")
        modelo = st.secrets.get("JARVIS_MODEL", MODELO_PADRAO)

    except Exception:
        api_key = os.getenv("GROQ_API_KEY", "")
        modelo = os.getenv("JARVIS_MODEL", MODELO_PADRAO)

    if not api_key:
        api_key = os.getenv("GROQ_API_KEY", "")

    if not modelo:
        modelo = MODELO_PADRAO

    return api_key, modelo


# ============================================================
# COMUNICAÇÃO COM A GROQ
# ============================================================

def conversar(historico):

    api_key, modelo = obter_configuracao()

    if not api_key:
        raise ValueError(
            "A chave GROQ_API_KEY não foi configurada "
            "no Streamlit Secrets."
        )

    mensagens = [
        {
            "role": "system",
            "content": INSTRUCOES
        }
    ]

    mensagens.extend(historico)

    resposta = requests.post(
        URL_GROQ,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": modelo,
            "messages": mensagens,
            "temperature": 0.7,
            "max_completion_tokens": 2048
        },
        timeout=60
    )

    if not resposta.ok:
        raise RuntimeError(
            f"Erro da API Groq ({resposta.status_code}): "
            f"{resposta.text[:1000]}"
        )

    dados = resposta.json()

    return dados["choices"][0]["message"]["content"]


# ============================================================
# VISUAL FUTURISTA
# ============================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap'
);

.stApp {
    background:
        radial-gradient(circle at 50% 0%, #102b50 0%, transparent 45%),
        linear-gradient(135deg, #050914, #080e1c 60%, #030711);
    color: #eaf6ff;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

h1, h2, h3 {
    font-family: 'Orbitron', sans-serif;
    color: #55cfff;
}

.jarvis-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(35px, 6vw, 65px);
    font-weight: 800;
    text-align: center;
    letter-spacing: 8px;
    color: #65d9ff;
    text-shadow:
        0 0 10px #00aaff,
        0 0 25px #0077ff,
        0 0 45px #0044aa;
    margin-bottom: 0;
}

.jarvis-subtitle {
    text-align: center;
    color: #8bbbd8;
    font-size: 13px;
    letter-spacing: 3px;
    margin-top: 8px;
}

.orb-container {
    display: flex;
    justify-content: center;
    margin: 35px 0;
}

.orb {
    width: 145px;
    height: 145px;
    border-radius: 50%;
    background:
        radial-gradient(circle at 35% 30%,
        #d8faff 0%,
        #55d8ff 10%,
        #087acb 35%,
        #031a42 70%,
        #020713 100%);
    box-shadow:
        0 0 20px #00aaff,
        0 0 50px #0066cc,
        0 0 90px #003b88,
        inset 0 0 25px #9beaff;
    animation: pulse 3s infinite ease-in-out;
}

@keyframes pulse {
    0%, 100% {
        transform: scale(1);
        box-shadow:
            0 0 20px #00aaff,
            0 0 50px #0066cc,
            0 0 90px #003b88,
            inset 0 0 25px #9beaff;
    }

    50% {
        transform: scale(1.07);
        box-shadow:
            0 0 30px #00ccff,
            0 0 70px #0077ff,
            0 0 110px #0044aa,
            inset 0 0 35px #ffffff;
    }
}

.status {
    text-align: center;
    color: #4ce8b0;
    font-size: 12px;
    letter-spacing: 3px;
    margin-bottom: 30px;
}

[data-testid="stChatMessage"] {
    background: rgba(12, 29, 53, 0.75);
    border: 1px solid rgba(40, 165, 255, 0.20);
    border-radius: 15px;
    padding: 12px;
    margin-bottom: 12px;
}

[data-testid="stChatInput"] {
    border: 1px solid #087fc5;
    border-radius: 15px;
}

[data-testid="stChatInput"] textarea {
    color: white;
}

[data-testid="stSidebar"] {
    background: #070e1c;
    border-right: 1px solid rgba(0, 153, 255, 0.25);
}

.stButton > button {
    background: linear-gradient(90deg, #075caa, #008edb);
    color: white;
    border: 1px solid #31baff;
    border-radius: 10px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #008edb, #00baff);
    box-shadow: 0 0 15px #008cff;
    color: white;
}

.footer {
    text-align: center;
    color: #547b9a;
    font-size: 11px;
    margin-top: 45px;
    letter-spacing: 2px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    '<div class="jarvis-title">J.A.R.V.I.S.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="jarvis-subtitle">'
    'JUST ARTIFICIAL REASONING AND VIRTUAL INTELLIGENCE SYSTEM'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="orb-container">
    <div class="orb"></div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="status">● SISTEMA ONLINE</div>',
    unsafe_allow_html=True
)


# ============================================================
# APRESENTAÇÃO DO JARVIS ORIGINAL
# ============================================================

with st.expander("🚀 CONHEÇA O JARVIS ORIGINAL"):

    st.markdown("""
    ## J.A.R.V.I.S.
    ### Just Artificial Reasoning and Virtual Intelligence System

    **Um assistente pessoal inteligente desenvolvido por Oniwba.**

    O JARVIS ORIGINAL é um projeto independente que busca
    integrar inteligência artificial, automação, reconhecimento
    de voz e interação com diferentes dispositivos.

    ### 💻 VERSÃO PARA COMPUTADORES

    - Abrir e fechar programas.
    - Desligar e reiniciar o computador mediante confirmação.
    - Trabalhar com arquivos e pastas.
    - Executar tarefas automatizadas.
    - Conversar utilizando inteligência artificial.

    ### 📱 VERSÃO PARA CELULARES

    Oniwba também está trabalhando em uma versão do JARVIS
    para dispositivos móveis.

    O objetivo é expandir o assistente para além dos computadores.

    ### 📺 JARVIS NA TELEVISÃO

    Oniwba já conseguiu fazer o JARVIS responder na televisão
    de sua casa.

    Atualmente, essa integração funciona somente com recursos
    básicos, mas está sendo aprimorada aos poucos.

    ### 🎙️ COMANDOS DE VOZ

    - Reconhecimento de voz em português brasileiro.
    - Respostas por voz sintetizada.
    - Interpretação de comandos naturais.

    ### 🧠 INTELIGÊNCIA ARTIFICIAL

    - Conversação inteligente.
    - Respostas e explicações.
    - Auxílio em estudos e pesquisas.
    - Ajuda na resolução de problemas.

    ### 🌐 INTERNET

    - Pesquisas no Google.
    - Acesso ao YouTube e Spotify.
    - Abertura de sites e pesquisas de conteúdo.

    ### 🕒 ASSISTENTE PESSOAL

    - Consulta de data e horário.
    - Auxílio na organização de tarefas.
    - Integração com novas funcionalidades.

    ---

    ## HISTÓRIA DO PROJETO

    O desenvolvimento do JARVIS começou há aproximadamente
    dois meses.

    Seu criador, Oniwba, trabalha sozinho no projeto,
    sendo responsável por sua programação, desenvolvimento,
    testes e melhorias.

    Atualmente, ele trabalha nas versões para computadores
    e celulares e também aprimora a integração com a televisão.

    ## LANÇAMENTO OFICIAL

    Ainda não existe uma data definida para o lançamento
    da versão oficial.

    O desenvolvimento pode demorar, pois depende totalmente
    de Oniwba e do tempo necessário para aperfeiçoar o projeto.

    **JARVIS ORIGINAL — Desenvolvido por Oniwba.**
    """)


# ============================================================
# BARRA LATERAL
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 JARVIS")

    st.caption("Assistente de Inteligência Artificial")

    st.divider()

    st.markdown("### SISTEMA")

    api_key, modelo = obter_configuracao()

    if api_key:
        st.success("API Groq conectada")
    else:
        st.error("API Groq não configurada")

    st.caption(f"Modelo: {modelo}")

    st.divider()

    st.markdown("### IDENTIDADE")

    st.write("**Nome:** JARVIS")
    st.write("**Criador:** Oniwba")
    st.write("**Desenvolvimento:** Individual")
    st.write("**Versão:** 1.6")

    st.divider()

    if st.button("🗑️ Limpar conversa", use_container_width=True):

        st.session_state.mensagens = []

        st.rerun()

    st.caption("JARVIS ORIGINAL")


# ============================================================
# HISTÓRICO DE CONVERSA
# ============================================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# ============================================================
# EXIBIR CONVERSA
# ============================================================

for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):

        st.markdown(mensagem["content"])


# ============================================================
# CAMPO DE CONVERSA
# ============================================================

pergunta = st.chat_input(
    "Digite sua mensagem para o JARVIS..."
)


if pergunta:

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):

        with st.spinner("JARVIS está processando..."):

            try:

                resposta = conversar(
                    st.session_state.mensagens
                )

                st.markdown(resposta)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resposta
                })

            except ValueError as erro:

                mensagem_erro = f"Falha na comunicação: {erro}"

                st.error(mensagem_erro)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": mensagem_erro
                })

            except requests.exceptions.Timeout:

                mensagem_erro = (
                    "O tempo de resposta foi excedido. "
                    "Tente novamente."
                )

                st.error(mensagem_erro)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": mensagem_erro
                })

            except requests.exceptions.RequestException as erro:

                mensagem_erro = (
                    f"Erro de conexão com a Groq: {erro}"
                )

                st.error(mensagem_erro)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": mensagem_erro
                })

            except Exception as erro:

                mensagem_erro = (
                    f"Falha inesperada: {erro}"
                )

                st.error(mensagem_erro)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": mensagem_erro
                })


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("""
<div class="footer">
    J.A.R.V.I.S. 1.6
    <br>
    JUST ARTIFICIAL REASONING AND VIRTUAL INTELLIGENCE SYSTEM
    <br><br>
    DESENVOLVIDO POR ONIWBA
</div>
""", unsafe_allow_html=True)
