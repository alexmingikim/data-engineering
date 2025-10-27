-- this configuration overrides the default materialization set in dbt_project.yml
-- set model to INCREMENTAL
{{
    config(
        materialized='incremental'
    )
}}

WITH src_ratings AS (
    SELECT * FROM {{ ref('src_ratings') }} -- reference to staging model
)

SELECT
    user_id,
    movie_id,
    rating,
    rating_timestamp
FROM src_ratings
WHERE rating IS NOT NULL

-- incremental logic: updates only for new records and for condition defined below
{% if is_incremental() %} 
    -- only insert new records where the rating_timestamp is greater than the max in the existing table instead of full refresh
    AND rating_timestamp > (SELECT MAX(rating_timestamp) FROM {{ this }})
{% endif %}