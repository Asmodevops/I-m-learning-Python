const fb_btn = document.getElementById("fb_submit");

fb_btn.onclick = function() {
    let fb = document.getElementById("fb-input").value;
    if (fb == ''){
        alert('Отзыв не должен быть пустым!'); };
};