{{
    config(
        materialized='table'
    )
}}

WITH fct_ratings AS (
    SELECT * FROM {{ ref('fct_ratings') }} -- reference to fact model
),
seed_dates AS (
    SELECT * FROM {{ ref('seed_movie_release_dates') }} -- reference to seed model
)

SELECT 
    r.*,
    CASE
        WHEN d.release_date IS NOT NULL THEN 'unknown'
        ELSE 'known'
    END AS release_info_available
FROM fct_ratings r
LEFT JOIN seed_dates d ON r.movie_id = d.movie_id