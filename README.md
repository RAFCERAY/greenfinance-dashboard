# 🌿 GreenFinance Dashboard — Europe

> **Dashboard interactif sur la finance durable en Europe** · données Banque mondiale (2007-2021)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://greenfinance-dashboard-axquz7mjqrk8ynnrx3gf4v.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 🚀 Démo en ligne

**👉 [Accéder au dashboard](https://greenfinance-dashboard-axquz7mjqrk8ynnrx3gf4v.streamlit.app/)**

> Aucune installation requise. L'application est hébergée gratuitement sur Streamlit Community Cloud.

---

## 📋 Description

Dashboard d'analyse de la **finance durable en Europe** combinant données ouvertes de la Banque mondiale et indicateurs de transition énergétique. Le projet couvre l'ensemble du pipeline analytique : de l'exploration brute jusqu'à la visualisation interactive et la génération automatique de rapports.

**Objectifs :**
- Cartographier la part des énergies renouvelables dans le mix énergétique européen
- Suivre la trajectoire de l'électricité verte par pays sur 10+ ans
- Identifier les leaders et les retardataires de la transition énergétique
- Fournir un outil reproductible pour la veille ESG / finance durable

---

## 📊 Pages du dashboard

| Page | Indicateur | Période | Source |
| --- | --- | --- | --- |
| 🌿 **Énergies renouvelables** | Part des renouvelables dans la consommation finale (%) | 2007-2021 | World Bank (`EG.FEC.RNEW.ZS`) |
| 💚 **Électricité renouvelable** | Part des renouvelables dans la production électrique (%) | 2010-2021 | World Bank (`EG.ELC.RNEW.ZS`) |

---

## 🛠️ Stack technique

- **Python 3.12** — langage principal
- **Streamlit** — interface interactive multi-pages
- **Plotly** — visualisations dynamiques (cartes, séries temporelles, barres)
- **Pandas** — manipulation de données tabulaires
- **World Bank API** — ingestion des indicateurs ouverts
- **Jupyter Notebook** — exploration & analyse exploratoire

---

## ⚙️ Installation locale

```bash
# 1. Cloner le repo
git clone https://github.com/RAFCERAY/greenfinance-dashboard.git
cd greenfinance-dashboard

# 2. Créer un environnement virtuel (recommandé)
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# ou : venv\Scripts\activate   # Windows

# 3. Installer les dépendances
pip3 install -r requirements.txt

# 4. Lancer l'application
python3 -m streamlit run 0_renouvelables.py
```

L'application s'ouvre automatiquement sur `http://localhost:8501`.

---

## 📁 Structure du projet

```
greenfinance-dashboard/
│
├── 0_renouvelables.py          # 🏠 Page d'accueil — énergies renouvelables
├── pages/
│   └── 1_green_bonds.py        # 💚 Page secondaire — électricité verte
│
├── data/                       # 📂 Données nettoyées (CSV)
│   ├── renouvelables.csv
│   └── green_bonds.csv
│
├── 01_exploration.ipynb        # 🔍 Exploration des données brutes
├── 02_nettoyage.ipynb          # 🧹 Nettoyage & préparation
├── 03_analyse.ipynb            # 📈 Analyse statistique & insights
│
├── reports/                    # 📄 Rapports générés
├── rapport_greenfinance.md     # Rapport de synthèse
├── generate_presentation.py    # Génération automatique du deck
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📈 Méthodologie

1. **Ingestion** — Téléchargement des indicateurs World Bank via API publique
2. **Nettoyage** — Filtrage Europe, gestion des valeurs manquantes, harmonisation des codes ISO pays
3. **Analyse exploratoire** — Distribution, tendances, classement par pays
4. **Visualisation** — Construction de l'interface Streamlit avec graphiques Plotly interactifs
5. **Reporting** — Synthèse Markdown + génération automatique de présentation

---

## 🎯 Cas d'usage

- 🏦 **Analystes ESG** — suivi macro de la transition énergétique européenne
- 📚 **Étudiants finance / data** — exemple de pipeline data complet (extract → clean → visualize → report)
- 🌍 **Veille climat** — accès rapide aux indicateurs Banque mondiale sans coder

---

## 🔜 Roadmap

- [ ] Ajout d'une page Green Bonds (émissions obligataires vertes par pays)
- [ ] Intégration des indicateurs CO₂ par habitant
- [ ] Comparaison Europe vs reste du monde
- [ ] Export PDF des analyses depuis le dashboard

---

## 📝 Sources de données

- [World Bank Open Data](https://data.worldbank.org/) — indicateurs énergie & environnement
- Code indicateurs : `EG.FEC.RNEW.ZS`, `EG.ELC.RNEW.ZS`

---

## 👤 Auteure

**Rafika Cervera** — Data Governance & Analytics
[GitHub](https://github.com/RAFCERAY) · [Portfolio](https://github.com/RAFCERAY?tab=repositories)

---

## 📄 Licence

Ce projet est distribué sous licence MIT — voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

*⭐ Si ce projet t'a été utile, n'hésite pas à laisser une étoile sur le repo !*
