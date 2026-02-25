import streamlit as st

st.set_page_config(page_title="Plan Maestro - DEMO", layout="centered")

st.markdown("# 📊 PLAN MAESTRO DE VIDA")
st.markdown("**Versión DEMO - Muestra gratuita**")
st.divider()

st.subheader("📋 Datos de ejemplo (fijos)")
st.markdown("**Capital inicial:** $360,000")
st.markdown("**Tasa de interés:** 10% anual")
st.markdown("**Ahorro IMSS:** $3,500/mes")
st.markdown("**Incremento anual:** 5%")
st.divider()

st.markdown("## 🔒 VERSIÓN COMPLETA")
st.markdown("✅ Tus datos reales")
st.markdown("✅ 5 retiros especiales configurables")
st.markdown("✅ Aguinaldo prorrateado o reinvertido")
st.markdown("✅ Gráficas interactivas")
st.markdown("✅ Asesoría personal 3 meses")
st.markdown("")
st.markdown("### **$2,500 MXN**")

whatsapp_link = "https://wa.me/5218715791810?text=Quiero%20el%20Plan%20Maestro"
st.markdown(f'<a href="{whatsapp_link}" target="_blank"><button style="background-color:#25D366; color:white; padding:15px; width:100%; border:none; border-radius:5px; font-size:18px; font-weight:bold">📲 CONTACTAR POR WHATSAPP</button></a>', unsafe_allow_html=True)

st.divider()
st.caption("© Ing. Roberto Villarreal")
