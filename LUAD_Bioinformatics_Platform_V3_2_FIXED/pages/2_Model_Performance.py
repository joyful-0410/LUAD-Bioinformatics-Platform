import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, confusion_matrix, classification_report
from utils import FEATURES, load_data, load_model, load_metrics, inject_css

st.set_page_config(page_title="Model Performance | LUAD Platform", page_icon="📊", layout="wide")
inject_css()
st.title("📊 Model Performance")
st.caption("以內建 10-gene dataset 進行固定 train/test split 的模型展示。")

metrics = load_metrics()
c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Accuracy", f"{metrics.get('accuracy',0)*100:.1f}%")
c2.metric("AUC", f"{metrics.get('auc',0):.3f}")
c3.metric("Precision", f"{metrics.get('precision',0):.3f}")
c4.metric("Recall", f"{metrics.get('recall',0):.3f}")
c5.metric("F1-score", f"{metrics.get('f1',0):.3f}")


df = load_data()
model, scaler = load_model()
X = df[FEATURES]
y_col = "risk" if "risk" in df.columns else "target"
y = df[y_col].astype(int)
_, X_test, _, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
X_test_scaled = scaler.transform(X_test)
y_prob = model.predict_proba(X_test_scaled)[:,1]
y_pred = model.predict(X_test_scaled)
fpr,tpr,_ = roc_curve(y_test, y_prob)
cm = confusion_matrix(y_test, y_pred)

left, right = st.columns(2)
with left:
    st.subheader("ROC Curve")
    fig, ax = plt.subplots(figsize=(6,4.5))
    ax.plot(fpr, tpr, linewidth=2.5, label=f"AUC = {metrics.get('auc',0):.3f}")
    ax.plot([0,1],[0,1], linestyle="--", linewidth=1)
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("Receiver Operating Characteristic")
    ax.legend(loc="lower right")
    st.pyplot(fig, clear_figure=True)
with right:
    st.subheader("Confusion Matrix")
    fig, ax = plt.subplots(figsize=(5.5,4.5))
    im = ax.imshow(cm)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, cm[i,j], ha="center", va="center", fontsize=16, fontweight="bold")
    ax.set_xticks([0,1]); ax.set_yticks([0,1])
    ax.set_xticklabels(["Low", "High"]); ax.set_yticklabels(["Low", "High"])
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    ax.set_title("Confusion Matrix")
    st.pyplot(fig, clear_figure=True)

st.subheader("Classification report")
report = classification_report(y_test, y_pred, output_dict=True)
st.dataframe(pd.DataFrame(report).T, use_container_width=True)


