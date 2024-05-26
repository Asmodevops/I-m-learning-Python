document.addEventListener('DOMContentLoaded', function() {
    const loadMoreBtn = document.getElementById('load-more-btn');
    const gameContainer = document.getElementById('game-container');
    const loadMoreContainer = document.getElementById('load-more-container');
    const priceCheckboxes = document.querySelectorAll('.filter-checkbox[data-filter="price"]');
    const genreCheckboxes = document.querySelectorAll('.filter-checkbox[data-filter="genre"]');
    const featureCheckboxes = document.querySelectorAll('.filter-checkbox[data-filter="feature"]');

    function truncateWords(str, numWords) {
        const words = str.split(' ');
        return words.length > numWords ? words.slice(0, numWords).join(' ') + '...' : str;
    }

    function getFilterValues() {
        const filters = {};
        priceCheckboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                filters.price = checkbox.value;
            }
        });
        genreCheckboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                filters.genre = checkbox.value;
            }
        });
        featureCheckboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                filters.feature = checkbox.value;
            }
        });
        return filters;
    }

    function updateGames() {
        const filters = getFilterValues();

        // Убедимся, что в объекте filters нет ключей с пустыми значениями
        if (!filters.price) {
            delete filters.price;
        }
        if (!filters.genre) {
            delete filters.genre;
        }
        if (!filters.feature) {
            delete filters.feature;
        }

        const queryString = new URLSearchParams(filters).toString();
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `/catalog/?${queryString}`, true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 400) {
                const data = JSON.parse(xhr.responseText);
                gameContainer.innerHTML = '';
                data.games.forEach(function(game) {
                    const gameCard = document.createElement('div');
                    gameCard.classList.add('d-flex', 'mb-5', 'game-card', 'p-3');
                    gameCard.innerHTML = `
                        <a href="/game/${game.id}" title="${game.title}" class="d-flex">
                            <img src="${game.image}" class="img-fluid" alt="${game.title}">
                            <div class="d-flex flex-column">
                                <h3 class="text-white">${game.title}</h3>
                                <br>
                                <br>
                                <p class="text-white text-justify">${truncateWords(game.description, 50)}</p>
                                <br>
                                <h5 class="text-white">Цена: ${game.price}</h5>
                            </div>
                        </a>
                    `;
                    gameContainer.appendChild(gameCard);
                });

                if (data.has_next) {
                    loadMoreBtn.setAttribute('data-next-page', data.next_page_number);
                    gameContainer.appendChild(loadMoreContainer); // Перемещаем кнопку в конец
                    loadMoreContainer.style.display = 'block';
                } else {
                    loadMoreContainer.style.display = 'none';
                }
            }
        };
        xhr.onerror = function() {
            console.error('Request failed.');
        };
        xhr.send();
    }

    priceCheckboxes.forEach(function(checkbox) {
        checkbox.addEventListener('click', function() {
            if (checkbox.checked) {
                // Сбросить остальные чекбоксы по цене
                priceCheckboxes.forEach(function(cb) {
                    if (cb !== checkbox) {
                        cb.checked = false;
                    }
                });
            }
            updateGames(); // Обновить список игр после изменения фильтров
        });
    });

    genreCheckboxes.forEach(function(checkbox) {
        checkbox.addEventListener('click', function() {
            if (checkbox.checked) {
                // Сбросить остальные чекбоксы по жанру
                genreCheckboxes.forEach(function(cb) {
                    if (cb !== checkbox) {
                        cb.checked = false;
                    }
                });
            }
            updateGames(); // Обновить список игр после изменения фильтров
        });
    });

    featureCheckboxes.forEach(function(checkbox) {
        checkbox.addEventListener('click', function() {
            if (checkbox.checked) {
                // Сбросить остальные чекбоксы по техническим возможностям
                featureCheckboxes.forEach(function(cb) {
                    if (cb !== checkbox) {
                        cb.checked = false;
                    }
                });
            }
            updateGames(); // Обновить список игр после изменения фильтров
        });
    });

    if (loadMoreBtn && gameContainer) {
        loadMoreBtn.addEventListener('click', function() {
            const nextPage = loadMoreBtn.getAttribute('data-next-page');
            const filters = getFilterValues();
            filters.page = nextPage;
            const queryString = new URLSearchParams(filters).toString();
            const xhr = new XMLHttpRequest();
            xhr.open('GET', `/catalog/?${queryString}`, true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            xhr.onload = function() {
                if (xhr.status >= 200 && xhr.status < 400) {
                    const data = JSON.parse(xhr.responseText);
                    data.games.forEach(function(game) {
                        const gameCard = document.createElement('div');
                        gameCard.classList.add('d-flex', 'mb-5', 'game-card', 'p-3');
                        gameCard.innerHTML = `
                            <a href="/game/${game.id}" title="${game.title}" class="d-flex">
                                <img src="${game.image}" class="img-fluid" alt="${game.title}">
                                <div class="d-flex flex-column">
                                    <h3 class="text-white">${game.title}</h3>
                                    <br>
                                    <br>
                                    <p class="text-white text-justify">${truncateWords(game.description, 50)}</p>
                                    <br>
                                    <h5 class="text-white">Цена: ${game.price}</h5>
                                </div>
                            </a>
                        `;
                        gameContainer.appendChild(gameCard);
                    });

                    if (data.has_next) {
                        loadMoreBtn.setAttribute('data-next-page', data.next_page_number);
                        gameContainer.appendChild(loadMoreContainer); // Перемещаем кнопку в конец
                    } else {
                        loadMoreContainer.style.display = 'none';
                    }
                }
            };
            xhr.onerror = function() {
                console.error('Request failed.');
            };
            xhr.send();
        });
    }
});
