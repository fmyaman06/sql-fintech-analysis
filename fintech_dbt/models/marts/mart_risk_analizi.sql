-- İş analizine hazır risk tablosu
WITH stg AS (
    SELECT * FROM {{ ref('stg_islemler') }}
),

risk_ozet AS (
    SELECT
        kategori,
        tutar_segmenti,
        COUNT(*)                            AS islem_sayisi,
        SUM(tutar)                          AS toplam_tutar,
        AVG(tutar)                          AS ort_tutar,
        SUM(CASE WHEN iptal_mi = TRUE 
            THEN 1 ELSE 0 END)              AS iptal_sayisi,
        ROUND(
            SUM(CASE WHEN iptal_mi = TRUE 
                THEN 1 ELSE 0 END) * 100.0 
            / COUNT(*), 2
        )                                   AS iptal_orani
    FROM stg
    GROUP BY kategori, tutar_segmenti
)

SELECT * FROM risk_ozet
ORDER BY iptal_orani DESC