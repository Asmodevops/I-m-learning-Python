/* 
Создать таблицу группа (имя, рейтинг, курс)
добавить 3 любые группы 
*показать группы(имя, рейтинг и курс)  рейтинг, которых меньше либо равен 50 
*/


CREATE TABLE IF NOT EXISTS mygroup(
	name TEXT PRIMARY KEY,
	rating INTEGER,
	class TEXT
);

INSERT INTO mygroup (name, rating, class) VALUES
    ('group1', 40, 1),
    ('group2', 55, 2),
    ('group3', 30, 3); 
	
	
SELECT * FROM mygroup WHERE rating <= 50;


/* 
Создать таблицу оружие(имя, тип, мощность)
добавить 3 любых оружия
показать оружия(имя, тип и мощность) мощность, которых равна 200
*/

CREATE TABLE IF NOT EXISTS weapons(
	name TEXT PRIMARY KEY,
	type TEXT, 
	power INTEGER
);

INSERT INTO weapons (name, type, power) VALUES
    ('Widow''s Cry', 'Sword', 200),
    ('True to the Oath', 'Sword', 190),
    ('Heartbreaker', 'Sword', 210); 


SELECT * FROM weapons WHERE power == 200;


/* 
Создать таблицу игры (имя игры, дата и время сохранения)
добавить 3 любые игры 
показать все записи игр
*/


CREATE TABLE IF NOT EXISTS games(
	name TEXT PRIMARY KEY,
	save_date TEXT,
	save_time TEXT
);


INSERT INTO games (name, save_date, save_time) VALUES
    ('The Witcher', '01.03.2024', '14:34'),
    ('Grand Theft Auto VI', '01.03.2024', '15:55'),
    ('Red Dead Redemption 2', '29.02.2024', '22:30'); 

SELECT * FROM games;


