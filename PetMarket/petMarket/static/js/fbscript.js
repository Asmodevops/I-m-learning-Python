const fb_btn = document.querySelector(".fb_btn");

fb_btn.onclick = function() {
    let fb = document.querySelector(".form-input").value;
    if (fb == ''){
        alert('Отзыв не должен быть пустым!'); };
};