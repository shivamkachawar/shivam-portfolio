(() => {
  const toggle = document.getElementById('menuToggle');
  const nav = document.getElementById('nav');
  toggle?.addEventListener('click', () => nav.classList.toggle('open'));
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => nav.classList.remove('open')));

  const items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    items.forEach(item => observer.observe(item));
  } else {
    items.forEach(item => item.classList.add('visible'));
  }
})();