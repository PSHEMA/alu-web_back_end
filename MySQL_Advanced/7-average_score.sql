-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
-- Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_score FLOAT;
    SELECT AVG(score) INTO average_score FROM corrections WHERE user_id = input_user_id;
    UPDATE users SET average_score = average_score WHERE id = input_user_id;
END$$
DELIMITER;
