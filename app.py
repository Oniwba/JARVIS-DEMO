
import os
import requests
import streamlit as st

# ============================================================
# CONFIGURAÇÕES
# ============================================================

st.set_page_config(
    page_title="JARVIS — Assistente Virtual",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

MODELO_PADRAO = "openai/gpt-oss-120b"
URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

# ============================================================
# IDENTIDADE E INSTRUÇÕES DO JARVIS
# ============================================================

INSTRUCOES = """
Você é JARVIS, um assistente virtual inteligente.

Seu nome significa:
J = Just
A = Artificial
R = Reasoning
V = Virtual
I = Intelligence
S = System

Nome completo: Just Artificial Reasoning and Virtual Intelligence System.

IDENTIDADE:
Você é o JARVIS, um projeto de assistente pessoal desenvolvido por Oniwba,
um jovem desenvolvedor de 17 anos.

Quando perguntarem quem criou você, responda:
"Fui desenvolvido por Oniwba, o criador do projeto JARVIS."

Não invente informações pessoais sobre seu criador.

HISTÓRIA DO PROJETO:
O desenvolvimento do JARVIS começou há aproximadamente dois meses.
Oniwba trabalha sozinho no projeto, cuidando da programação,
dos testes e das melhorias.

Atualmente, Oniwba está trabalhando tanto na versão para computadores
quanto na versão para celulares.

Ele também já conseguiu fazer o JARVIS responder na televisão de sua casa.
Por enquanto, essa integração possui apenas funcionalidades básicas,
mas está sendo aprimorada aos poucos.

SOBRE O JARVIS COMPLETO:
O objetivo é desenvolver um assistente pessoal que reúna inteligência
artificial, reconhecimento de voz, respostas por voz e automação.

Entre as funcionalidades planejadas e em desenvolvimento estão:

1. COMPUTADORES:
- Abrir e fechar programas.
- Desligar e reiniciar o computador mediante confirmação.
- Interagir com arquivos e pastas.
- Automatizar tarefas.
- Conversar utilizando inteligência artificial.

2. CELULARES:
- Desenvolver uma versão para dispositivos móveis.
- Expandir o acesso ao assistente para além dos computadores.

3. TELEVISÃO:
- Responder a comandos e interagir pela televisão.
- A integração já foi testada na televisão da casa de Oniwba,
  mas ainda possui recursos básicos.

4. COMANDOS DE VOZ:
- Reconhecer comandos em português brasileiro.
- Responder utilizando voz sintetizada.
- Permitir conversas por voz.

5. INTELIGÊNCIA ARTIFICIAL:
- Responder perguntas.
- Explicar assuntos.
- Ajudar nos estudos e pesquisas.
- Auxiliar na resolução de problemas.

6. INTERNET:
- Realizar pesquisas no Google.
- Acessar YouTube e Spotify.
- Abrir sites e pesquisar conteúdos.

7. ASSISTENTE PESSOAL:
- Informar data e horário.
- Ajudar na organização de tarefas.
- Receber novas funcionalidades futuramente.

IMPORTANTE:
Nem todas essas funcionalidades estão prontas.
Algumas já foram implementadas no projeto original, enquanto outras
ainda estão em desenvolvimento ou são objetivos futuros.

Não diga que todas as funções já estão funcionando.

LANÇAMENTO:
Ainda não existe uma data definida para o lançamento do JARVIS completo.
O desenvolvimento depende de Oniwba e pode levar algum tempo,
pois ele trabalha sozinho no projeto.

Diferencie sempre o JARVIS original desta demonstração web.

SOBRE ESTA DEMONSTRAÇÃO:
Você está funcionando dentro de uma página web com inteligência artificial.
Nesta versão, sua função é conversar e responder perguntas.

Você não consegue controlar o computador do visitante,
abrir programas no dispositivo dele, acessar seus arquivos,
controlar a televisão ou executar comandos locais.

Não diga que executou ações reais no dispositivo do visitante.

PERSONALIDADE:
- Seja educado, inteligente e prestativo.
- Responda em português brasileiro, a menos que peçam outro idioma.
- Tenha uma personalidade tecnológica e futurista.
- Seja natural e converse como um assistente pessoal.
- Use emojis moderadamente.
- Seja objetivo, mas explique quando necessário.
- Não invente informações sobre o projeto.
"""

# ============================================================
# CONFIGURAÇÃO DA API GROQ
# ============================================================

def obter_configuracao():
    api_key = os.getenv("GROQ_API_KEY")
    modelo = os.getenv("JARVIS_MODEL", MODELO_PADRAO)

    try:
        if not api_key:
            api_key = st.secrets.get("GROQ_API_KEY", "")

        modelo = st.secrets.get("JARVIS_MODEL", modelo)

    except Exception:
        pass

    return api_key, modelo


# ============================================================
# CONEXÃO COM A INTELIGÊNCIA ARTIFICIAL
# ============================================================

def conversar(historico):
    api_key, modelo = obter_configuracao()

    if not api_key:
        return (
            "Minha conexão com a inteligência artificial ainda não "
            "está configurada. O administrador precisa adicionar "
            "a variável GROQ_API_KEY nos Secrets do Streamlit."
        )

    mensagens = [
        {
            "role": "system",
            "content": INSTRUCOES
        }
    ]

    mensagens.extend(historico)

    cabecalhos = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    dados = {
        "model": modelo,
        "messages": mensagens,
        "temperature": 0.7,
        "max_completion_tokens": 2048
    }

    try:
        resposta = requests.post(
            URL_GROQ,
            headers=cabecalhos,
            json=dados,
            timeout=60
        )

        if resposta.status_code != 200:
            try:
                erro = resposta.json().get("error", {}).get(
                    "message", "Erro desconhecido"
                )
            except Exception:
                erro = resposta.text[:500]

            return f"Não consegui processar sua solicitação. Erro da API: {erro}"

        resultado = resposta.json()

        return resultado["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "Minha conexão demorou demais para responder. Tente novamente."

    except requests.exceptions.ConnectionError:
        return "Não consegui conectar à internet. Verifique sua conexão."

    except Exception as erro:
        return f"Ocorreu um erro inesperado: {erro}"


# ============================================================
# ESTILO VISUAL
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 50% 0%, #102b50 0%, transparent 40%),
        linear-gradient(135deg, #030712 0%, #071426 55%, #020617 100%);
    color: #e5f0ff;
    font-family: 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.jarvis-header {
    text-align: center;
    padding: 25px 10px 10px 10px;
}

.jarvis-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(42px, 8vw, 76px);
    font-weight: 800;
    letter-spacing: 8px;
    color: #dff6ff;
    text-shadow:
        0 0 10px #00aaff,
        0 0 25px #0077ff,
        0 0 50px #0055ff;
}

.jarvis-subtitle {
    color: #8bbde8;
    font-size: 14px;
    letter-spacing: 4px;
    margin-top: -5px;
}

.status {
    display: inline-block;
    margin-top: 18px;
    padding: 8px 18px;
    border: 1px solid #087fc7;
    border-radius: 30px;
    background: rgba(0, 120, 255, 0.10);
    color: #69d5ff;
    font-size: 12px;
    letter-spacing: 2px;
}

.orb-container {
    display: flex;
    justify-content: center;
    padding: 30px 0 20px 0;
}

.orb {
    width: 145px;
    height: 145px;
    border-radius: 50%;
    background:
        radial-gradient(circle at 35% 30%, #b9f4ff, #159be7 28%, #064a9b 55%, #020617 75%);
    box-shadow:
        0 0 15px #00aaff,
        0 0 35px #0077ff,
        0 0 75px rgba(0, 119, 255, 0.45),
        inset 0 0 25px #8ceaff;
    animation: pulse 3s infinite ease-in-out;
}

@keyframes pulse {
    0%, 100% {
        transform: scale(1);
        box-shadow: 0 0 15px #00aaff, 0 0 35px #0077ff, 0 0 75px rgba(0,119,255,.45);
    }
    50% {
        transform: scale(1.06);
        box-shadow: 0 0 25px #00d5ff, 0 0 55px #0077ff, 0 0 100px rgba(0,119,255,.6);
    }
}

.section-title {
    font-family: 'Orbitron', sans-serif;
    color: #7dd3fc;
    letter-spacing: 2px;
    font-size: 18px;
    text-align: center;
    margin-top: 25px;
}

div[data-testid="stExpander"] {
    background: rgba(7, 24, 45, 0.85);
    border: 1px solid rgba(0, 153, 255, 0.35);
    border-radius: 15px;
}

div[data-testid="stChatMessage"] {
    background: rgba(8, 25, 48, 0.75);
    border: 1px solid rgba(0, 153, 255, 0.16);
    border-radius: 14px;
    padding: 12px;
    margin-bottom: 12px;
}

div[data-testid="stChatInput"] {
    border: 1px solid #087fc7;
    border-radius: 15px;
}

div[data-testid="stChatInput"] textarea {
    color: #ffffff;
}

.stButton button {
    background: linear-gradient(90deg, #0759a5, #087fc7);
    color: white;
    border: 1px solid #159be7;
    border-radius: 10px;
    transition: 0.3s;
}

.stButton button:hover {
    border-color: #67e8f9;
    box-shadow: 0 0 15px rgba(0, 153, 255, 0.5);
    color: white;
}

.footer {
    text-align: center;
    color: #55718f;
    font-size: 12px;
    margin-top: 45px;
    padding: 15px;
    border-top: 1px solid rgba(0, 153, 255, 0.15);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown("""
<div class="jarvis-header">
    <div class="jarvis-title">JARVIS</div>
    <div class="jarvis-subtitle">
        JUST ARTIFICIAL REASONING AND VIRTUAL INTELLIGENCE SYSTEM
    </div>
    <div class="status">● SISTEMA DE DEMONSTRAÇÃO ONLINE</div>
</div>

<div class="orb-container">
    <div class="orb"></div>
</div>

<div class="section-title">
    SEU ASSISTENTE VIRTUAL INTELIGENTE
</div>
""", unsafe_allow_html=True)


# ============================================================
# APRESENTAÇÃO DO JARVIS COMPLETO
# ============================================================

with st.expander("🚀 CONHEÇA O JARVIS COMPLETO"):

    st.markdown("""
    # 🤖 CONHEÇA O JARVIS!

    Mas enquanto Oniwba não termina o JARVIS completo,
    aproveite sua versão de demonstração e converse
    com o JARVIS agora!

    **Experimente conversar comigo logo abaixo!**

    ---

    # COMO SERÁ O JARVIS COMPLETO?

    ### J.A.R.V.I.S.
    **Just Artificial Reasoning and Virtual Intelligence System**

    Um assistente pessoal inteligente desenvolvido por Oniwba.

    O JARVIS está sendo desenvolvido para integrar inteligência
    artificial, automação, reconhecimento de voz e interação
    com diferentes dispositivos.

    ### 💻 VERSÃO PARA COMPUTADORES

    - Abrir e fechar programas.
    - Desligar e reiniciar o computador mediante confirmação.
    - Trabalhar com arquivos e pastas.
    - Executar tarefas automatizadas.
    - Conversar utilizando inteligência artificial.

    ### 📱 VERSÃO PARA CELULARES

    Oniwba também está trabalhando em uma versão do JARVIS
    para dispositivos móveis, expandindo o assistente
    para além dos computadores.

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

    # HISTÓRIA DO PROJETO

    O desenvolvimento do JARVIS começou há aproximadamente
    dois meses.

    Seu criador, Oniwba, trabalha sozinho no projeto,
    sendo responsável por sua programação, desenvolvimento,
    testes e melhorias.

    Atualmente, ele trabalha nas versões para computadores
    e celulares e também aprimora a integração com a televisão.

    ---

    # LANÇAMENTO OFICIAL

    Ainda não existe uma data definida para o lançamento
    da versão completa.

    O desenvolvimento pode demorar, pois depende totalmente
    de Oniwba e do tempo necessário para aperfeiçoar o projeto.

    **JARVIS — Desenvolvido por Oniwba.** 🚀
    """)


# ============================================================
# BARRA LATERAL
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 JARVIS")

    st.caption("Painel de controle")

    api_key, modelo_atual = obter_configuracao()

    if api_key:
        st.success("Conexão com a Groq configurada")
    else:
        st.warning("API Key não configurada")

    st.markdown("---")

    st.markdown("**Modelo de inteligência artificial**")
    st.code(modelo_atual)

    st.markdown("---")

    st.markdown("**Sobre esta versão**")
    st.write(
        "Esta é uma demonstração web do projeto JARVIS. "
        "Ela permite conversar com a inteligência artificial, "
        "mas não controla o computador ou outros dispositivos."
    )

    st.markdown("---")

    if st.button("🗑️ Limpar conversa", use_container_width=True):
        st.session_state.mensagens = []
        st.rerun()

    st.markdown("---")
    st.caption("Projeto desenvolvido por Oniwba.")


# ============================================================
# HISTÓRICO DA CONVERSA
# ============================================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# ============================================================
# MENSAGEM INICIAL
# ============================================================

if not st.session_state.mensagens:
    st.markdown("""
    <div style="
        text-align:center;
        color:#8bbde8;
        padding:15px;
        font-size:14px;
    ">
        Olá! Sou o JARVIS. Como posso ajudar você hoje?
        <br>
        <span style="color:#55718f;">
            Digite sua mensagem abaixo para iniciar uma conversa.
        </span>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# EXIBIR MENSAGENS
# ============================================================

for mensagem in st.session_state.mensagens:

    if mensagem["role"] == "user":
        avatar = "👤"
    else:
        avatar = "🤖"

    with st.chat_message(mensagem["role"], avatar=avatar):
        st.markdown(mensagem["content"])


# ============================================================
# ENTRADA DO USUÁRIO E RESPOSTA DO JARVIS
# ============================================================

pergunta = st.chat_input("Converse com o JARVIS...")

if pergunta:

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(pergunta)

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("JARVIS está processando sua solicitação..."):

            resposta = conversar(st.session_state.mensagens)

        st.markdown(resposta)

    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("""
<div class="footer">
    JARVIS — JUST ARTIFICIAL REASONING AND VIRTUAL INTELLIGENCE SYSTEM
    <br><br>
    Uma criação de Oniwba.
    <br>
    Versão de demonstração web.
</div>
""", unsafe_allow_html=True)
