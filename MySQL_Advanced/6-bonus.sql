-- a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    INSERT INTO projects(name)
    VALUES(project_name);
    INSERT INTO corrections(correlation_id, user_id, score, project_id)
    VALUES(user_id, user_id, score, (SELECT id FROM projects WHERE name = project_name));
END$$
DELIMITER ;
