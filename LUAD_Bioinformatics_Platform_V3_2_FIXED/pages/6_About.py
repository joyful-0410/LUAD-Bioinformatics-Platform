import streamlit as st
from utils import inject_css

st.set_page_config(page_title="About | LUAD Platform", page_icon="👤", layout="wide")
inject_css()

OLD_REPO = "https://github.com/joyful-0410/lung-cancer-prediction1"
OLD_DEMO = "https://lung-cancer-prediction1-i8ah4bbmitplzlry972vlf.streamlit.app/"
NEW_REPO = "https://github.com/joyful-0410/LUAD-Bioinformatics-Platform"
NEW_DEMO = "https://joyful-luad-platform.streamlit.app/"
POSTER_URL = "https://raw.githubusercontent.com/joyful-0410/lung-cancer-prediction1/main/poster.png.png"
CURRENT_HOME_IMAGE = "https://raw.githubusercontent.com/joyful-0410/LUAD-Bioinformatics-Platform/main/image/home.png"

st.title("👤 關於")

col1, col2 = st.columns([1.2, 1], gap="large")
with col1:
    st.subheader("開發者")
    st.markdown("**Kang-Sheng Liu／劉康聖**")
    st.write("長榮大學生物科技學系")
with col2:
    st.subheader("研究興趣")
    st.write("Cancer Bioinformatics")
    st.write("Explainable AI")
    st.write("Machine Learning")
    st.write("Precision Medicine")

st.divider()
st.header("🎯 Project Goal")
st.write("本專案旨在整合肺腺癌基因表達資料、Random Forest、SHAP 可解釋性分析與生物學詮釋，建立一個可公開展示、可互動操作的生物資訊平台。")

g1, g2, g3 = st.columns(3)
with g1:
    st.info("🧬 **Bioinformatics**\n\n基因表達、TCGA-LUAD、基因功能解釋")
with g2:
    st.info("🤖 **Machine Learning**\n\nRandom Forest、分類評估、風險預測")
with g3:
    st.info("🔍 **Explainable AI**\n\nSHAP、基因重要性、結果詮釋")

st.divider()
st.header("📈 Development Timeline")
for number, title, description in [
    ("1", "Original Research Poster", "完成初步資料分析、模型與海報"),
    ("2", "Version 1 Prototype", "建立單頁式 Streamlit 初版網站"),
    ("3", "Review and Correction", "發現海報、模型與網站內容存在不一致"),
    ("4", "Version 2 Platform", "重新整理模型呈現並建立多頁式平台"),
    ("5", "Future Development", "生存分析、藥物反應與 TRBP2 模組"),
]:
    c1, c2 = st.columns([0.12, 0.88])
    with c1:
        st.markdown(f"### {number}")
    with c2:
        st.markdown(f"### {title}")
        st.caption(description)
    if number != "5":
        st.markdown("⬇️")

st.divider()
st.header("🔄 Project Evolution")
tab_v1, tab_v2 = st.tabs(["Version 1 — Initial Prototype", "Version 2 — Current Platform"])

with tab_v1:
    st.warning("此版本為早期原型，保留作為學習與開發歷程紀錄。其中海報、模型流程與網站內容仍有初步假設與不一致，不應視為目前的最終科學結論。")
    left, right = st.columns([1.1, 1], gap="large")
    with left:
        st.subheader("Original Research Poster")
        st.image(POSTER_URL, caption="Version 1 undergraduate research poster", use_container_width=True)
    with right:
        st.subheader("Version 1 Features")
        st.markdown("""
- 初版 Random Forest 預測原型
- 初步基因篩選與 SHAP 解釋
- 單頁式 Streamlit 介面
- 基因表達輸入與風險預測
- 原始研究海報
""")
        st.subheader("Limitations Identified Later")
        st.markdown("""
- 海報與部署網站內容未完全一致
- 模型輸入與效能數字需要重新檢查
- 生物學解釋仍較初步
- 分析流程與版本資訊不夠清楚
- 網站缺少獨立功能模組
""")
        st.link_button("🌐 Open Version 1 Website", OLD_DEMO, use_container_width=True)
        st.link_button("📂 Open Version 1 GitHub", OLD_REPO, use_container_width=True)

with tab_v2:
    st.success("Version 2 是目前正式作品集版本，是在重新檢查 Version 1 的限制後完成的多頁式平台。")
    left, right = st.columns([1.1, 1], gap="large")
    with left:
        st.subheader("Current Platform")
        st.image(CURRENT_HOME_IMAGE, caption="Version 2 Lung Cancer Bioinformatics Platform", use_container_width=True)
    with right:
        st.subheader("Version 2 Features")
        st.markdown("""
- 多頁式 Streamlit 架構
- 10 基因互動式預測
- Model Performance 頁面
- SHAP Analysis 頁面
- Gene Explorer
- Dataset Workflow
- 完整 GitHub README 與截圖
- 公開 Streamlit 網站
""")
        st.subheader("Major Improvements")
        st.markdown("""
- 重新檢查海報與網站不一致之處
- 整理基因面板與模型呈現方式
- 將預測、效能與解釋分成獨立模組
- 擴充生物學功能與基因說明
- 改善介面設計與文件
- 清楚區分研究展示與臨床用途
""")
        st.link_button("🌐 Open Current Platform", NEW_DEMO, use_container_width=True)
        st.link_button("📂 Open Current GitHub", NEW_REPO, use_container_width=True)

st.divider()
st.header("📊 Version Comparison")
st.dataframe({
    "Category": ["Interface", "Model presentation", "Explainability", "Biological interpretation", "Documentation", "Deployment", "Project status"],
    "Version 1": ["Single-page prototype", "Basic prediction output", "Preliminary SHAP ranking", "Short gene descriptions", "Basic README and poster", "Early Streamlit website", "Historical prototype"],
    "Version 2": ["Multi-page platform", "Dedicated performance module", "Dedicated SHAP analysis page", "Gene Explorer", "Complete README and screenshots", "Current public Streamlit platform", "Current portfolio version"],
}, use_container_width=True, hide_index=True)

st.divider()
st.header("🛠 Skills Demonstrated")
s1, s2, s3 = st.columns(3)
with s1:
    st.subheader("Bioinformatics")
    st.markdown("- Gene-expression analysis\n- TCGA-LUAD data\n- Gene-function interpretation\n- Cancer biology")
with s2:
    st.subheader("Machine Learning")
    st.markdown("- Random Forest\n- Classification metrics\n- Model evaluation\n- SHAP explainability")
with s3:
    st.subheader("Software Development")
    st.markdown("- Python\n- Streamlit\n- GitHub\n- Public deployment")

st.divider()
st.header("🚀 Future Work")
st.markdown("- Survival analysis\n- External dataset validation\n- Drug-response prediction\n- Multi-cancer analysis\n- Deep-learning models\n- TRBP2 and RNA-binding protein modules\n- Improved biological and clinical interpretation")

st.divider()
st.info("This platform is intended for research, education and portfolio demonstration only. It is not intended for clinical diagnosis, treatment selection or medical decision making.")
