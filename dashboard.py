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

# Bağlantı
@st.cache_data
def veri_yukle():
    return pd.read_csv('islemler.csv')

df = veri_yukle()

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
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.divider()
st.subheader("🤖 AI Analiz Asistanı")

soru = st.text_input("Veri hakkında soru sor:", 
                      placeholder="Örnek: En riskli kategori hangisi?")

if soru:
    with st.spinner("Analiz yapılıyor..."):
        ozet = filtered_df.groupby('kategori')['tutar'].sum().to_string()
        
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages = [
                {"role": "system", "content": "Sen bir FinTech analistisin. Türkçe, kısa cevap ver."},
                {"role": "user", "content": f"Veri:\n{ozet}\n\nSoru: {soru}"}
            ]
        )
        
        st.success(response.choices[0].message.content)