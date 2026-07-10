import streamlit as st
from utils import FEATURES, load_data, inject_css

st.set_page_config(page_title="Dataset & Workflow | LUAD Platform", page_icon="📚", layout="wide")
inject_css()
st.title("📚 Dataset & Workflow")

df = load_data()
c1,c2,c3,c4 = st.columns(4)
c1.metric("Samples", len(df))
c2.metric("Input genes", len(FEATURES))
c3.metric("Target", "High / Low risk")
c4.metric("Platform", "Streamlit")

st.subheader("Dataset preview")
st.dataframe(df.head(20), use_container_width=True)

st.subheader("Workflow")
st.markdown('''
<div class="card">
<b>1. Data source</b>：TCGA-LUAD gene expression and survival-related information.<br><br>
<b>2. Label definition</b>：samples are labeled as high-risk or low-risk groups.<br><br>
<b>3. Feature panel</b>：10 genes selected from previous SHAP feature importance analysis.<br><br>
<b>4. Model</b>：Random Forest classifier for interactive prediction.<br><br>
<b>5. Interpretation</b>：SHAP ranking, model importance, and gene function explanation.<br><br>
<b>6. Deployment</b>：Streamlit web platform for presentation and portfolio use.
</div>
''', unsafe_allow_html=True)

st.subheader("10 input features")
st.write(", ".join(FEATURES))
st.warning("This platform is for education and research presentation. It is not a clinical diagnostic tool.")
