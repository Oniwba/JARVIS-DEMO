
import os
from datetime import datetime

import streamlit as st
from groq import Groq

# ==========================================
# JARVIS DEMO 1.1
# Assistente pessoal com IA da Groq
# ==========================================

st.set_page_config(
    page_title="JARVIS - Assistente Pessoal",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# CONFIGURAÇÃO DA INTERFACE
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700&display=swap');

.stApp {
    background: radial-gradient(circle at top, #102b49, #020812 65%);
    color: #d9efff;
}

h1, h2, h3 {
    font-family: Orbitron, sans-serif;
}

.jarvis-title {
    text-align: center;
    font-family: Orbitron, sans-serif;
    font-size: 65px;
    color: #55cfff;
    text-shadow: 0 0 20px #008cff;
    letter-spacing: 12px;
}

.subtitle {
    text-align: center;
    color: #54caff;
    letter-spacing: 5px;
}

.orb {
    width: 170px;
    height: 170px;
    border: 3px solid #20aaff;
    border-radius: 50%;
    margin: 30px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 30px #008cff,
                inset 0 0 30px #008cff;
    animation: pulse 3s infinite;
    color: #a8eaff;
    font-family: Orbitron;
    font-size: 20px;
}

@keyframes pulse {
    50% {
        box-shadow: 0 0 60px #00aaff,
                    inset 0 0 50px #008cff;
    }
}

.stChatMessage {
    background: #071b30;
    border: 1px solid #126da0;
    border-radius: 12px;
}

.stButton button {
    background: #075d91;
    color: white;
    border: 1px solid #25aaff;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# CONFIGURAÇÃO DA GROQ
# ==========================================

def obter_chave():
    try:
        return st.secrets.get("GROQ_API_KEY", "")
    except Exception:
        return os.getenv("GROQ_API_KEY", "")


def obter_modelo():
    try:
        return st.secrets.get(
            "JARVIS_MODEL",
            "openai/gpt-oss-120b"
        )
    except Exception:
        return os.getenv(
            "JARVIS_MODEL",
            "openai/gpt-oss-120b"
        )


API_KEY = obter_chave()
MODELO = obter_modelo()


@st.cache_resource
def criar_cliente(chave):
    return Groq(api_key=chave)


# ==========================================
# MEMÓRIA E HISTÓRICO
# ==========================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

if "memorias" not in st.session_state:
    st.session_state.memorias = []


# ==========================================
# INTELIGÊNCIA ARTIFICIAL
# ==========================================

def conversar(pergunta):

    cliente = criar_cliente(API_KEY)

    historico = [
        {
            "role": "system",
            "content": """
            Você é JARVIS, um assistente pessoal inteligente.

            Sua personalidade deve ser:
            - Educada
            - Inteligente
            - Prestativa
            - Objetiva
            - Profissional

            Fale sempre em português brasileiro,
            salvo quando solicitado outro idioma.

            Converse naturalmente com o usuário.
            Entenda perguntas abertas e mantenha
            o contexto da conversa.

            Você está funcionando em uma versão DEMO.
            Não afirme que executou ações no computador,
            pois não possui acesso ao sistema operacional.
            """
        }
    ]

    historico.extend(st.session_state.mensagens)

    historico.append({
        "role": "user",
        "content": pergunta
    })

    resposta = cliente.chat.completions.create(
        model=MODELO,
        messages=historico,
        temperature=0.7,
        max_tokens=1000
    )

    return resposta.choices[0].message.content


# ==========================================
# COMANDOS DEMONSTRATIVOS
# ==========================================

def executar_comando(texto):

    texto = texto.lower().strip()

    if texto == "hora":
        return f"Agora são {datetime.now().strftime('%H:%M:%S')}."

    if texto == "data":
        return f"Hoje é {datetime.now().strftime('%d/%m/%Y')}."

    if texto.startswith("lembrar "):

        memoria = texto[8:].strip()

        if memoria and memoria not in st.session_state.memorias:
            st.session_state.memorias.append(memoria)
            return "Informação adicionada à minha memória demonstrativa."

        return "Essa informação já está armazenada."

    if texto in ("memoria", "memórias", "memorias"):

        if not st.session_state.memorias:
            return "Ainda não tenho memórias armazenadas."

        return "\n".join(
            "- " + m for m in st.session_state.memorias
        )

    return None


# ==========================================
# CABEÇALHO
# ==========================================

st.markdown(
    '<div class="jarvis-title">JARVIS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">PERSONAL AI SYSTEM • DEMO 1.1</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="orb">J.A.R.V.I.S</div>',
    unsafe_allow_html=True
)


# ==========================================
# PAINEL LATERAL
# ==========================================

with st.sidebar:

    st.title("SISTEMAS")

    if API_KEY:
        st.success("INTELIGÊNCIA ARTIFICIAL ONLINE")
    else:
        st.error("API DA GROQ NÃO CONFIGURADA")

    st.write("**MÓDULOS DISPONÍVEIS**")

    st.write("🟢 Conversação com IA")
    st.write("🟢 Memória demonstrativa")
    st.write("🟢 Data e horário")
    st.write("🟢 Processamento de linguagem")

    st.divider()

    st.write("**MINHAS MEMÓRIAS**")

    if st.session_state.memorias:
        for memoria in st.session_state.memorias:
            st.caption("• " + memoria)
    else:
        st.caption("Nenhuma memória armazenada.")

    if st.button("Limpar conversa"):

        st.session_state.mensagens = []
        st.rerun()


# ==========================================
# STATUS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("SISTEMA", "ONLINE")

with col2:
    st.metric(
        "HORÁRIO",
        datetime.now().strftime("%H:%M:%S")
    )

with col3:
    st.metric(
        "MODO",
        "DEMO"
    )


# ==========================================
# CHAT DO JARVIS
# ==========================================

st.divider()

st.subheader("CANAL DE COMUNICAÇÃO")

for mensagem in st.session_state.mensagens:

    with st.chat_message(
        mensagem["role"],
        avatar="🤖" if mensagem["role"] == "assistant" else "👤"
    ):

        st.markdown(mensagem["content"])


# ==========================================
# ENTRADA DO USUÁRIO
# ==========================================

pergunta = st.chat_input(
    "Converse com o JARVIS..."
)

if pergunta:

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(pergunta)

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("JARVIS está pensando..."):

            try:

                resultado = executar_comando(pergunta)

                if resultado is None:

                    if not API_KEY:
                        raise ValueError(
                            "Configure GROQ_API_KEY nos Secrets do Streamlit."
                        )

                    resultado = conversar(pergunta)

                st.markdown(resultado)

                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resultado
                })

            except Exception as erro:

                st.error(
                    f"Erro ao processar solicitação: {erro}"
                )

                st.info(
                    "Verifique sua chave da Groq, "
                    "o modelo configurado e as dependências."
                )


# ==========================================
# RODAPÉ
# ==========================================

st.divider()

st.caption(
    "JARVIS DEMO 1.1 | Desenvolvido em Python | "
    "Inteligência Artificial via Groq"
)

