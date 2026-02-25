import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Plan Maestro - DEMO", layout="centered")

# Ocultar menús de Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("# 📊 PLAN MAESTRO DE VIDA")
st.markdown("**Versión DEMO - Muestra gratuita**")
st.caption("Proyección 2028–2049 (datos de ejemplo)")
st.divider()

st.subheader("📋 Parámetros de ejemplo (fijos)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Capital inicial**")
    st.markdown("# $360,000")
    st.markdown("")
    st.markdown("**Ahorro IMSS inicial**")
    st.markdown("# $3,500/mes")
with col2:
    st.markdown("**Tasa de interés**")
    st.markdown("# 10% anual")
    st.markdown("")
    st.markdown("**Incremento anual**")
    st.markdown("# 5%")

st.divider()

años = list(range(2028, 2050))
capital_ejemplo = [360000, 378000, 397000, 417000, 438000, 
                   460000, 483000, 507000, 532000, 558000,
                   585000, 613000, 642000, 672000, 703000,
                   735000, 768000, 802000, 837000, 873000,
                   910000, 948000]
total_mensual = [12500, 13100, 13700, 14300, 14900,
                 15500, 16500, 17100, 17700, 18300,
                 12100, 12700, 13300, 13900, 14500,
                 15100, 15700, 16300, 16900, 17500,
                 18100, 18700]

df_ejemplo = pd.DataFrame({
    "Año": años,
    "Capital ($)": capital_ejemplo,
    "Total Mensual ($)": total_mensual
})

st.subheader("📋 Proyección 2028–2049 (ejemplo)")
st.dataframe(df_ejemplo, use_container_width=True, hide_index=True)
st.divider()

st.subheader("📈 Evolución del Capital (ejemplo)")
fig = px.line(df_ejemplo, x="Año", y="Capital ($)", markers=True)
fig.update_traces(line_color="#0066b3", line_width=3)
fig.update_layout(yaxis_tickformat="$,.0f", height=400)
st.plotly_chart(fig, use_container_width=True)
st.divider()

st.markdown("## 🔒 VERSIÓN COMPLETA")
st.markdown("✅ Tus datos reales")
st.markdown("✅ 5 retiros especiales configurables")
st.markdown("✅ Aguinaldo prorrateado o reinvertido")
st.markdown("✅ Pensión Bienestar bimestral")
st.markdown("✅ Gráficas interactivas")
st.markdown("✅ Resumen al 2049")
st.markdown("✅ Asesoría personal 3 meses")
st.markdown("")
st.markdown("### **$2,500 MXN**")
st.markdown("Pago único · Sin instalaciones")

st.markdown("### 📲 ¿Interesado?")
whatsapp_link = "https://wa.me/5218715791810?text=Quiero%20la%20versi%C3%B3n%20completa%20del%20Plan%20Maestro"
st.markdown(f"""
<div style='text-align: center'>
    <a href='{whatsapp_link}' target='_blank'>
        <button style='background-color: #25D366; color: white; padding: 15px 30px; 
                border: none; border-radius: 5px; font-size: 20px; font-weight: bold;
                cursor: pointer; margin-bottom: 20px; width: 100%;'>
            📲 CONTACTAR POR WHATSAPP
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

with st.expander("💳 Métodos de pago aceptados"):
    st.markdown("""
    - **Transferencia bancaria** (CLABE se proporciona al contactar)
    - **OXXO** (generamos código al confirmar)
    """)

st.divider()
st.caption("© Ing. Roberto Villarreal · Plan Maestro DEMO · Versión completa: $2,500")