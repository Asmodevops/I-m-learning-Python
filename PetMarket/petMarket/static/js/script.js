p_element = document.getElementsByTagName('p'); // находим элемент
p_element[0].setAttribute('class', 'p-style'); //измение элемента

btn_theme = document.getElementById('btn_theme')


// функция при загрузки страницы будет брать тему из локального хранилаща

// нажимаем на кнопку меняется надпись и тема
// повтороное нажатие на кнопку меняется надпись и тема
function changeTheme() {
    mode = localStorage.getItem('theme');// получить значение темы
    if (mode == 'dark') {
        console.log(localStorage.getItem('theme'));
        document.body.classList.remove('dark-mode') //обратиться к стилям и сменить их
        document.body.classList.add('light-mode')
        localStorage.setItem('theme', 'light');
    } else {
        console.log(localStorage.getItem('theme'));
        document.body.classList.remove('light-mode')
        document.body.classList.add('dark-mode') //обратиться к стилям и сменить их
        localStorage.setItem('theme', 'dark');
    }
}

document.addEventListener("DOMContentLoaded ",changeTheme);

btn_theme.addEventListener('click', changeTheme);
// // save
// localStorage.setItem('theme', 'light'); // локально на компьютер

// //read
// console.log(localStorage.getItem('theme'));

//sessionStorage.setItem('username', 'John');
console.log(sessionStorage.getItem('username'));

document.cookie = "name=oeschger; SameSite=None; Secure";
document.cookie = "favorite_food=tripe; SameSite=None; Secure";

function showCookies() {
    const output = document.getElementById("cookies");
    output.textContent = `> ${document.cookie}`;
}

function clearOutputCookies() {
    const output = document.getElementById("cookies");
    output.textContent = "";
}
















// -----------------------------------AJAX -------------------------------------------------------//
const requestUrl = 'https://jsonplaceholder.typicode.com/users';
let isLoading = false;

function sendRequest() {
    if (isLoading) return;

    isLoading = true;
    $.ajax({ // -инициализация AJAX-запроса
        url: requestUrl,
        method: 'GET',
        dataType: 'json',// -ожидание получение определенного типа
        success: function(data) {
            console.log('Good data', data);
            displayData(data);// вызов функции с отображением данных на странице
            //$('#result').append('<p>' + JSON.stringify(data) + '</p>');
        },
        error: function(err) {// в случае возникновения ошибки
            console.log('Error data', err);
        },
        complete: function() {// в случае любого завершения
            isLoading = false;
        }
    });
}

function displayData(users) {// просто красивое отображение данных пользователя
    const resultContainer = $('#result');
    users.forEach(user => {
        const userCard = $('<div class="user-card"></div>');
        userCard.append('<p><strong>id:</strong> ' + user.id + '</p>');
        userCard.append('<p><strong>Name:</strong> ' + user.name + '</p>');
        userCard.append('<p><strong>Email:</strong> ' + user.email + '</p>');
        userCard.append('<p><strong>Username:</strong> ' + user.username + '</p>');
        userCard.append('<p><strong>City:</strong> ' + user.address.city + '</p>');
        userCard.append('<p><strong>-------------------------------------</strong></p>');
        resultContainer.append(userCard);
    });
}
$(document).ready(function() {
    // Добавляем обработчик события прокрутки
    $(window).scroll(function() { //$(window).scroll в течении пролистывания страницы
        if ($(window).scrollTop() + $(window).height() >= $(document).height() - 200) {
            // Прокрутили достаточно близко к концу страницы
            sendRequest();
        }
    });

    // Инициируем первый запрос
    sendRequest();
});

const fb_btn = document.getElementById("fb");

function alertFb(event) {
    alert('Отзыв не должен быть пустым!')
}

.addEventListener('click', handleClickFunction)



fb_btn.onclick = function() {
    let fb = document.getElementById("fb").value;
    console.log(fb);
    if (fb == null){
        console.log("Please enter");
        alert('Отзыв не должен быть пустым!'); };
};