const carousel = document.querySelector('.carousel');
const prevBtn = document.querySelector('.carousel-prev-btn');
const nextBtn = document.querySelector('.carousel-next-btn');

prevBtn.addEventListener('click', () => {
  carousel.scrollBy({
    left: -130,
  });
});

nextBtn.addEventListener('click', () => {
  carousel.scrollBy({
    left: 130,
  });
});


 alert('ALOHA ALOHA ALOHA');
