
document.addEventListener("DOMContentLoaded", function () {
    const images = document.querySelectorAll(".carousel-img");
    const dots = document.querySelectorAll(".dot");

    dots.forEach(dot => {
        dot.addEventListener("click", () => {
            const index = parseInt(dot.getAttribute("data-index"));

            // Показ нужного изображения
            images.forEach(img => img.classList.remove("active"));
            images[index].classList.add("active");

            // Обновление стилей точек
            dots.forEach(d => d.classList.remove("active"));
            dot.classList.add("active");
        });
    });

    // Устанавливаем первую картинку активной по умолчанию
    images[0].classList.add("active");
    dots[0].classList.add("active");
});
