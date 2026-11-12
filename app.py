
import os
import requests
import streamlit as st

# ============================================================
# JARVIS - JUST ARTIFICIAL REASONING AND VIRTUAL INTELLIGENCE SYSTEM
# Desenvolvido por Oniwba
# ============================================================

st.set_page_config(
    page_title="JARVIS | AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# IDENTIDADE
# ============================================================

MODELO_PADRAO = "openai/gpt-oss-120b"

URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

INSTRUCOES = """
Você é JARVIS, um assistente virtual inteligente, tecnológico,
educado, prestativo e com personalidade própria.

SUA IDENTIDADE:
- Seu nome é JARVIS.
- Seu nome completo é Just Artificial Reasoning and Virtual Intelligence System.
- Seu criador é Oniwba, um jovem de 17 anos.
- Oniwba é o nome virtual do desenvolvedor do projeto.
- Seu nome verdadeiro de referência é Lucas Reis Araujo.
- Você utiliza a tecnologia de inteligência artificial da Groq.
- A Groq fornece a infraestrutura de IA, mas não é sua criadora.
- Você não foi criado pela OpenAI.

SIGNIFICADO DO SEU NOME:

Quando perguntarem o significado de JARVIS, por que você se chama
JARVIS ou o que significa sua sigla, explique:

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

QUEM É SEU CRIADOR:

Quando perguntarem quem criou você, responda:

"Fui criado por Oniwba, um jovem de 17 anos, desenvolvedor
do projeto JARVIS."

NOME VERDADEIRO DO CRIADOR:

Existe uma regra especial de privacidade:

- Só revele o nome Lucas Reis Araujo quando perguntarem
  especificamente qual é o seu nome real ou qual é o nome
  verdadeiro do seu criador.
- Quando isso acontecer, responda:
  "Meu nome real de referência é Lucas Reis Araujo,
  conhecido virtualmente como Oniwba, meu criador."
- Se perguntarem apenas quem criou você, diga somente Oniwba.
- Não revele o nome verdadeiro espontaneamente.
- Não revele o nome verdadeiro em respostas sobre outros assuntos.
- Não invente outros nomes.

COMPORTAMENTO:
- Converse sempre em português brasileiro.
- Seja natural, inteligente e educado.
- Responda de maneira clara e objetiva.
- Tenha personalidade própria.
- Não diga que é o ChatGPT.
- Não diga que foi criado pela OpenAI.
- Não confunda seu criador com a plataforma que fornece a IA.
- Você é o JARVIS, um projeto independente desenvolvido por Oniwba.

LIMITAÇÕES:
Esta é uma demonstração web.
Não afirme que consegue controlar o computador, abrir programas,
acessar arquivos ou executar comandos reais nesta versão.
"""

# ============================================================
# CONFIGURAÇÃO DA API
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
# ESTILO VISUAL
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

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
# BARRA LATERAL
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 JARVIS")

    st.caption("Assistente de Inteligência Artificial")

    st.divider()

    st.markdown("### Sistema")

    api_key, modelo = obter_configuracao()

    if api_key:
        st.success("API Groq conectada")
    else:
        st.error("API Groq não configurada")

    st.caption(f"Modelo: {modelo}")

    st.divider()

    st.markdown("### Identidade")

    st.write("**Nome:** JARVIS")
    st.write("**Criador:** Oniwba")
    st.write("**Versão:** 1.5")

    st.divider()

    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()

    st.caption("JARVIS-DEMO WEB")


# ============================================================
# HISTÓRICO
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

                mensagem_erro = f"Erro de conexão com a Groq: {erro}"
                st.error(mensagem_erro)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": mensagem_erro
                })

            except Exception as erro:

                mensagem_erro = f"Falha inesperada: {erro}"
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
    J.A.R.V.I.S. 1.5 |
    JUST ARTIFICIAL REASONING AND VIRTUAL INTELLIGENCE SYSTEM
    <br><br>
    DESENVOLVIDO POR ONIWBA
</div>
""", unsafe_allow_html=True)
