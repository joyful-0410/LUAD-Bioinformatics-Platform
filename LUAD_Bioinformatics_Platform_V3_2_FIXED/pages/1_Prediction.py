import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import FEATURES, DEFAULTS, POSTER_SHAP, GENE_INFO, load_model, inject_css

st.set_page_config(page_title="Prediction | LUAD Platform", page_icon="🤖", layout="wide")
inject_css()
st.title("🤖 10-Gene LUAD Risk Prediction")
st.caption("輸入 10 個 SHAP 重要基因的表達量，使用 Random Forest 模型預測高/低風險。")

model, scaler = load_model()

with st.sidebar:
    st.header("Gene Expression Input")
    st.caption("建議先用預設值測試，再調整基因表達量。")
    values = {}
    for g in FEATURES:
        values[g] = st.number_input(g, min_value=0.0, max_value=25.0, value=float(DEFAULTS[g]), step=0.1)
    run = st.button("Predict Risk", type="primary", use_container_width=True)

df = pd.DataFrame([values], columns=FEATURES)

m1,m2,m3 = st.columns(3)
m1.metric("Dataset", "TCGA-LUAD")
m2.metric("Input genes", "10")
m3.metric("Algorithm", "Random Forest")

st.subheader("Input data")
st.dataframe(df, use_container_width=True, hide_index=True)

if run:
    scaled = scaler.transform(df)
    pred = int(model.predict(scaled)[0])
    proba = model.predict_proba(scaled)[0]
    high_prob = float(proba[1])
    low_prob = float(proba[0])
    label = "High Risk" if pred == 1 else "Low Risk"

    st.divider()
    left, right = st.columns([1,1])
    with left:
        st.subheader("Prediction result")
        if pred == 1:
            st.markdown(f'<div class="risk-high">⚠️ {label}<br>High-risk probability：{high_prob*100:.2f}%</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="risk-low">✅ {label}<br>Low-risk probability：{low_prob*100:.2f}%</div>', unsafe_allow_html=True)
        st.progress(high_prob, text=f"High-risk probability：{high_prob*100:.2f}%")
    with right:
        st.subheader("Risk gauge")
        fig, ax = plt.subplots(figsize=(7,1.8))
        ax.barh(["Risk"], [high_prob*100])
        ax.set_xlim(0,100)
        ax.set_xlabel("High-risk probability (%)")
        ax.set_title("Predicted risk score")
        st.pyplot(fig, clear_figure=True)

    st.subheader("AI interpretation")
    input_series = pd.Series(values)
    default_series = pd.Series(DEFAULTS)
    delta = (input_series - default_series).abs().sort_values(ascending=False).head(3)
    st.markdown('<div class="note">以下解釋是根據輸入值相對預設值變化最大的 3 個基因產生，用於研究展示與口頭報告，不是臨床診斷。</div>', unsafe_allow_html=True)
    for i, g in enumerate(delta.index, start=1):
        direction = "higher" if values[g] > DEFAULTS[g] else "lower"
        st.markdown(f"**{i}. {g}**：目前輸入值比預設值 **{direction}**。{GENE_INFO[g]['interpretation']}")

st.divider()
st.subheader("10-gene panel table")
rank_df = pd.DataFrame({
    "Rank": range(1, len(FEATURES)+1),
    "Gene": FEATURES,
    "Poster mean SHAP value": [POSTER_SHAP[g] for g in FEATURES],
    "Biological meaning": [GENE_INFO[g]["role"] for g in FEATURES]
})
st.dataframe(rank_df, use_container_width=True, hide_index=True)
