let task_header = document.querySelectorAll('.task_header');
for (let i = 0; i < task_header.length; i++){
    task_header[i].addEventListener ('click', function (){
        this.classList.toggle('active');
        let panel = this.nextElementSibling;
        if (panel.style.maxHeight){
            panel.style.maxHeight = null;
        }
        else{
            panel.style.maxHeight = panel.scrollHeight + 'px';
        }
    });
}


let task_add_btn = document.querySelector(".task-submit")
task_add_btn.onclick = function() {
    let task_name = document.querySelector(".task-name").value;
    let task_text = document.querySelector(".task-text").value;
    if (task_name == '' || task_text == ''){
        alert('Все поля должны быть заполнены!'); };
};