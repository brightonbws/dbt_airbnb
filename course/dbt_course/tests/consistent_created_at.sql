SELECT
    *
FROM
    {{ ref('dim_listings_cleansed') }} AS dlc
JOIN
    {{ ref('fct_reviews') }} AS fr
ON
    dlc.listing_id = fr.listing_id
WHERE
    fr.review_date <= dlc.created_at
LIMIT 10