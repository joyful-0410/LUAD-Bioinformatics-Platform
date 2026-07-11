import streamlit as st
from utils import inject_css

st.set_page_config(
    page_title="About | LUAD Platform",
    page_icon="👤",
    layout="wide"
)

inject_css()

# =========================
# Links
# =========================
OLD_REPO = "https://github.com/joyful-0410/lung-cancer-prediction1"
OLD_DEMO = "https://lung-cancer-prediction1-i8ah4bbmitplzlry972vlf.streamlit.app/"

NEW_REPO = "https://github.com/joyful-0410/LUAD-Bioinformatics-Platform"
NEW_DEMO = "https://joyful-luad-platform.streamlit.app/"

POSTER_URL = (
    "https://raw.githubusercontent.com/"
    "joyful-0410/lung-cancer-prediction1/main/poster.png.png"
)

CURRENT_HOME_IMAGE = (
    "https://raw.githubusercontent.com/"
    "joyful-0410/LUAD-Bioinformatics-Platform/main/image/home.png"
)

# =========================
# Page title
# =========================
st.title("👤 About")

st.markdown(
    """
    <div class="card">
        <h3>Developer</h3>
        <b>Kang-Sheng Liu / 劉康聖</b><br>
        Department of Biotechnology<br>
        Chang Jung Christian University<br><br>

        <h3>Research interests</h3>
        Cancer Bioinformatics · Explainable AI · Machine Learning · Precision Medicine<br><br>

        <h3>Project title</h3>
        Lung Cancer Bioinformatics Platform<br>
        Machine Learning × SHAP × TCGA-LUAD
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# Project goal
# =========================
st.divider()
st.header("🎯 Project Goal")

st.markdown(
    """
    This project aims to integrate:

    - Gene expression analysis
    - Random Forest machine learning
    - SHAP model explainability
    - Biological interpretation
    - Interactive web deployment

    into a single lung adenocarcinoma bioinformatics platform.

    The platform was developed as an undergraduate bioinformatics portfolio project
    and documents the complete process from an early prototype to a redesigned
    multi-page analysis system.
    """
)

# =========================
# Timeline
# =========================
st.divider()
st.header("📈 Development Timeline")

st.markdown(
    """
    <div class="card" style="text-align:center;">
        <h3>Original Research Poster</h3>
        <p>Early machine-learning analysis and preliminary biological interpretation</p>

        <h2>↓</h2>

        <h3>Version 1 — Prototype Website</h3>
        <p>Single-page Streamlit prediction system</p>

        <h2>↓</h2>

        <h3>Model and Workflow Review</h3>
        <p>Identification of inconsistencies between the poster, model and website</p>

        <h2>↓</h2>

        <h3>Version 2 — Current Platform</h3>
        <p>Multi-page bioinformatics platform with SHAP, Gene Explorer and Dataset Workflow</p>

        <h2>↓</h2>

        <h3>Future Development</h3>
        <p>Survival analysis, drug response, TRBP2 and multi-cancer modules</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# Project evolution tabs
# =========================
st.divider()
st.header("🔄 Project Evolution")

tab_v1, tab_v2 = st.tabs(
    [
        "Version 1 — Initial Prototype",
        "Version 2 — Current Platform"
    ]
)

# -------------------------
# Version 1
# -------------------------
with tab_v1:
    st.warning(
        "Version 1 is preserved as an early development record. "
        "The poster, model workflow and website contained preliminary assumptions "
        "and inconsistencies. It should not be interpreted as the current scientific "
        "conclusion of the project."
    )

    col1, col2 = st.columns([1.15, 1], gap="large")

    with col1:
        st.subheader("Original Research Poster")

        st.image(
            POSTER_URL,
            caption="Version 1 undergraduate research poster",
            use_container_width=True
        )

    with col2:
        st.subheader("Version 1 Features")

        st.markdown(
            """
            - Initial Random Forest prediction prototype
            - Early gene selection and SHAP interpretation
            - Single-page Streamlit interface
            - Basic gene-expression input
            - Original undergraduate poster
            - Preliminary performance claims
            """
        )

        st.subheader("Limitations Identified Later")

        st.markdown(
            """
            - Poster and deployed website were not fully consistent
            - Model inputs and reported performance required rechecking
            - Biological interpretation was still preliminary
            - The scientific workflow was not documented clearly
            - The website lacked independent analysis modules
            """
        )

        st.link_button(
            "🌐 Open Version 1 Website",
            OLD_DEMO,
            use_container_width=True
        )

        st.link_button(
            "📂 Open Version 1 GitHub",
            OLD_REPO,
            use_container_width=True
        )

# -------------------------
# Version 2
# -------------------------
with tab_v2:
    st.success(
        "Version 2 is the current portfolio version. "
        "It was redesigned after reviewing the limitations of Version 1."
    )

    col1, col2 = st.columns([1.15, 1], gap="large")

    with col1:
        st.subheader("Current Platform")

        st.image(
            CURRENT_HOME_IMAGE,
            caption="Version 2 Lung Cancer Bioinformatics Platform",
            use_container_width=True
        )

    with col2:
        st.subheader("Version 2 Features")

        st.markdown(
            """
            - Multi-page Streamlit architecture
            - 10-gene interactive prediction module
            - Model Performance page
            - SHAP Analysis page
            - Gene Explorer
            - Dataset Workflow
            - Improved GitHub README
            - Public Streamlit deployment
            """
        )

        st.subheader("Major Improvements")

        st.markdown(
            """
            - Rechecked inconsistencies between the poster and website
            - Reorganized the gene panel and model workflow
            - Separated prediction, performance and explainability modules
            - Expanded biological interpretation
            - Improved interface design and documentation
            - Clearly separated educational demonstration from clinical use
            """
        )

        st.link_button(
            "🌐 Open Current Platform",
            NEW_DEMO,
            use_container_width=True
        )

        st.link_button(
            "📂 Open Current GitHub",
            NEW_REPO,
            use_container_width=True
        )

# =========================
# Comparison table
# =========================
st.divider()
st.header("📊 Version Comparison")

comparison_data = {
    "Category": [
        "Interface",
        "Model presentation",
        "Explainability",
        "Biological interpretation",
        "Documentation",
        "Deployment",
        "Project status"
    ],
    "Version 1": [
        "Single-page prototype",
        "Basic prediction output",
        "Preliminary SHAP ranking",
        "Short gene descriptions",
        "Basic README and poster",
        "Early Streamlit website",
        "Historical prototype"
    ],
    "Version 2": [
        "Multi-page platform",
        "Dedicated performance module",
        "Dedicated SHAP analysis page",
        "Gene Explorer",
        "Complete README and screenshots",
        "Current public Streamlit platform",
        "Current portfolio version"
    ]
}

st.dataframe(
    comparison_data,
    use_container_width=True,
    hide_index=True
)

# =========================
# Skills demonstrated
# =========================
st.divider()
st.header("🛠 Skills Demonstrated")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        ### Bioinformatics
        - Gene-expression analysis
        - TCGA-LUAD data
        - Gene-function interpretation
        - Cancer biology
        """
    )

with col2:
    st.markdown(
        """
        ### Machine Learning
        - Random Forest
        - Classification metrics
        - Model evaluation
        - SHAP explainability
        """
    )

with col3:
    st.markdown(
        """
        ### Software Development
        - Python
        - Streamlit
        - GitHub
        - Public deployment
        """
    )

# =========================
# Future work
# =========================
st.divider()
st.header("🚀 Future Work")

st.markdown(
    """
    Planned future directions include:

    - Survival analysis
    - External dataset validation
    - Drug-response prediction
    - Multi-cancer analysis
    - Deep-learning models
    - TRBP2 and RNA-binding protein modules
    - Improved biological and clinical interpretation
    """
)

# =========================
# Final note
# =========================
st.divider()

st.info(
    "This platform is intended for research, education and portfolio demonstration only. "
    "It is not intended for clinical diagnosis, treatment selection or medical decision making."
)
