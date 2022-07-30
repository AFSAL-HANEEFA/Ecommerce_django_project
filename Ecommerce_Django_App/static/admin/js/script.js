const theme_btn = document.querySelector('#theme_btn');
theme()
function theme() {
    if (localStorage.getItem('dark-mode') === 'true') {
        document.body.classList.remove('light')
        theme_btn.innerHTML = '<i class="fas fa-sun sun-hide text-info fs-3" role="button"></i>'
    }
    else {
        document.body.classList.add('light')
        theme_btn.innerHTML = '<i class="fas fa-moon moon-hide text-dark fs-3" role="button"></i>'
    }
}


theme_btn.addEventListener('click', () => {
    if (localStorage.getItem('dark-mode') === 'false') {
        localStorage.setItem("dark-mode", "true");
    }
    else {
        localStorage.setItem("dark-mode", "false");
    }
    theme()
})

var navToggler = document.querySelector('#nav-toggler-btn')
navToggler.addEventListener('click', () => {
    document.body.classList.toggle('sidebar-icon-only')
})
