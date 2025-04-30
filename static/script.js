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
