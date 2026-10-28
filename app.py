import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Sistema Experto Dermatológico", page_icon="🩺")

st.title("🩺 Sistema Experto: Diagnóstico Dermatológico")
st.markdown("""
Bienvenido. Este es un sistema experto basado en reglas diseñado para dar un **diagnóstico preliminar** de afecciones cutáneas comunes.
*Por favor, responda las siguientes preguntas sobre los síntomas del paciente.*
""")

# Advertencia ética (Muy importante para un sistema de salud)
st.warning("⚠️ **Aviso:** Este sistema es un ejercicio académico y no sustituye el diagnóstico de un médico profesional. Si los síntomas son graves, acuda a un especialista.")

st.divider()

# 2. Interfaz de Usuario (Entrada de datos)
st.subheader("Síntomas del Paciente")

col1, col2 = st.columns(2)

with col1:
    espinillas = st.radio("¿Presenta espinillas o puntos negros?", ["Sí", "No"])
    picazon = st.radio("¿Presenta picazón intensa?", ["Sí", "No"])
    enrojecimiento = st.radio("¿Hay enrojecimiento o inflamación en la zona?", ["Sí", "No"])

with col2:
    ronchas = st.radio("¿Tiene ronchas elevadas (habones)?", ["Sí", "No"])
    escamas = st.radio("¿Tiene descamación o escamas plateadas?", ["Sí", "No"])
    piel_seca = st.radio("¿La piel se siente extremadamente seca?", ["Sí", "No"])

st.divider()

# 3. Motor de Inferencia (Reglas IF-THEN)
if st.button("🔍 Generar Diagnóstico Preliminar", type="primary"):
    
    diagnostico = "No determinado"
    recomendacion = ""
    nivel_alerta = "info"

    # Regla 1: Acné
    if espinillas == "Sí" and ronchas == "No" and escamas == "No":
        diagnostico = "Acné"
        recomendacion = "Mantener una rutina de limpieza facial suave. Evitar manipular las lesiones. Consultar a un dermatólogo para tratamiento tópico."
        nivel_alerta = "success"
    
    # Regla 2: Urticaria
    elif ronchas == "Sí" and picazon == "Sí":
        diagnostico = "Urticaria"
        recomendacion = "Evitar rascarse. Se pueden usar antihistamínicos de venta libre. Si hay dificultad para respirar o hinchazón en el rostro, acudir a urgencias inmediatamente."
        nivel_alerta = "warning"
    
    # Regla 3: Psoriasis
    elif escamas == "Sí" and enrojecimiento == "Sí":
        diagnostico = "Psoriasis"
        recomendacion = "Requiere evaluación médica. Se recomiendan cremas hidratantes espesas y exposición moderada al sol. Evitar el estrés."
        nivel_alerta = "error"
        
    # Regla 4: Dermatitis
    elif picazon == "Sí" and piel_seca == "Sí" and ronchas == "No":
        diagnostico = "Dermatitis Atópica o Eccema"
        recomendacion = "Aplicar cremas hidratantes sin fragancia. Evitar jabones fuertes y alérgenos conocidos."
        nivel_alerta = "success"

    # 4. Mostrar Resultados (Salida)
    st.subheader("Resultado del Análisis")
    
    if diagnostico != "No determinado":
        if nivel_alerta == "success":
            st.success(f"**Diagnóstico Preliminar:** {diagnostico}")
        elif nivel_alerta == "warning":
            st.warning(f"**Diagnóstico Preliminar:** {diagnostico}")
        elif nivel_alerta == "error":
            st.error(f"**Diagnóstico Preliminar:** {diagnostico}")
            
        st.info(f"**Recomendación:** {recomendacion}")
    else:
        st.error("**No se pudo determinar un diagnóstico.** La combinación de síntomas no coincide con nuestra base de conocimiento. Por favor, consulte a un médico.")