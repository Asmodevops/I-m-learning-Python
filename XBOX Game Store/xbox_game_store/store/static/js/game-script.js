document.addEventListener('DOMContentLoaded', function() {
    const description = document.querySelector('.game-description');
    const expandBtn = document.querySelector('.btn-expand');

    if (description.scrollHeight > description.clientHeight + 20) {
        expandBtn.classList.remove('d-none');
    }

    expandBtn.addEventListener('click', function() {
        description.classList.toggle('expanded');
        if (description.classList.contains('expanded')) {
            expandBtn.textContent = 'Свернуть';
            description.style.maxHeight = description.scrollHeight + 'px';
        } else {
            expandBtn.textContent = 'Развернуть';
            description.style.maxHeight = '145px';
        }
    });
});
