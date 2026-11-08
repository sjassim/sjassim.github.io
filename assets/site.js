/* Mobile menu only; the portfolio needs no framework or Squarespace runtime. */
(() => {
  const header = document.querySelector('.site-header');
  const button = document.querySelector('.menu-toggle');
  const menu = document.querySelector('.mobile-menu');
  if (!header || !button || !menu) return;

  function setMenu(open, returnFocus = false) {
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Stäng menyn' : 'Öppna menyn');
    menu.hidden = !open;
    document.body.classList.toggle('menu-open', open);
    if (open) menu.querySelector('a')?.focus();
    else if (returnFocus) button.focus();
  }
  button.addEventListener('click', () => setMenu(menu.hidden));
  menu.addEventListener('click', event => {
    if (event.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', event => {
    if (menu.hidden) return;
    if (event.key === 'Escape') setMenu(false, true);
    if (event.key === 'Tab') {
      const controls = [button, ...menu.querySelectorAll('a')];
      const index = controls.indexOf(document.activeElement);
      if (event.shiftKey && index === 0) { event.preventDefault(); controls.at(-1).focus(); }
      else if (!event.shiftKey && index === controls.length - 1) { event.preventDefault(); button.focus(); }
    }
  });
  const updateHeader = () => {
    document.documentElement.style.setProperty('--header-height', `${header.offsetHeight}px`);
    if (window.matchMedia('(min-width: 768px)').matches) setMenu(false);
  };
  updateHeader();
  window.addEventListener('resize', updateHeader);
})();
