(() => {
  const root = document.documentElement;
  const theme = document.getElementById('theme-toggle');
  const menu = document.getElementById('menu-toggle');
  const navigation = document.getElementById('navigation');
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  let preference = null;
  try { preference = localStorage.getItem('theme'); } catch { /* Private storage can be unavailable. */ }
  function applyTheme(value) {
    root.dataset.theme = value;
    theme.setAttribute('aria-label', value === 'dark' ? 'Use light appearance' : 'Use dark appearance');
    theme.setAttribute('aria-pressed', String(value === 'dark'));
  }
  applyTheme(preference === 'dark' || preference === 'light' ? preference : media.matches ? 'dark' : 'light');
  theme.addEventListener('click', () => {
    preference = root.dataset.theme === 'dark' ? 'light' : 'dark';
    applyTheme(preference);
    try { localStorage.setItem('theme', preference); } catch { /* The chosen appearance still works for this page. */ }
  });
  media.addEventListener('change', event => { if (!preference) applyTheme(event.matches ? 'dark' : 'light'); });
  function closeMenu() { navigation.dataset.open = 'false'; menu.setAttribute('aria-expanded', 'false'); menu.textContent = 'Menu'; }
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    navigation.dataset.open = String(open); menu.setAttribute('aria-expanded', String(open)); menu.textContent = open ? 'Close' : 'Menu';
  });
  navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { closeMenu(); menu.focus(); } });
  document.addEventListener('click', event => { if (!event.target.closest('.nav')) closeMenu(); });
  window.matchMedia('(min-width: 761px)').addEventListener('change', closeMenu);
  document.querySelector('[data-year]').textContent = String(new Date().getFullYear());
})();
