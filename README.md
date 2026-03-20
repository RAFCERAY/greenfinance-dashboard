# 🌿 GreenFinance Dashboard — Europe

> Dashboard interactif sur la finance durable en Europe · données Banque mondiale

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## 📋 Description
Dashboard d'analyse de la finance durable en Europe avec données réelles de la Banque mondiale.

## 📊 Pages
| Page | Description |
|---|---|
| 🌿 Énergies renouvelables | Part des énergies renouvelables par pays · 2007-2021 |
| 💚 Électricité renouvelable | Part de l'électricité renouvelable par pays · 2010-2021 |

## 🛠️ Stack
- Python · Streamlit · Plotly · Pandas · World Bank API

## ⚙️ Installation
```bash
pip install -r requirements.txt
streamlit run 0_renouvelables.py
```

## 📁 Structure
```
├── 0_renouvelables.py
├── pages/
│   └── 1_green_bonds.py
├── data/
│   ├── renouvelables.csv
│   └── green_bonds.csv
└── requirements.txt
```

*Données : Banque mondiale · Rafika Cervera*
