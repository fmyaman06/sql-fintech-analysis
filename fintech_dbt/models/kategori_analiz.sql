-- Kategori bazında risk analizi
WITH islemler AS (
    SELECT * FROM islemler
),

kategori_ozet AS (
    SELECT
        kategori,
        COUNT(*)                                        AS islem_sayisi,
        SUM(tutar)                                      AS toplam_tutar,
        AVG(tutar)                                      AS ort_tutar,
        MAX(tutar)                                      AS max_tutar,
        SUM(CASE WHEN durum = 'iptal' 
            THEN 1 ELSE 0 END)                          AS iptal_sayisi,
        SUM(CASE WHEN durum = 'beklemede' 
            THEN 1 ELSE 0 END)                          AS beklemede_sayisi,
        ROUND(
            SUM(CASE WHEN durum = 'iptal' 
                THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
        )                                               AS iptal_orani
    FROM islemler
    GROUP BY kategori
)

SELECT * FROM kategori_ozet
ORDER BY iptal_orani DESC