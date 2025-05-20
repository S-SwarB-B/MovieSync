document.addEventListener('DOMContentLoaded', function() {
    // Элементы управления
    const loginBtn = document.querySelector('.btn-login');
    const registerBtn = document.querySelector('.btn-register');
    const profileBtn = document.querySelector('.btn-profile');
    const closeButtons = document.querySelectorAll('.close-modal');
    const loginModal = document.querySelector('.login-modal');
    const registerModal = document.querySelector('.register-modal');

    // Показать/скрыть модальные окна
    function showModal(modal) {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden'; // Блокируем прокрутку фона
    }

    function hideModal(modal) {
        modal.style.display = 'none';
        document.body.style.overflow = ''; // Восстанавливаем прокрутку
    }

    // Показать модальное окно входа
    loginBtn.addEventListener('click', function() {
        showModal(loginModal);
    });

    // Показать модальное окно регистрации
    registerBtn.addEventListener('click', function() {
        showModal(registerModal);
    });

    // Закрыть модальные окна
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modal = this.closest('.auth-modal');
            hideModal(modal);
        });
    });

    // Закрыть при клике вне окна
    window.addEventListener('click', function(event) {
        if (event.target === loginModal) {
            hideModal(loginModal);
        }
        if (event.target === registerModal) {
            hideModal(registerModal);
        }
    });

    // Закрыть при нажатии Escape
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            hideModal(loginModal);
            hideModal(registerModal);
        }
    });

    // === ПОДСВЕТКА ТЕКУЩЕЙ ВКЛАДКИ И СБРОС ДРУГИХ ===
    const navLinks = document.querySelectorAll('.sidebar a');
    const currentPage = window.location.pathname.split('/').pop();

    navLinks.forEach(link => {
        const li = link.closest('li');
        // Удаляем класс active у всех
        li.classList.remove('active');
    
        // Добавляем класс только если ссылка совпадает с текущей страницей
        if (link.getAttribute('href') === currentPage) {
            li.classList.add('active');
        }
    });
});

