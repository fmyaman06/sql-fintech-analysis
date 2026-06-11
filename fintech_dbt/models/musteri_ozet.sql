-- Müşteri bazında özet analizi
WITH islemler AS (
    SELECT * FROM islemler
),

ozet AS (
    SELECT
        musteri_id,
        COUNT(*)                                    AS islem_sayisi,
        SUM(tutar)                                  AS toplam_tutar,
        AVG(tutar)                                  AS ort_tutar,
        MAX(tutar)                                  AS max_tutar,
        SUM(CASE WHEN durum = 'onaylı' 
            THEN tutar ELSE 0 END)                  AS onayli_toplam,
        SUM(CASE WHEN durum = 'iptal' 
            THEN tutar ELSE 0 END)                  AS iptal_toplam
    FROM islemler
    GROUP BY musteri_id
)

SELECT * FROM ozet