import streamlit as st
from utils import FEATURES, POSTER_SHAP, inject_css, load_metrics

st.set_page_config(page_title="Lung Cancer Bioinformatics Platform", page_icon="🫁", layout="wide")
inject_css()
metrics = load_metrics()

st.markdown('''
<div class="hero">
  <h1>🫁 Lung Cancer Bioinformatics Platform</h1>
  <p>Machine Learning × SHAP × TCGA-LUAD × Precision Medicine</p>
  <p>整合 TCGA-LUAD 基因表達資料、Random Forest 機器學習與 SHAP 可解釋 AI 的肺腺癌生物資訊互動平台。</p>
</div>
''', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
c1.metric("Dataset", metrics.get("dataset", "TCGA-LUAD"))
c2.metric("Samples", metrics.get("samples", 515))
c3.metric("Input genes", "10")
c4.metric("Model", "Random Forest")

st.divider()

left, right = st.columns([1.2, 1])
with left:
    st.subheader("Project overview")
    st.markdown('''
    <div class="card">
    <h3>研究目的</h3>
    <p>本平台以肺腺癌（LUAD）為主題，將基因表達資料轉換成可互動的 AI 預測系統。核心概念是：先利用機器學習模型建立高/低風險分類，再以 SHAP 與基因功能解釋模型判斷依據。</p>
    <p>這個版本固定使用海報中的 <b>Top 10 SHAP important genes</b> 作為輸入基因，讓海報、簡報、GitHub 和網站更一致。</p>
    </div>
    ''', unsafe_allow_html=True)
with right:
    st.subheader("Platform modules")
    st.markdown('''
    <div class="card">
    <b>🤖 Prediction</b><br>10 基因互動式風險預測<br><br>
    <b>📊 Model Performance</b><br>ROC、AUC、Confusion Matrix<br><br>
    <b>🧬 SHAP Analysis</b><br>重要基因排序與可解釋性<br><br>
    <b>🔬 Gene Explorer</b><br>基因功能與癌症關聯
    </div>
    ''', unsafe_allow_html=True)

st.subheader("10-gene SHAP panel")
st.markdown("".join([f'<span class="gene-pill">{g} · {POSTER_SHAP[g]:.3f}</span>' for g in FEATURES]), unsafe_allow_html=True)

st.subheader("Workflow")
w1,w2,w3,w4,w5 = st.columns(5)
for col, title, body in zip([w1,w2,w3,w4,w5], ["1. TCGA-LUAD", "2. Preprocessing", "3. Random Forest", "4. SHAP", "5. Web Platform"], ["RNA-seq gene expression", "10-gene feature panel", "High/low risk classifier", "Feature interpretation", "Streamlit deployment"]):
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><p class="muted">{body}</p></div>', unsafe_allow_html=True)

st.info("請從左側 pages 選單進入 Prediction、Model Performance、SHAP Analysis、Gene Explorer、Dataset & Workflow、About。")
