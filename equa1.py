import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="Equação do 1º Grau",
    page_icon="📈",
    layout="centered"
)

# ============================================
# FUNDO ROSA
# ============================================

st.markdown(
    """
    <style>

    /* Fundo principal da página */
    .stApp {
        background-color: #F8BBD0;
    }

    /* Cor padrão dos textos */
    .stApp,
    .stApp p,
    .stApp label,
    .stApp span {
        color: #4A0033;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #880E4F !important;
    }

    /* Caixa dos campos numéricos */
    div[data-baseweb="input"] > div {
        background-color: white !important;
        border: 2px solid #EC407A !important;
        border-radius: 10px !important;
    }

    /* Valor digitado */
    div[data-baseweb="input"] input {
        color: black !important;
        background-color: white !important;
    }

    /* Botão */
    .stButton > button {
        background-color: #EC407A;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
    }

    /* Botão quando passa o mouse */
    .stButton > button:hover {
        background-color: #C2185B;
        color: white;
        border: none;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================
# CAMINHO DA PASTA DO PROGRAMA
# ============================================

PASTA_APP = Path(__file__).parent

# ============================================
# CAMINHO DA LOGOMARCA
# ============================================

CAMINHO_LOGO = PASTA_APP / "mat.jpeg"

# ============================================
# LOGOMARCA
# ============================================

if CAMINHO_LOGO.exists():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            str(CAMINHO_LOGO),
            use_container_width=True
        )

else:
    st.warning(
        "⚠️ A imagem mat.jpeg não foi encontrada."
    )

# ============================================
# TÍTULO
# ============================================

st.title("📈 Equação do 1º Grau")

st.write("Equação no formato:")

st.latex(r"ax + b = 0")

# ============================================
# ENTRADA DOS VALORES
# ============================================

a = st.number_input(
    "Digite o valor de a",
    value=1,
    step=1
)

b = st.number_input(
    "Digite o valor de b",
    value=0,
    step=1
)

# ============================================
# BOTÃO CALCULAR
# ============================================

if st.button(
    "🌸 CALCULAR",
    use_container_width=True
):

    # ========================================
    # VERIFICA O VALOR DE A
    # ========================================

    if a == 0:

        if b == 0:

            st.warning(
                "A equação possui infinitas soluções."
            )

        else:

            st.error(
                "A equação não possui solução."
            )

    else:

        # ====================================
        # CALCULA A RAIZ
        # ====================================

        x_raiz = -b / a

        # ====================================
        # RESULTADO
        # ====================================

        st.subheader("✅ Resultado")

        st.write(
            "A raiz da equação é:"
        )

        st.success(
            f"x = {x_raiz:.2f}"
        )

        # ====================================
        # MOSTRA A EQUAÇÃO
        # ====================================

        st.subheader("📝 Equação")

        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        # ====================================
        # MOSTRA O CÁLCULO
        # ====================================

        st.subheader("🧮 Resolução")

        if b >= 0:

            st.latex(
                f"{a}x + {b} = 0"
            )

        else:

            st.latex(
                f"{a}x - {abs(b)} = 0"
            )

        st.latex(
            f"{a}x = {-b}"
        )

        st.latex(
            f"x = \\frac{{{-b}}}{{{a}}}"
        )

        st.latex(
            f"x = {x_raiz:.2f}"
        )

        # ====================================
        # GRÁFICO
        # ====================================

        st.subheader(
            "📊 Gráfico da função"
        )

        # Intervalo do gráfico
        x = np.linspace(
            x_raiz - 10,
            x_raiz + 10,
            500
        )

        # Função
        y = a * x + b

        # Cria o gráfico
        fig, ax = plt.subplots(
            figsize=(8, 5)
        )

        # Desenha a reta
        ax.plot(
            x,
            y,
            linewidth=2,
            label=f"y = {a}x + {b}"
        )

        # Eixo X
        ax.axhline(
            y=0,
            linewidth=1
        )

        # Eixo Y
        ax.axvline(
            x=0,
            linewidth=1
        )

        # Marca a raiz
        ax.scatter(
            [x_raiz],
            [0],
            s=100,
            zorder=5,
            label=f"Raiz: x = {x_raiz:.2f}"
        )

        # ====================================
        # CONFIGURAÇÃO DO GRÁFICO
        # ====================================

        ax.set_xlabel("x")

        ax.set_ylabel("y")

        ax.set_title(
            "Gráfico da Função do 1º Grau"
        )

        ax.grid(True)

        ax.legend()

        # ====================================
        # MOSTRA O GRÁFICO
        # ====================================

        st.pyplot(
            fig,
            use_container_width=True
        )

        plt.close(fig)

# ============================================
# RODAPÉ
# ============================================

st.divider()

st.caption(
    "📚 Calculadora de Equação do 1º Grau"
)
