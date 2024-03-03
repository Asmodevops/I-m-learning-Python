CREATE TABLE IF NOT EXISTS films(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	release_date INTEGER,
	genre TEXT, 
	duration INTEGER
);

INSERT INTO films (id, title, release_date, genre, duration) VALUES
	(1, 'Титаник', 1998, 'Драма', 194), 
	(2, 'Аватар', 2009 , 'Фантастика', 162), 
	(3, 'Пираты Карибского моря: Проклятие Черной жемчужины', 2003, 'Фэнтези', 143), 
	(4, 'Переводчик', 2023, 'Боевик', 123), 
	(5, 'Достать ножи', 2019, 'Детектив', 130),
	(6, 'Эйс Вентура: Розыск домашних животных', 1994, 'Комедия', 86),
	(7, 'Терминатор', 1984, 'Боевик', 108);


--Получить список всех фильмов вместе с их названиями, датами выхода и жанрами.
SELECT title, release_date, genre FROM films;

--Найти фильмы, вышедшие после 2010 года.
SELECT * from films WHERE release_date > 2010;

--Получить список фильмов жанра "Фантастика".
SELECT * FROM films WHERE genre == 'Фантастика';

--Найти фильмы с длительностью более 150 минут.
SELECT * FROM films WHERE duration > 150;

--Получить список фильмов, названия которых начинаются на букву "П".
SELECT * FROM films WHERE title LIKE 'П%';

--Найти фильмы жанра "Боевик", вышедшие до 2005 года.
SELECT * FROM films WHERE genre == 'Боевик' AND release_date < 2005;

--Найти фильмы с длительностью менее 120 минут.
SELECT * FROM films WHERE duration < 120;




CREATE TABLE IF NOT EXISTS albums(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	artist INTEGER NOT NULL,
	release_date INTEGER, 
	genre TEXT
);

INSERT INTO albums (id, title, artist, release_date, genre) VALUES
	(1, 'Акустический альбом', 'Король и шут', 1999, 'Рок'), 
	(2, 'Abbey Road', 'The Beatles', 1969, 'Рок'), 
	(3, 'Баста / Смоки Мо', 'Баста и Смоки Мо', 2015, 'Хип-хоп'), 
	(4, 'Номер 1', 'Artik & Asti', 2021, 'Поп'), 
	(5, 'Русский народный R’n’B', 'Бьянка', 2006, 'Хип-хоп'), 
	(6, 'Singles of the 90s', 'Ace of Base', 1999, 'Поп'); 


-- Получить список всех альбомов вместе с их названиями, исполнителями, датами выпуска и жанрами.
SELECT title, artist, release_date, genre FROM albums;

-- Найти альбомы, выпущенные после 2015 года.
SELECT * FROM albums WHERE release_date > 2015;

-- Получить список альбомов жанра "Рок".
SELECT * FROM albums WHERE genre == 'Рок';

-- Найти альбомы с названием, начинающимся на букву "S".
SELECT * FROM albums WHERE title LIKE 'S%';

-- Получить список альбомов, исполнителями которых являются "The Beatles".
SELECT * FROM albums WHERE artist == 'The Beatles';

-- Найти альбомы жанра "Хип-хоп", выпущенные до 2010 года.
SELECT * FROM albums WHERE genre == 'Хип-хоп' and release_date < 2010;

-- Найти альбомы с датой выпуска после 2000 года и жанром "Поп".
SELECT * FROM albums WHERE release_date > 2000 and genre == 'Поп';



	



