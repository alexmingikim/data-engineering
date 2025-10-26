WITH src_tags AS (
    SELECT * FROM {{ ref('src_genome_tags') }} -- reference to staging model
)

SELECT
    tag_id,
    INITCAP(TRIM(tag)) AS tag_name -- remove extra spaces and capitalise
FROM src_tags