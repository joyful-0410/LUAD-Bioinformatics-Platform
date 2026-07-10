from pathlib import Path
import json
import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
FEATURES = ["SLC34A2","MUC16","ANLN","CDC20","KIF20A","TOP2A","MKI67","BIRC5","TYMS","CCNA2"]
DEFAULTS = {"SLC34A2":9.0,"MUC16":8.0,"ANLN":6.0,"CDC20":6.0,"KIF20A":5.5,"TOP2A":6.5,"MKI67":6.0,"BIRC5":5.5,"TYMS":6.0,"CCNA2":5.8}
POSTER_SHAP = {"SLC34A2":1.248,"MUC16":1.102,"ANLN":0.997,"CDC20":0.921,"KIF20A":0.864,"TOP2A":0.847,"MKI67":0.812,"BIRC5":0.761,"TYMS":0.703,"CCNA2":0.689}
GENE_INFO = {
    "SLC34A2": {"name":"Solute Carrier Family 34 Member 2", "role":"肺泡上皮分化與磷酸鹽轉運相關基因。", "cancer":"常被視為肺泡上皮來源與分化狀態相關標誌。", "interpretation":"表現改變可能反映腫瘤分化狀態與 LUAD 分子特徵。"},
    "MUC16": {"name":"Mucin 16 / CA125", "role":"大型膜結合黏蛋白，與黏附、腫瘤微環境與免疫逃脫相關。", "cancer":"CA125 常見於腫瘤標誌研究，也和癌症進展相關。", "interpretation":"高表現可能暗示腫瘤細胞黏附、浸潤與免疫逃脫特徵。"},
    "ANLN": {"name":"Anillin Actin Binding Protein", "role":"參與細胞骨架組織與細胞分裂。", "cancer":"在多種癌症中與腫瘤增殖、侵襲和預後相關。", "interpretation":"表現升高通常代表細胞分裂活性較強。"},
    "CDC20": {"name":"Cell Division Cycle 20", "role":"細胞週期與有絲分裂調控蛋白。", "cancer":"CDC20 上升常與細胞週期失控、腫瘤增殖有關。", "interpretation":"高表現可能代表腫瘤細胞處於高分裂狀態。"},
    "KIF20A": {"name":"Kinesin Family Member 20A", "role":"Kinesin 馬達蛋白，參與細胞分裂與胞內運輸。", "cancer":"與有絲分裂、增殖與不良預後相關。", "interpretation":"高表現常被解讀為腫瘤細胞分裂活性增加。"},
    "TOP2A": {"name":"DNA Topoisomerase II Alpha", "role":"參與 DNA 複製、拓撲結構調節與染色體分離。", "cancer":"常見增殖相關基因，也與部分抗癌藥物反應相關。", "interpretation":"高表現代表 DNA 複製與細胞增殖活性高。"},
    "MKI67": {"name":"Marker of Proliferation Ki-67", "role":"經典細胞增殖標記。", "cancer":"常用於評估腫瘤增殖程度。", "interpretation":"表現越高通常代表增殖活性越強。"},
    "BIRC5": {"name":"Baculoviral IAP Repeat Containing 5 / Survivin", "role":"抑制細胞凋亡並協助細胞分裂。", "cancer":"與抗凋亡、治療抗性與腫瘤進展相關。", "interpretation":"高表現可能代表癌細胞存活能力提高。"},
    "TYMS": {"name":"Thymidylate Synthase", "role":"參與 DNA 合成所需的胸苷酸合成。", "cancer":"與 DNA 複製、細胞增殖及部分化療藥物反應相關。", "interpretation":"高表現代表 DNA 合成需求增加。"},
    "CCNA2": {"name":"Cyclin A2", "role":"調控 S 期與 G2/M 細胞週期進程。", "cancer":"細胞週期調控異常是癌症核心特徵之一。", "interpretation":"高表現通常代表細胞週期推進與增殖活性增加。"},
}

@st.cache_resource
def load_model():
    return joblib.load(ROOT / "model.pkl"), joblib.load(ROOT / "scaler.pkl")

@st.cache_data
def load_data():
    p = ROOT / "data" / "training_data_10genes.csv"
    if p.exists():
        return pd.read_csv(p)
    return pd.read_csv(ROOT / "data" / "dataset.csv")

@st.cache_data
def load_metrics():
    p = ROOT / "metrics.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}

def inject_css():
    st.markdown('''
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 2rem; max-width: 1220px;}
    .hero {padding: 2rem; border-radius: 28px; background: linear-gradient(135deg,#08203e 0%,#0b4f6c 55%,#00a6a6 100%); color: white; box-shadow: 0 12px 30px rgba(0,0,0,.12); margin-bottom: 1.2rem;}
    .hero h1 {font-size: 3.05rem; line-height: 1.08; margin-bottom: .6rem; font-weight: 900;}
    .hero p {font-size: 1.2rem; opacity: .95;}
    .card {
    padding:1.2rem;
    border-radius:20px;
    border:1px solid #dce8ef;
    background:linear-gradient(180deg,#ffffff,#f7fbfd);
    box-shadow:0 8px 20px rgba(8,32,62,.06);
    height:100%;
    color:#1f2937 !important;
}

.card h1,
.card h2,
.card h3,
.card h4,
.card h5,
.card p,
.card span,
.card div,
.card li,
.card b,
.card strong {
    color:#1f2937 !important;
}

.card h3 {
    margin-top:0;
    color:#12355b !important;
}
    .muted {color:#60717d; font-size:.95rem;}
    .gene-pill {display:inline-block; padding:7px 12px; border-radius:999px; background:#e7f5ff; border:1px solid #b6e0fe; color:#075985; font-weight:700; margin:4px;}
    .risk-high {padding:1.1rem; border-radius:18px; background:#fff0f0; border:1px solid #ffb4b4; color:#8a1f1f; font-size:1.2rem; font-weight:800;}
    .risk-low {padding:1.1rem; border-radius:18px; background:#ecfff3; border:1px solid #b7efc5; color:#176b35; font-size:1.2rem; font-weight:800;}
    .note {
    padding:1rem;
    border-radius:16px;
    background:#f0f7ff;
    border-left:6px solid #1d75bd;
    color:#1f2937 !important;
}

.note * {
    color:#1f2937 !important;
}
    </style>
    ''', unsafe_allow_html=True)
