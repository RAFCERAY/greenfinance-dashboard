# 🌿 Rapport d'analyse — GreenFinance Europe
**Auteure : Rafika Cervera | Date : Mars 2026**

---

## 1. Contexte et objectifs

Ce rapport analyse la progression des énergies renouvelables en Europe entre 2007 et 2021, 
en comparaison avec l'objectif fixé par l'Union Européenne pour 2030 : **42.5% d'énergies renouvelables**.

**Sources de données :** Banque mondiale — Indicateurs EG.FEC.RNEW.ZS et EG.ELC.RNEW.ZS

**Pays analysés :** Autriche, Belgique, Danemark, France, Allemagne, Italie, Pays-Bas, Pologne, Espagne, Suède

---

## 2. Données

### 2.1 Datasets utilisés

| Dataset | Indicateur | Période | Lignes |
|---|---|---|---|
| renouvelables_clean.csv | Part des énergies renouvelables (%) | 2007-2021 | 150 |
| electricite_clean.csv | Part de l'électricité renouvelable (%) | 2010-2021 | 120 |

### 2.2 Qualité des données
- **0 valeurs manquantes** sur les deux datasets
- **0 doublons** — données Banque mondiale déjà structurées
- **Enrichissement** : ajout des colonnes région, objectif UE 2030, écart à l'objectif

---

## 3. Résultats clés

### 3.1 Progression globale
- Moyenne européenne : **14.1% (2007) → 24.3% (2021)** soit +10.2 points en 14 ans
- À ce rythme, l'Europe n'atteindra pas l'objectif de 42.5% avant 2035
- **Écart restant : +18.2 points** à combler d'ici 2030

### 3.2 Classement des pays (2021)

| Rang | Pays | Part renouvelables | Statut |
|---|---|---|---|
| 🥇 1 | Sweden | 57.9% | ✅ Objectif atteint |
| 🥈 2 | Denmark | 39.5% | 🟡 Proche |
| 🥉 3 | Austria | 36.0% | 🟡 Proche |
| 4 | Spain | 19.0% | 🔴 En retard |
| 5 | Italy | 17.5% | 🔴 En retard |
| 6 | Germany | 17.6% | 🔴 En retard |
| 7 | France | 16.2% | 🔴 En retard |
| 8 | Poland | 15.2% | 🔴 En retard |
| 9 | Netherlands | 12.2% | 🔴 Très en retard |
| 10 | Belgium | 11.7% | 🔴 Très en retard |

### 3.3 Meilleures progressions (2007-2021)
1. **Denmark** : +21.8 points — modèle européen
2. **Sweden** : +16.1 points — leader absolu
3. **Spain** : +10.0 points — bonne dynamique

### 3.4 Analyse par région

| Région | Moyenne renouvelables | Statut |
|---|---|---|
| Nordic | ~39% | 🟡 Proche objectif |
| Central | ~23% | 🔴 En retard |
| Southern | ~15% | 🔴 En retard |
| Eastern | ~11% | 🔴 En retard |
| Western | ~9% | 🔴 Très en retard |

### 3.5 Corrélation
Corrélation de **0.85** entre renouvelables totales et électricité renouvelable — 
les pays qui investissent dans les renouvelables le font de façon cohérente sur tous les secteurs.

---

## 4. Recommandations

### Pour les pays en retard (Belgium, Netherlands, France)
1. **Accélérer les investissements** en éolien offshore et solaire
2. **S'inspirer du modèle danois** — politique énergétique volontariste depuis les années 1990
3. **Réduire les obstacles réglementaires** aux projets d'énergies renouvelables

### Pour maintenir le leadership (Sweden, Denmark)
1. **Exporter leur expertise** vers les pays en retard
2. **Viser 60%+** pour compenser les retards des autres pays européens

---

## 5. Conclusion

L'Europe progresse mais insuffisamment. Seule la **Suède** a atteint l'objectif UE 2030.
Le **Danemark** est le modèle à suivre avec la meilleure progression (+21.8 pts).
Les pays d'Europe occidentale (France, Belgique, Pays-Bas) doivent **tripler leur rythme** 
de transition énergétique pour espérer atteindre l'objectif 2030.

---

*Données : Banque mondiale | Analyse : Rafika Cervera | Outils : Python, Pandas, Matplotlib, Streamlit*