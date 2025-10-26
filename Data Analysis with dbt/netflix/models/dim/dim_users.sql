WITH ratings AS (
    SELECT DISTINCT user_id FROM {{ ref('src_ratings') }} -- reference to staging model
),

tags AS (
    SELECT DISTINCT user_id FROM {{ ref('src_tags') }} -- reference to staging model
)

SELECT DISTINCT user_id
FROM (
    SELECT user_id FROM ratings
    UNION
    SELECT user_id FROM tags
)