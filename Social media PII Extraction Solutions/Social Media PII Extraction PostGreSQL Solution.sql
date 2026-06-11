"Social Media PII Extraction PostGreSQL Solution"
SELECT CONCAT('******',RIGHT(phone::text,4)) AS anon_phone,
SPLIT_PART(email,'@',2) AS email_domain, CAST(user_id AS int)
FROM social_media_pii_input
ORDER BY anon_phone
