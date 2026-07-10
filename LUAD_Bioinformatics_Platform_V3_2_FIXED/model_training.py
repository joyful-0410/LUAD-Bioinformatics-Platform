import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

ROOT = Path(__file__).resolve().parent
FEATURES = ["SLC34A2","MUC16","ANLN","CDC20","KIF20A","TOP2A","MKI67","BIRC5","TYMS","CCNA2"]

def main():
    data_path = ROOT / "data" / "training_data_10genes.csv"
    df = pd.read_csv(data_path)
    target_col = "risk" if "risk" in df.columns else "target"
    X = df[FEATURES]
    y = df[target_col].astype(int)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    model = RandomForestClassifier(n_estimators=300, random_state=42, class_weight="balanced")
    model.fit(X_train_s, y_train)
    y_pred = model.predict(X_test_s)
    y_prob = model.predict_proba(X_test_s)[:,1]
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("AUC:", roc_auc_score(y_test, y_prob))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1:", f1_score(y_test, y_pred))
    print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
    joblib.dump(model, ROOT / "model.pkl")
    joblib.dump(scaler, ROOT / "scaler.pkl")
    print("Saved model.pkl and scaler.pkl")

if __name__ == "__main__":
    main()
