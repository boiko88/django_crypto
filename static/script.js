



document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".carousel");
    const images = document.querySelectorAll(".carousel-img");
    const dots = document.querySelectorAll(".dot");
  
    let currentIndex = 0;
    const slideCount = images.length;
    const intervalTime = 3000;
    let autoScroll;
  
    function setActiveSlide(index) {
      images.forEach(img => img.classList.remove("active"));
      images[index].classList.add("active");
  
      dots.forEach(dot => dot.classList.remove("active"));
      dots[index].classList.add("active");
  
      currentIndex = index;
    }
  
    function scrollToSlide(index) {
      images[index].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
      setActiveSlide(index);
    }
  
    // Клик по точкам
    dots.forEach((dot, index) => {
      dot.addEventListener("click", () => {
        scrollToSlide(index);
        resetAutoScroll();
      });
    });
  
    // Автопрокрутка
    function startAutoScroll() {
      autoScroll = setInterval(() => {
        let nextIndex = (currentIndex + 1) % slideCount;
        scrollToSlide(nextIndex);
      }, intervalTime);
    }
  
    function stopAutoScroll() {
      clearInterval(autoScroll);
    }
  
    function resetAutoScroll() {
      stopAutoScroll();
      startAutoScroll();
    }
  
    // Обработка ручной прокрутки (тачпад/мышь)
    let isScrolling;
    carousel.addEventListener("scroll", () => {
      clearTimeout(isScrolling);
  
      isScrolling = setTimeout(() => {
        const scrollLeft = carousel.scrollLeft;
        let closestIndex = 0;
        let closestDistance = Infinity;
  
        images.forEach((img, i) => {
          const imgLeft = img.offsetLeft;
          const distance = Math.abs(scrollLeft - imgLeft);
          if (distance < closestDistance) {
            closestDistance = distance;
            closestIndex = i;
          }
        });
  
        setActiveSlide(closestIndex);
        resetAutoScroll();
      }, 100);
    });
  
    // Пауза автопрокрутки при наведении мыши
    carousel.addEventListener("mouseenter", () => {
      stopAutoScroll();
    });
  
    // Возобновление автопрокрутки при уходе мыши
    carousel.addEventListener("mouseleave", () => {
      resetAutoScroll();
    });
  
    // Инициализация
    setActiveSlide(0);
    startAutoScroll();
  });
  

  