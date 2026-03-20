import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="GreenFinance Europe",
    page_icon="🌿",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("data/renouvelables.csv")

df = load_data()

# Sidebar
st.sidebar.title("🌿 GreenFinance Europe")
st.sidebar.markdown("---")
st.sidebar.markdown("---")

pays_sel = st.sidebar.multiselect(
    "Pays", sorted(df["country"].unique()),
    default=["France", "Germany", "Sweden", "Denmark"]
)
annees = st.sidebar.slider("Période", 2007, 2021, (2010, 2021))

df_f = df[df["country"].isin(pays_sel) & df["year"].between(annees[0], annees[1])]

st.title("🌿 GreenFinance Europe")
st.markdown("**Part des énergies renouvelables · Source : Banque mondiale**")
st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("Pays sélectionnés", len(pays_sel))
col2.metric("Période", f"{annees[0]}–{annees[1]}")
col3.metric("Moyenne renouvelables", f"{df_f['value'].mean():.1f}%" if not df_f.empty else "-")

st.markdown("---")

st.subheader("Évolution de la part des énergies renouvelables")
if df_f.empty:
    st.warning("Sélectionne au moins un pays.")
else:
    fig = px.line(df_f, x="year", y="value", color="country",
                  labels={"value": "Part renouvelables (%)", "year": "Année"},
                  color_discrete_sequence=px.colors.qualitative.Set2,
                  template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Comparaison par pays — moyenne sur la période")
if not df_f.empty:
    df_moy = df_f.groupby("country")["value"].mean().reset_index().sort_values("value")
    df_moy["value"] = df_moy["value"].round(1)
    fig2 = px.bar(df_moy, x="value", y="country", orientation="h",
                  color="value", color_continuous_scale="Teal",
                  text="value", template="plotly_dark")
    fig2.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig2.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

with st.expander("Voir les données brutes"):
    st.dataframe(df_f.sort_values(["country", "year"]), use_container_width=True)

st.markdown("---")
st.markdown("*🌿 GreenFinance Europe · Données Banque mondiale · Rafika Cervera*")
