import random
from datetime import datetime

import streamlit as st

# ==========================================================
# JARVIS - DEMO 1.0 | Interface Web
# Demonstração segura: não executa comandos do sistema.
# ==========================================================

st.set_page_config(
    page_title="JARVIS | Assistente Pessoal",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Estilo visual ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

.stApp {
    background:
      radial-gradient(ellipse at 50% 8%, rgba(0, 153, 255, .13), transparent 38%),
      linear-gradient(145deg, #030914 0%, #061426 48%, #020711 100%);
    color: #d9efff;
}
header[data-testid="stHeader"] { background: rgba(0,0,0,0); }
.block-container { padding-top: 2rem; max-width: 1250px; }
h1, h2, h3, .jarvis-font { font-family: 'Orbitron', sans-serif !important; }
.hero {
    text-align:center; padding: 18px 10px 10px;
}
.hero-title {
    font-family:'Orbitron',sans-serif; font-size: clamp(2.4rem, 6vw, 4.5rem);
    letter-spacing: .22em; color:#bdeaff; text-shadow:0 0 12px #00aaff, 0 0 32px #0077cc;
    margin:0;
}
.hero-sub {
    color:#64cfff; letter-spacing:.28em; font-size:.78rem;
    font-family:'Orbitron',sans-serif; margin-top:8px;
}
.orb-wrap { display:flex; justify-content:center; padding:22px 0 18px; }
.orb {
    width:190px; height:190px; border-radius:50%; position:relative;
    display:flex; align-items:center; justify-content:center;
    border:1px solid rgba(73,202,255,.85);
    box-shadow:0 0 18px #008dcb, inset 0 0 24px rgba(0,162,255,.22), 0 0 65px rgba(0,128,255,.25);
    background:radial-gradient(circle, rgba(0,150,255,.20), rgba(0,25,55,.22) 60%, transparent 72%);
    animation:pulse 3s ease-in-out infinite;
}
.orb:before,.orb:after {
    content:""; position:absolute; border-radius:50%; border:1px dashed rgba(67,190,255,.7);
}
.orb:before { inset:12px; animation:spin 18s linear infinite; }
.orb:after { inset:-9px; border-style:solid; border-color:rgba(0,140,255,.32); animation:spin 24s linear infinite reverse; }
.orb-core { font-family:'Orbitron',sans-serif; color:#c8f2ff; font-size:1.3rem; letter-spacing:.1em; text-shadow:0 0 12px #00aaff; }
@keyframes spin { to { transform:rotate(360deg); } }
@keyframes pulse { 50% { box-shadow:0 0 32px #00aaff, inset 0 0 34px rgba(0,162,255,.35), 0 0 85px rgba(0,128,255,.35); } }
.panel {
    border:1px solid rgba(39,164,226,.35); border-radius:14px;
    background:linear-gradient(145deg,rgba(7,29,51,.82),rgba(3,13,27,.82));
    padding:16px 18px; box-shadow:0 8px 30px rgba(0,0,0,.18);
}
.panel-label { color:#53caff; font: .72rem 'Orbitron',sans-serif; letter-spacing:.12em; }
.status-dot { color:#54f5bb; }
div[data-testid="stChatMessage"] {
    background:rgba(6,28,48,.72); border:1px solid rgba(35,142,201,.24);
    border-radius:12px; padding:12px;
}
.stButton>button {
    background:linear-gradient(90deg,#075d91,#087eb4); color:#e8f8ff;
    border:1px solid #24baff; border-radius:8px; font-family:'Orbitron',sans-serif;
}
.stButton>button:hover { border-color:#a5eaff; color:white; box-shadow:0 0 14px #008dcc; }
.stTextInput input, .stTextArea textarea {
    background:#06182b !important; color:#e2f6ff !important;
    border:1px solid #17628c !important;
}
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- Estado da sessão ----------
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Olá! Sou o JARVIS. Sistemas demonstrativos iniciados. Como posso ajudar?"
    }]
if "memorias" not in st.session_state:
    st.session_state.memorias = []

def responder(pergunta: str) -> str:
    p = pergunta.lower().strip()

    if any(x in p for x in ("que horas", "hora", "horário")):
        return f"Agora são {datetime.now().strftime('%H:%M:%S')}."
    if any(x in p for x in ("que dia", "data de hoje", "qual a data", "data")):
        return f"Hoje é {datetime.now().strftime('%d/%m/%Y')}."
    if "seu nome" in p or "quem é você" in p:
        return "Meu nome é JARVIS, seu assistente pessoal demonstrativo."
    if "python" in p:
        return "Python é uma linguagem de programação versátil, utilizada em automação, aplicações e inteligência artificial."
    if "inteligência artificial" in p or "ia" == p:
        return "A inteligência artificial permite que sistemas realizem tarefas como interpretar linguagem, reconhecer padrões e apoiar decisões."
    if p.startswith("abrir "):
        nome = p.replace("abrir ", "", 1).strip()
        permitidos = ["calculadora", "bloco de notas", "paint", "explorador de arquivos", "spotify", "youtube", "google"]
        if nome in permitidos:
            return f"Solicitação demonstrativa: abertura de {nome}. Nenhum aplicativo foi realmente iniciado."
        return "Aplicativo não encontrado na demonstração. Experimente calculadora, bloco de notas, Paint, Spotify, YouTube ou Google."
    if p.startswith("tocar ") or p.startswith("música ") or p.startswith("musica "):
        nome = p.split(" ", 1)[1] if " " in p else "música"
        return f"Simulação de reprodução de '{nome}'. Nenhuma mídia foi iniciada."
    if p.startswith("lembrar "):
        memoria = pergunta.split(" ", 1)[1].strip()
        if memoria and memoria not in st.session_state.memorias:
            st.session_state.memorias.append(memoria)
            return "Informação adicionada à memória demonstrativa desta sessão."
        return "Essa informação já está armazenada ou está vazia."
    if "memória" in p or "memoria" in p:
        if not st.session_state.memorias:
            return "Ainda não tenho informações armazenadas nesta sessão."
        return "Estas são minhas memórias:\n" + "\n".join(f"• {m}" for m in st.session_state.memorias)
    if "pausar" in p:
        return "Mídia pausada (simulação)."
    if "continuar" in p:
        return "Reprodução continuada (simulação)."
    if "próxima" in p or "proxima" in p:
        return "Próxima faixa selecionada (simulação)."
    if "anterior" in p:
        return "Faixa anterior selecionada (simulação)."
    if any(x in p for x in ("arquivo", "criar pasta", "excluir arquivo", "renomear")):
        return "Posso demonstrar operações de arquivos, mas esta versão não altera, cria ou exclui nenhum arquivo."
    if p in ("oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"):
        return random.choice(["Olá! Como posso ajudar?", "Saudações! Estou à disposição.", "Sistemas online. O que deseja fazer?"])
    if "ajuda" in p or "comandos" in p:
        return ("Você pode perguntar a hora ou a data, conversar sobre Python e IA, "
                "pedir para abrir um aplicativo (simulação), simular uma música ou usar "
                "'lembrar [informação]' para guardar uma memória nesta sessão.")
    return ("Entendi sua solicitação. Esta é uma demonstração local de respostas predefinidas; "
            "a integração com uma IA generativa ainda não está conectada nesta versão.")

def enviar(pergunta: str):
    pergunta = pergunta.strip()
    if not pergunta:
        return
    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.session_state.messages.append({"role": "assistant", "content": responder(pergunta)})

# ---------- Cabeçalho ----------
st.markdown("""
<div class="hero">
  <p class="hero-title">JARVIS</p>
  <p class="hero-sub">PERSONAL AI • DEMO 1.0</p>
</div>
<div class="orb-wrap"><div class="orb"><div class="orb-core">J.A.R.V.I.S</div></div></div>
""", unsafe_allow_html=True)

# ---------- Barra lateral ----------
with st.sidebar:
    st.markdown("## <span style='color:#62d2ff;font-family:Orbitron'>SISTEMAS</span>", unsafe_allow_html=True)
    st.markdown("<div class='panel'><span class='status-dot'>● ONLINE</span><br><small>Modo demonstração seguro</small><br><small>Interface web ativa</small></div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("**MÓDULOS DISPONÍVEIS**")
    modules = [
        "Conversação demonstrativa", "Aplicativos (simulação)",
        "Mídia (simulação)", "Memória da sessão", "Data e hora"
    ]
    for item in modules:
        st.markdown(f"🟦 {item}")
    st.write("")
    st.markdown("**MEMÓRIAS DA SESSÃO**")
    if st.session_state.memorias:
        for m in st.session_state.memorias:
            st.caption("• " + m)
    else:
        st.caption("Nenhuma memória salva.")
    if st.button("Limpar conversa", use_container_width=True):
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Conversa reiniciada. Sistemas demonstrativos prontos."
        }]
        st.rerun()
    st.caption("JARVIS DEMO 1.0 • Python + Streamlit")

# ---------- Indicadores ----------
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<div class='panel'><div class='panel-label'>STATUS DO SISTEMA</div><h3 style='color:#54f5bb;margin-bottom:0'>ONLINE</h3></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='panel'><div class='panel-label'>HORÁRIO LOCAL DO SERVIDOR</div><h3 style='color:#bdeaff;margin-bottom:0'>{datetime.now().strftime('%H:%M:%S')}</h3></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='panel'><div class='panel-label'>MODO DE OPERAÇÃO</div><h3 style='color:#bdeaff;margin-bottom:0'>DEMO</h3></div>", unsafe_allow_html=True)

st.write("")
st.markdown("<div class='panel-label'>INTERFACE DE COMUNICAÇÃO</div>", unsafe_allow_html=True)

# Histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🤖" if msg["role"] == "assistant" else "👤"):
        st.markdown(msg["content"])

# Entrada
prompt = st.chat_input("Digite um comando para o JARVIS...")
if prompt:
    enviar(prompt)
    st.rerun()

# Sugestões rápidas
st.write("")
st.caption("COMANDOS RÁPIDOS")
quick_cols = st.columns(4)
quick_prompts = ["Que horas são?", "Qual é a data de hoje?", "Fale sobre Python", "Ajuda"]
for col, quick in zip(quick_cols, quick_prompts):
    with col:
        if st.button(quick, use_container_width=True):
            enviar(quick)
            st.rerun()

st.markdown("""
<div style="text-align:center;color:#47738e;font-size:.75rem;padding:28px 0 8px">
JARVIS DEMO 1.0 • Demonstração segura • Nenhum comando do sistema é executado
</div>
""", unsafe_allow_html=True)
