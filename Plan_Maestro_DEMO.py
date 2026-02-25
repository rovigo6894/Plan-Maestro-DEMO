import streamlit as st

st.set_page_config(page_title="Plan Maestro - DEMO", layout="centered")

# Ocultar menús
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título
st.markdown("# 📊 PLAN MAESTRO DE VIDA")
st.markdown("**Versión DEMO - Muestra gratuita**")
st.caption("Descubre lo que la versión completa puede hacer por ti")
st.divider()

# ============================================
# DATOS DE EJEMPLO
# ============================================

st.subheader("📋 Ejemplo de resultados (con datos fijos)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Capital inicial**")
    st.markdown("# $360,000")
    st.markdown("**Ahorro IMSS inicial**")
    st.markdown("# $3,500/mes")
with col2:
    st.markdown("**Tasa de interés**")
    st.markdown("# 10% anual")
    st.markdown("**Incremento anual**")
    st.markdown("# 5%")

st.divider()

# ============================================
# LO QUE LA VERSIÓN COMPLETA OFRECE
# ============================================

st.markdown("## 🔍 EN LA VERSIÓN COMPLETA PODRÁS:")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    #### 📈 Proyección año por año
    ```
    2028: $360,000  → $12,500/mes
    2029: $378,000  → $13,100/mes
    2030: $397,000  → $13,700/mes
    2034: $483,000  → $16,500/mes
    2038: $613,000  → $12,700/mes
    2049: $948,000  → $18,700/mes
    ```
    """)

with col_b:
    st.markdown("""
    #### 🎯 Retiros especiales configurables
    - **Retiro 1:** 2029 → $190,000
    - **Retiro 2:** 2034 → $50,000  
    - **Retiro 3, 4 y 5:** Tú eliges año y monto
    """)

st.divider()

# ============================================
# GRÁFICA ILUSTRATIVA
# ============================================

st.markdown("#### 📊 Evolución de tu capital (ejemplo)")

años = [2028, 2032, 2036, 2040, 2044, 2049]
capital = [360, 440, 540, 670, 820, 950]

grafica = ""
for i in range(len(años)):
    barra = "█" * int(capital[i] / 30)
    grafica += f"{años[i]}: {barra} ${capital[i]}k\n"

st.markdown(f"```\n{grafica}\n```")
st.caption("Gráfica ilustrativa - En la versión completa verás gráficas interactivas reales")

st.divider()

# ============================================
# BENEFICIOS DETALLADOS
# ============================================

st.markdown("## 🎁 LA VERSIÓN COMPLETA INCLUYE:")

beneficios = [
    "✅ Tus datos reales (no ejemplos fijos)",
    "✅ Proyección año por año 2028–2049",
    "✅ 5 retiros especiales configurables (año y monto)",
    "✅ Aguinaldo: elige si prorratearlo o reinvertirlo",
    "✅ Pensión Bienestar bimestral prorrateada a mensual",
    "✅ Gráficas interactivas profesionales",
    "✅ Resumen ejecutivo al 2049",
    "✅ Asesoría personalizada por 3 meses vía WhatsApp",
    "✅ Actualizaciones gratuitas de por vida"
]

for b in beneficios:
    st.markdown(b)

st.markdown("")
st.markdown("### **$2,500 MXN**")
st.markdown("")  # Línea vacía, sin "Pago único"

# ============================================
# TESTIMONIO
# ============================================

st.divider()
st.markdown("### 💬 Lo que dicen nuestros primeros usuarios:")
st.markdown("""
> *"Con el Plan Maestro pude visualizar mis retiros y ajustar mis metas.  
> La asesoría de Roberto fue clave para entender cuánto necesito realmente."*  
> — **Carlos R., Asesor Financiero**
""")

st.divider()

# ============================================
# BOTÓN WHATSAPP
# ============================================

st.markdown("### 📲 ¿Listo para tu plan personalizado?")
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

# Métodos de pago
with st.expander("💳 Métodos de pago aceptados"):
    st.markdown("""
    - **Transferencia bancaria** (CLABE: 646010157104792686)
    - **OXXO** (generamos código al confirmar)
    - **MercadoPago** (próximamente)
    """)

st.divider()
st.caption("© Ing. Roberto Villarreal · Plan Maestro DEMO · Versión completa: $2,500")
