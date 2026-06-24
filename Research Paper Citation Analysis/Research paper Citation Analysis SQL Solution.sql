SELECT a1.author_id,a1.name, a1.paper_id, 
ROW_NUMBER() OVER (PARTITION BY a1.paper_id ORDER BY a1.author_id)
FROM ai_author AS a1
INNER JOIN ai_research_papers AS a2 ON a1.paper_id = a2.paper_id