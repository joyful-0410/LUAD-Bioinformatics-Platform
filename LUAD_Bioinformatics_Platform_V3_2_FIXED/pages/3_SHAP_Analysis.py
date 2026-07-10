import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import FEATURES, POSTER_SHAP, load_metrics, inject_css

st.set_page_config(page_title="SHAP Analysis | LUAD Platform", page_icon="🧬", layout="wide")
inject_css()
st.title("🧬 SHAP Analysis")
st.caption("以海報中的 Top 10 SHAP genes 作為網站輸入基因 panel。")

metrics = load_metrics()
model_imp = metrics.get("model_feature_importance", {})
rank_df = pd.DataFrame({
    "Rank": range(1, len(FEATURES)+1),
    "Gene": FEATURES,
    "Poster mean SHAP value": [POSTER_SHAP[g] for g in FEATURES],
    "Current RF importance": [model_imp.get(g, 0) for g in FEATURES]
})

left, right = st.columns(2)
with left:
    st.subheader("Poster SHAP ranking")
    tmp = rank_df.sort_values("Poster mean SHAP value", ascending=True)
    fig, ax = plt.subplots(figsize=(6.5,5))
    ax.barh(tmp["Gene"], tmp["Poster mean SHAP value"])
    ax.set_xlabel("Mean SHAP value")
    ax.set_title("Top 10 SHAP-selected genes")
    st.pyplot(fig, clear_figure=True)
with right:
    st.subheader("Current model importance")
    tmp = rank_df.sort_values("Current RF importance", ascending=True)
    fig, ax = plt.subplots(figsize=(6.5,5))
    ax.barh(tmp["Gene"], tmp["Current RF importance"])
    ax.set_xlabel("Random Forest feature importance")
    ax.set_title("Importance in current 10-gene model")
    st.pyplot(fig, clear_figure=True)

st.subheader("Ranking table")
st.dataframe(rank_df, use_container_width=True, hide_index=True)

st.markdown('''

SHAP is a model interpretation method. It estimates how much each feature contributes to the model output. In this project, the website uses the Top 10 SHAP-important genes from the previous analysis as the final interactive input panel. This makes the system easier to explain than an all-gene black-box model.
''')
