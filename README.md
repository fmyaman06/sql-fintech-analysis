# 🏦 FinTech AI Veri Analizi / FinTech AI Data Analysis

[🇹🇷 Türkçe](#türkçe) | [🇬🇧 English](#english)

---

## Türkçe

SQL, Python, makine öğrenmesi ve LLM teknolojilerini birleştiren, dbt pipeline'ı ile desteklenen tam kapsamlı bir FinTech veri analizi projesi.

### 🚀 Canlı Demo
[Dashboard'u Görüntüle](BURAYA_LİNKİNİ_YAZ)

### 📊 Özellikler
- Kategori ve durum bazında filtrelenebilir dashboard
- KPI kartları: toplam işlem, tutar, ortalama
- İnteraktif Plotly grafikleri
- dbt pipeline'dan gelen risk analizi
- 🤖 AI Analiz Asistanı — Groq LLM ile doğal dilde soru sor
- Fraud detection modeli (Random Forest + SHAP)

### 🛠️ Kullanılan Teknolojiler
| Teknoloji | Kullanım |
|-----------|---------|
| Python | Ana dil |
| PostgreSQL | Veritabanı |
| pandas | Veri analizi |
| Plotly | Görselleştirme |
| Streamlit | Web uygulaması |
| dbt | Veri pipeline |
| scikit-learn | ML modelleri |
| SHAP | Model açıklama |
| LangChain | LLM zinciri |
| Groq API | LLM (Llama 3.3) |
| SQL | Veri sorgulama |

### 📁 Proje Yapısı
sql-fintech-analysis/
├── dashboard.py              # Streamlit uygulaması
├── islemler.csv              # Veri seti
├── requirements.txt          # Bağımlılıklar
├── hafta1_sql_eda.ipynb      # SQL & pandas EDA
├── hafta3_makine_ogrenmesi.ipynb  # ML & SHAP
├── hafta4_llm_rag.ipynb      # LLM & RAG
└── fintech_dbt/              # dbt modelleri
└── models/
├── staging/
│   └── stg_islemler.sql
└── marts/
└── mart_risk_analizi.sql
### 🚀 Kurulum
```bash
git clone https://github.com/fmyaman06/sql-fintech-analysis.git
cd sql-fintech-analysis
pip install -r requirements.txt
streamlit run dashboard.py
```

### 👤 İletişim
LinkedIn: [linkedin.com/in/fmyaman06](https://linkedin.com/in/fmyaman06)
GitHub: [github.com/fmyaman06](https://github.com/fmyaman06)

---

## English

A full-stack FinTech data analysis project combining SQL, Python, machine learning, LLM technologies, and dbt pipeline.

### 🚀 Live Demo
[View Dashboard](BURAYA_LİNKİNİ_YAZ)

### 📊 Features
- Filterable dashboard by category and status
- KPI cards: total transactions, amount, average
- Interactive Plotly charts
- Risk analysis from dbt pipeline
- 🤖 AI Analysis Assistant — ask questions in natural language via Groq LLM
- Fraud detection model (Random Forest + SHAP)

### 🛠️ Tech Stack
| Technology | Usage |
|------------|-------|
| Python | Main language |
| PostgreSQL | Database |
| pandas | Data analysis |
| Plotly | Visualization |
| Streamlit | Web application |
| dbt | Data pipeline |
| scikit-learn | ML models |
| SHAP | Model explainability |
| LangChain | LLM chain |
| Groq API | LLM (Llama 3.3) |
| SQL | Data querying |

### 🚀 Installation
```bash
git clone https://github.com/fmyaman06/sql-fintech-analysis.git
cd sql-fintech-analysis
pip install -r requirements.txt
streamlit run dashboard.py
```

### 👤 Contact
LinkedIn: [linkedin.com/in/fmyaman06](https://linkedin.com/in/fmyaman)
GitHub: [github.com/fmyaman06](https://github.com/fmyaman06)
