'PostGreSQL Solution'
SELECT duration, genre, release_year, title, video_id, view_count
FROM video_stream
WHERE view_count >1000000
    AND release_year >= EXTRACT(YEAR FROM current_date)-8
ORDER BY 1 ASC