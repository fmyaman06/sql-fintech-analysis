import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from groq import Groq
import os
from dotenv import load_dotenv

# Sayfa ayarları
st.set_page_config(
    page_title = "FinTech Dashboard",
    page_icon  = "🏦",
    layout     = "wide"
)

# ENV yükle
client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))

# Bağlantı
engine = create_engine(
    "postgresql://postgres@localhost:5432/fintech_db"
)

# Veri yükle
@st.cache_data
def veri_yukle():
    return pd.read_csv('islemler.csv')

df = veri_yukle()

# dbt mart tablosunu yükle
@st.cache_data
def risk_yukle():
    return pd.read_sql(
        "SELECT * FROM dbt_dev.mart_risk_analizi ORDER BY iptal_orani DESC",
        engine
    )

risk_df = risk_yukle()

# Groq client

client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))

# Başlık
st.title("🏦 FinTech İşlem Analizi")
st.markdown("Finansal işlem verilerini analiz eden interaktif dashboard.")
st.divider()

# Sidebar
st.sidebar.title("🔍 Filtreler")
kategoriler = df['kategori'].unique().tolist()
secili_kategori = st.sidebar.multiselect(
    "Kategori",
    options = kategoriler,
    default = kategoriler
)

durumlar = df['durum'].unique().tolist()
secili_durum = st.sidebar.multiselect(
    "Durum",
    options = durumlar,
    default = durumlar
)

# Filtrele
filtered_df = df[
    (df['kategori'].isin(secili_kategori)) &
    (df['durum'].isin(secili_durum))
]

# KPI kartları
st.subheader("📊 Özet")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Toplam İşlem",    len(filtered_df))
col2.metric("Toplam Tutar",    f"{filtered_df['tutar'].sum():,.0f} TL")
col3.metric("Ortalama Tutar",  f"{filtered_df['tutar'].mean():,.0f} TL")
col4.metric("En Yüksek Tutar", f"{filtered_df['tutar'].max():,.0f} TL")

st.divider()

# Grafikler
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Kategori Bazında Tutar")
    ozet = filtered_df.groupby('kategori')['tutar'].sum().reset_index()
    fig1 = px.bar(ozet, x='kategori', y='tutar', color='kategori')
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    st.subheader("Durum Dağılımı")
    durum_ozet = filtered_df.groupby('durum')['tutar'].sum().reset_index()
    fig2 = px.pie(durum_ozet, values='tutar', names='durum', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Tutar Dağılımı")
fig3 = px.box(filtered_df, x='kategori', y='tutar', color='kategori')
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Veri tablosu
st.subheader("📋 İşlem Detayları")
st.dataframe(filtered_df, use_container_width=True)

st.divider()

# Risk analizi
st.subheader("🎯 Risk Analizi — dbt Pipeline")

col_r1, col_r2 = st.columns(2)

with col_r1:
    st.markdown("**Kategori & Segment Bazında İptal Oranı**")
    fig_risk = px.bar(
        risk_df,
        x       = 'kategori',
        y       = 'iptal_orani',
        color   = 'tutar_segmenti',
        barmode = 'group',
        title   = 'İptal Oranı (%)'
    )
    st.plotly_chart(fig_risk, use_container_width=True)

with col_r2:
    st.markdown("**Risk Tablosu**")
    st.dataframe(
        risk_df[['kategori', 'tutar_segmenti',
                 'islem_sayisi', 'iptal_orani']],
        use_container_width=True
    )

st.divider()

# AI Analiz Asistanı
st.subheader("🤖 AI Analiz Asistanı")

soru = st.text_input("Veri hakkında soru sor:",
                      placeholder="Örnek: En riskli kategori hangisi?")

if soru:
    with st.spinner("Analiz yapılıyor..."):
        ozet_str = filtered_df.groupby('kategori')['tutar'].sum().to_string()

        response = client.chat.completions.create(
            model    = "llama-3.3-70b-versatile",
            messages = [
                {"role": "system", "content": "Sen bir FinTech analistisin. Türkçe, kısa cevap ver."},
                {"role": "user", "content": f"Veri:\n{ozet_str}\n\nSoru: {soru}"}
            ]
        )

        st.success(response.choices[0].message.content)