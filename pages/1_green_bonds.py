import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv("data/green_bonds.csv")

df = load_data()

st.sidebar.title("🌿 GreenFinance Europe")
pays_sel = st.sidebar.multiselect(
    "Pays", sorted(df["country"].unique()),
    default=["France", "Germany", "Sweden", "Denmark"]
)
annees = st.sidebar.slider("Période", 2010, 2021, (2012, 2021))
df_f = df[df["country"].isin(pays_sel) & df["year"].between(annees[0], annees[1])]

st.title("💚 Électricité Renouvelable")
st.markdown("**Source : Banque mondiale**")
st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("Pays", len(pays_sel))
col2.metric("Période", f"{annees[0]}–{annees[1]}")
col3.metric("Moyenne", f"{df_f['elec_renouvelable'].mean():.1f}%" if not df_f.empty else "-")

st.markdown("---")

if not df_f.empty:
    fig = px.line(df_f, x="year", y="elec_renouvelable", color="country",
                  labels={"elec_renouvelable": "Électricité renouvelable (%)", "year": "Année"},
                  color_discrete_sequence=px.colors.qualitative.Set2,
                  template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    df_moy = df_f.groupby("country")["elec_renouvelable"].mean().reset_index().sort_values("elec_renouvelable")
    df_moy["elec_renouvelable"] = df_moy["elec_renouvelable"].round(1)
    fig2 = px.bar(df_moy, x="elec_renouvelable", y="country", orientation="h",
                  color="elec_renouvelable", color_continuous_scale="Greens",
                  text="elec_renouvelable", template="plotly_dark")
    fig2.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    fig2.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.markdown("*💚 GreenFinance Europe · Données Banque mondiale · Rafika Cervera*")