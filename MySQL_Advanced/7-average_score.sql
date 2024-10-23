-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
-- Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score INT;
    SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id;
    IF total_score IS NULL THEN
        SET total_score = 0;
    END IF;
    UPDATE users SET average_score = total_score / (SELECT COUNT(*) FROM corrections WHERE user_id = user_id) WHERE id = user_id;
END$$
DELIMITER;
