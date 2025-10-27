WITH raw_movies AS (
    SELECT * FROM {{sources('netflix', 'r_movies')}} -- using a source definition
)
SELECT 
    movieID AS movie_id,
    title,
    genres
FROM raw_movies