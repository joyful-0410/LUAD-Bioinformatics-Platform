# Lung Cancer Bioinformatics Platform V3.2 FIXED

This version fixes the model/scaler feature mismatch.

## Run

```cmd
pip install -r requirements.txt
streamlit run app.py --server.port 8502
```

Then open: http://localhost:8502

## Notes

The model and scaler in this folder are trained with the same 10 genes used by the website:
SLC34A2, MUC16, ANLN, CDC20, KIF20A, TOP2A, MKI67, BIRC5, TYMS, CCNA2.
