import streamlit as st
from utils import FEATURES, GENE_INFO, POSTER_SHAP, inject_css

st.set_page_config(page_title="Gene Explorer | LUAD Platform", page_icon="🔬", layout="wide")
inject_css()
st.title("🔬 Gene Explorer")
st.caption("查詢 Top 10 gene panel 的功能、癌症意義與報告時可用的解釋。")

gene = st.selectbox("Select a gene", FEATURES)
info = GENE_INFO[gene]

c1,c2,c3 = st.columns(3)
c1.metric("Gene", gene)
c2.metric("Poster SHAP", f"{POSTER_SHAP[gene]:.3f}")
c3.metric("Panel", "Top 10")

st.markdown(f'''
<div class="card">
<h3>{info['name']}</h3>
<b>Function</b><br>{info['role']}<br><br>
<b>Cancer relevance</b><br>{info['cancer']}<br><br>
<b>Interpretation in this platform</b><br>{info['interpretation']}
</div>
''', unsafe_allow_html=True)

st.subheader("External resources")
st.markdown(f"- GeneCards： https://www.genecards.org/Search/Keyword?queryString={gene}")
st.markdown(f"- NCBI Gene： https://www.ncbi.nlm.nih.gov/gene/?term={gene}")
st.markdown(f"- PubMed： https://pubmed.ncbi.nlm.nih.gov/?term={gene}+lung+adenocarcinoma")
