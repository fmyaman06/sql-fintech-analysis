-- Ham veriyi temizle ve standartlaştır
WITH kaynak AS (
    SELECT * FROM islemler
),

temizlenmis AS (
    SELECT
        islem_id,
        musteri_id,
        tutar,
        UPPER(kategori)                    AS kategori,
        LOWER(durum)                       AS durum,
        CASE 
            WHEN durum = 'iptal' THEN TRUE
            ELSE FALSE
        END                                AS iptal_mi,
        CASE
            WHEN tutar >= 5000 THEN 'yuksek'
            WHEN tutar >= 1000 THEN 'orta'
            ELSE 'dusuk'
        END                                AS tutar_segmenti
    FROM kaynak
    WHERE tutar > 0  -- geçersiz tutarları çıkar
)

SELECT * FROM temizlenmis