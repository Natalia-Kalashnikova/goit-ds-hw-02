-- 1. Все задачи пользователя по user_id
SELECT * FROM tasks WHERE user_id = 1;

-- 2. Задачи по статусу (например, 'new')
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- 3. Обновить статус задачи
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 4;
SELECT * FROM tasks where id = 4;

-- 4. Пользователи без задач
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

-- 5. Добавить задачу пользователю
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ("Test add", "Add test task", 3, 1);
SELECT * FROM tasks where user_id = 1;

-- 6. Все незавершённые задачи
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- 7. Удалить задачу по id
DELETE FROM tasks WHERE id = 60;

-- 8. Найти пользователей по email (LIKE)
SELECT * FROM users WHERE email LIKE '%son%';

-- 9. Обновить имя пользователя
UPDATE users SET fullname = "Tatyana Filimonova" WHERE id = 5;
SELECT * FROM users WHERE id = 5;

-- 10. Количество задач по статусам
SELECT s.name, COUNT(t.id) FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.id;

-- 11. Задачи пользователей с определённым доменом email
SELECT t.* FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com%';

-- 12. Задачи без описания
SELECT * FROM tasks WHERE description IS NULL;

-- 13. Пользователи и их задачи в статусе 'in progress'
SELECT u.fullname, t.title FROM users u
JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- 14. Пользователи и количество их задач
SELECT u.fullname, COUNT(t.id) as task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id;
