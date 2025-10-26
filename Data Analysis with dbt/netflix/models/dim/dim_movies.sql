WITH src_movies AS (
    SELECT * FROM {{ ref('src_movies') }} -- reference to staging model
)

SELECT
    movie_id,
    INITCAP(TRIM(title)) AS movie_title, -- remove extra spaces and capitalise
    SPLIT(genres, '|') AS genre_array, -- convert genres to array
    genres
FROM src_movies
