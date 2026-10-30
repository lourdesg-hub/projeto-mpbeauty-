
document.addEventListener("DOMContentLoaded", function () {

    // Menu mobile
    const menuButton = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".nav-links");

    if (menuButton && menu) {
        menuButton.addEventListener("click", function () {
            menu.classList.toggle("active");
        });
    }

    // Fechar menu ao clicar em um link
    const menuLinks = document.querySelectorAll(".nav-links a");

    menuLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            if (menu) {
                menu.classList.remove("active");
            }
        });
    });

    // Confirmação antes de cancelar um agendamento
    const cancelButtons = document.querySelectorAll(".cancel-appointment");

    cancelButtons.forEach(function (button) {
        button.addEventListener("click", function (event) {
            const confirmar = confirm(
                "Tem certeza de que deseja cancelar este agendamento?"
            );

            if (!confirmar) {
                event.preventDefault();
            }
        });
    });

    // Atualizar ano do rodapé
    const yearElement = document.querySelector("#current-year");

    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }

});
