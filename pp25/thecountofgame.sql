SELECT u.user_name, COUNT(s.id) as games_played
FROM users u
JOIN user_score s ON u.user_id = s.user_id
GROUP BY u.user_name
ORDER BY games_played DESC;
