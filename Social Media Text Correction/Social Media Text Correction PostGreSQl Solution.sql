SELECT comments, date, id, likes, platform,shares,
REGEXP_REPLACE(text,'Python','PySpark') AS text 
FROM correct_social_media_post
ORDER BY comments