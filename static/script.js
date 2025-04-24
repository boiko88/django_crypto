const carousel = document.querySelector('.carousel');
let scrollAmount = 550;
let delay = 3000;

// Функция для прокрутки
function scrollCarousel() {
  carousel.scrollBy({
    left: scrollAmount,
    behavior: 'smooth',
  });

  if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 10) {
    carousel.scrollTo({ left: 0, behavior: 'smooth' });
  }
}

// Запуск автопрокрутки
let autoScroll = setInterval(scrollCarousel, delay);

// При наведении — остановка
carousel.addEventListener('mouseenter', () => {
  clearInterval(autoScroll); // ⛔ Останавливаем таймер
});

// При уходе мышки — снова запускаем
carousel.addEventListener('mouseleave', () => {
  autoScroll = setInterval(scrollCarousel, delay); // ▶️ Запускаем снова
});

