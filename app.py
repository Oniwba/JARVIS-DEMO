
import os
import requests
import streamlit as st

# ==========================================
# CONFIGURAÇÕES
# ==========================================

st.set_page_config(
    page_title="JARVIS | Assistente Pessoal",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

MODELO_PADRAO = "openai/gpt-oss-120b"

URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

INSTRUCOES = """
Você é JARVIS, um assistente virtual inteligente,
inspirado em assistentes futuristas.

PERSONALIDADE:
- Inteligente, educado e objetivo.
- Fale sempre em português brasileiro.
- Converse naturalmente.
- Seja prestativo e explique claramente.
- Use humor leve quando apropriado.
- Não invente informações.
- Chame-se sempre JARVIS.

LIMITAÇÕES:
Você é uma demonstração virtual.
Não controla o computador do usuário.
Não executa comandos reais no sistema.
"""

# ==========================================
# ESTILO VISUAL
# ==========================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            #102b49 0%,
            #071321 45%,
            #030811 100%
        );
    color: #e5f4ff;
}

header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

.block-container {
    max-width: 1000px;
    padding-top: 2rem;
    padding-bottom: 5rem;
}

.jarvis-title {
    text-align: center;
    color: #52c8ff;
    font-size: 48px;
    font-weight: 800;
    letter-spacing: 12px;
    text-shadow: 0 0 15px #008cff;
    margin-bottom: 0;
}

.jarvis-subtitle {
    text-align: center;
    color: #83b9d9;
    letter-spacing: 5px;
    font-size: 12px;
    margin-bottom: 30px;
}

.orb-container {
    display: flex;
    justify-content: center;
    margin: 25px 0 35px 0;
}

.orb {
    width: 145px;
    height: 145px;
    border-radius: 50%;
    background:
        radial-gradient(
            circle,
            #d8f8ff 0%,
            #55cfff 15%,
            #0876c9 40%,
            #03152c 72%
        );

    box-shadow:
        0 0 20px #00aaff,
        0 0 45px #0077ff,
        0 0 85px #0044aa;

    animation: pulse 3s infinite ease-in-out;
}

@keyframes pulse {
    0%, 100% {
        transform: scale(1);
        box-shadow:
            0 0 20px #00aaff,
            0 0 45px #0077ff,
            0 0 85px #0044aa;
    }

    50% {
        transform: scale(1.08);
        box-shadow:
            0 0 30px #00ccff,
            0 0 65px #0088ff,
            0 0 110px #0055cc;
    }
}

.status {
    text-align: center;
    color: #42d9ff;
    font-size: 12px;
    letter-spacing: 4px;
    margin-bottom: 25px;
}

[data-testid="stChatMessage"] {
    background: rgba(12, 36, 58, 0.72);
    border: 1px solid rgba(40, 160, 255, 0.25);
    border-radius: 12px;
}

[data-testid="stChatInput"] {
    border: 1px solid #168bd1;
    border-radius: 12px;
}

.stButton button {
    background: #082d4c;
    color: #65d8ff;
    border: 1px solid #168bd1;
    border-radius: 8px;
}

.stButton button:hover {
    background: #104b73;
    color: white;
    border-color: #50caff;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# CABEÇALHO
# ==========================================

st.markdown(
    '<div class="jarvis-title">JARVIS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="jarvis-subtitle">'
    'PERSONAL ARTIFICIAL INTELLIGENCE'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="orb-container">
    <div class="orb"></div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="status">● SYSTEM ONLINE</div>',
    unsafe_allow_html=True
)

# ==========================================
# CONFIGURAÇÃO DA API GROQ
# ==========================================

def obter_configuracao():

    chave = ""

    try:
        chave = st.secrets.get("GROQ_API_KEY", "")
    except Exception:
        pass

    if not chave:
        chave = os.getenv("GROQ_API_KEY", "")

    modelo = MODELO_PADRAO

    try:
        modelo = st.secrets.get(
            "JARVIS_MODEL",
            MODELO_PADRAO
        )
    except Exception:
        pass

    modelo = os.getenv("JARVIS_MODEL", modelo)

    return chave, modelo


# ==========================================
# FUNÇÃO DE CONVERSAÇÃO
# ==========================================

def conversar(historico):

    chave, modelo = obter_configuracao()

    if not chave:
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
            "Authorization": f"Bearer {chave}",
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

        try:
            detalhes = resposta.json().get(
                "error", {}
            ).get(
                "message",
                resposta.text
            )
        except Exception:
            detalhes = resposta.text

        raise RuntimeError(
            f"Erro da API Groq ({resposta.status_code}): "
            f"{detalhes}"
        )

    dados = resposta.json()

    return dados["choices"][0]["message"]["content"]


# ==========================================
# MEMÓRIA DA CONVERSA
# ==========================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# ==========================================
# BARRA LATERAL
# ==========================================

with st.sidebar:

    st.markdown("## ⚙️ Configurações")

    st.write("**JARVIS DEMO 1.3**")

    st.caption(
        "Assistente virtual conectado à inteligência artificial Groq."
    )

    if st.button(
        "🗑️ Limpar conversa",
        use_container_width=True
    ):
        st.session_state.mensagens = []
        st.rerun()

    st.divider()

    st.markdown("### Informações")

    st.write("Status: Online")
    st.write("Inteligência: Groq AI")
    st.write("Interface: Streamlit")

    st.caption(
        "Demonstração virtual. "
        "Não executa comandos reais no computador."
    )


# ==========================================
# MENSAGEM INICIAL
# ==========================================

if not st.session_state.mensagens:

    st.markdown(
        "**JARVIS:** Sistemas inicializados. "
        "Olá! Como posso ajudar você hoje?"
    )


# ==========================================
# EXIBIR HISTÓRICO
# ==========================================

for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):

        st.markdown(mensagem["content"])


# ==========================================
# ENTRADA DO USUÁRIO
# ==========================================

pergunta = st.chat_input(
    "Digite uma mensagem para o JARVIS..."
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

            except requests.exceptions.Timeout:

                resposta = (
                    "A conexão demorou demais. "
                    "Tente novamente."
                )

                st.error(resposta)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resposta
                })

            except requests.exceptions.RequestException:

                resposta = (
                    "Não consegui estabelecer conexão "
                    "com a API da Groq. Verifique sua internet."
                )

                st.error(resposta)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resposta
                })

            except Exception as erro:

                resposta = f"Falha na comunicação: {erro}"

                st.error(resposta)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resposta
                })


# ==========================================
# RODAPÉ
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        color:#527d9c;
        font-size:11px;
        letter-spacing:3px;
    ">
        JARVIS PERSONAL AI SYSTEM • DEMO VERSION 1.3
    </div>
    """,
    unsafe_allow_html=True
)
