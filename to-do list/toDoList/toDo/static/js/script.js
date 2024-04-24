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