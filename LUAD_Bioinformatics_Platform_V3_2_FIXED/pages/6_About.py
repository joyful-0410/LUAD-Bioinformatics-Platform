import streamlit as st
from utils import inject_css

st.set_page_config(page_title="About | LUAD Platform", page_icon="👤", layout="wide")
inject_css()
st.title("👤 About")

st.markdown('''
<div class="card">
<h3>Developer</h3>
<b>Kang-Sheng Liu / 劉康聖</b><br>
Department of Biotechnology, Chang Jung Christian University<br><br>
<h3>Project title</h3>
Lung Cancer Bioinformatics Platform<br>
Machine Learning × SHAP × TCGA-LUAD<br><br>
<h3>Portfolio positioning</h3>
This platform demonstrates machine learning implementation, biological interpretation, Streamlit deployment, and bioinformatics project organization. It can be shown together with the TARBP2 Cancer Bioinformatics Platform as a bioinformatics portfolio.
</div>
''', unsafe_allow_html=True)

