document.addEventListener("DOMContentLoaded", function () {
  const carousel = document.querySelector('.carousel');
  const dots = document.querySelectorAll('.dot');
  const slides = document.querySelectorAll('.carousel-img');
  const delay = 3000;

  const getSlideWidth = () => slides[0].getBoundingClientRect().width;

  // 👉 Функция обновления активной точки
  function updateDots(index) {
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });
  }

  // 👉 Прокрутка карусели автоматически
  function scrollCarousel() {
    const slideWidth = getSlideWidth();
    const nextScrollLeft = carousel.scrollLeft + slideWidth;

    if (nextScrollLeft + carousel.clientWidth >= carousel.scrollWidth) {
      carousel.scrollTo({ left: 0, behavior: 'smooth' });
      updateDots(0);
    } else {
      carousel.scrollBy({ left: slideWidth, behavior: 'smooth' });
      const index = Math.round((carousel.scrollLeft + slideWidth) / slideWidth);
      updateDots(index);
    }
  }

  // 👉 Таймер автопрокрутки
  let autoScroll = setInterval(scrollCarousel, delay);

  // 👉 Остановка автопрокрутки при наведении
  carousel.addEventListener('mouseenter', () => clearInterval(autoScroll));
  carousel.addEventListener('mouseleave', () => {
    autoScroll = setInterval(scrollCarousel, delay);
  });


  // 👉 Обработка клика по точкам
  dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      const slideWidth = getSlideWidth();
      carousel.scrollTo({
        left: index * slideWidth,
        behavior: 'smooth'
      });
      updateDots(index);
    });
  });

  // 👉 Обработка прокрутки мышью/пальцем — обновление точек
  carousel.addEventListener('scroll', () => {
    const slideWidth = getSlideWidth();
    const index = Math.round(carousel.scrollLeft / slideWidth);
    updateDots(index);
  });
});

const carousel = document.querySelector('.carousel');
let scrollAmount = 550;
let delay = 3000;

// Scroll function
function scrollCarousel() {
  carousel.scrollBy({
    left: scrollAmount,
    behavior: 'smooth',
  });

  if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 10) {
    carousel.scrollTo({ left: 0, behavior: 'smooth' });
  }
}

// Auto scroll function
let autoScroll = setInterval(scrollCarousel, delay);

// Stop wile hovering
carousel.addEventListener('mouseenter', () => {
  clearInterval(autoScroll); // ⛔ Stop timer
});

// Continues while no hovering
carousel.addEventListener('mouseleave', () => {
  autoScroll = setInterval(scrollCarousel, delay); // ▶️ start again
});


let currentIndex = 0;

function currentSlide(n) {
  const slides = document.querySelectorAll('.carousel-img');
  const dots = document.querySelectorAll('.dot');

  slides.forEach(slide => slide.classList.remove('active'));
  dots.forEach(dot => dot.classList.remove('active'));

  slides[n-1].classList.add('active');
  dots[n-1].classList.add('active');

  // Чтобы слайды двигались: можно добавить анимацию через transform
  document.querySelector('.slides').style.transform = `translateX(-${(n-1) * 100}%)`;
}
