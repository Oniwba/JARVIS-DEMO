
import os
import streamlit as st
from groq import Groq

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

INSTRUCOES = """
Você é JARVIS, um assistente virtual inteligente,
inspirado em assistentes futuristas.

Sua personalidade:
- Inteligente, educado e objetivo.
- Fale sempre em português brasileiro.
- Seja prestativo e converse naturalmente.
- Explique assuntos de maneira clara.
- Use humor leve quando apropriado.
- Não invente informações.
- Você é uma demonstração virtual e não controla
  o computador do usuário.
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
            #071321 40%,
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
# CONFIGURAÇÃO DA API
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


def criar_cliente():

    chave, modelo = obter_configuracao()

    if not chave:
        return None, modelo

    cliente = Groq(api_key=chave)

    return cliente, modelo


# ==========================================
# MEMÓRIA DA CONVERSA
# ==========================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

if "cliente" not in st.session_state:
    st.session_state.cliente = None

if "modelo" not in st.session_state:
    st.session_state.modelo = None

# ==========================================
# BARRA LATERAL
# ==========================================

with st.sidebar:

    st.markdown("## ⚙️ Configurações")

    st.write("**JARVIS DEMO 1.2**")

    st.caption("Assistente virtual conectado à IA Groq.")

    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()

    st.divider()

    st.markdown("### Informações")

    st.write("Status: Online")
    st.write("Inteligência: Groq AI")
    st.write("Interface: Streamlit")

    st.caption(
        "Esta é uma demonstração. "
        "O JARVIS não executa comandos reais no computador."
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

    # Exibe e salva a mensagem do usuário
    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user"):
        st.markdown(pergunta)

    # ======================================
    # CONECTAR À GROQ
    # ======================================

    try:

        cliente, modelo = criar_cliente()

        if cliente is None:

            resposta = (
                "Minha conexão com a inteligência artificial "
                "não foi configurada. Verifique a variável "
                "GROQ_API_KEY em Settings → Secrets no "
                "Streamlit Cloud."
            )

        else:

            with st.chat_message("assistant"):

                with st.spinner("JARVIS está processando..."):

                    historico = [
                        {
                            "role": "system",
                            "content": INSTRUCOES
                        }
                    ]

                    # O histórico já contém a pergunta atual.
                    # Não adicionar a pergunta novamente.
                    historico.extend(
                        st.session_state.mensagens
                    )

                    resultado = cliente.chat.completions.create(
                        model=modelo,
                        messages=historico,
                        temperature=0.7,
                        max_completion_tokens=2048
                    )

                    resposta = (
                        resultado.choices[0].message.content
                        or "Não consegui gerar uma resposta."
                    )

                st.markdown(resposta)

        # Salva a resposta
        st.session_state.mensagens.append({
            "role": "assistant",
            "content": resposta
        })

        if cliente is None:
            with st.chat_message("assistant"):
                st.warning(resposta)

    except Exception as erro:

        mensagem_erro = (
            "Não consegui me conectar à inteligência artificial. "
            "Verifique a configuração da API e o modelo selecionado. "
            "Detalhes técnicos: " + str(erro)
        )

        with st.chat_message("assistant"):
            st.error(mensagem_erro)

        st.session_state.mensagens.append({
            "role": "assistant",
            "content": mensagem_erro
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
        JARVIS PERSONAL AI SYSTEM • DEMO VERSION 1.2
    </div>
    """,
    unsafe_allow_html=True
)

