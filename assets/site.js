(() => {
  const header = document.querySelector('header');
  const menu = document.querySelector('.header-menu');
  const toggles = [...document.querySelectorAll('.header-burger button, button.header-burger-btn')];
  function setMenu(open) {
    document.body.classList.toggle('header--menu-open', open);
    document.body.classList.toggle('migration-menu-open', open);
    toggles.forEach(button => {
      button.setAttribute('aria-expanded', String(open));
      button.setAttribute('aria-label', open ? 'Stäng menyn' : 'Öppna menyn');
    });
    if (menu) { menu.inert = !open; menu.setAttribute('aria-hidden', String(!open)); }
    if(open) menu?.querySelector('a')?.focus();
  }
  toggles.forEach(button => button.addEventListener('click', () => setMenu(!document.body.classList.contains('migration-menu-open'))));
  document.addEventListener('keydown', e => { if(e.key === 'Escape') {setMenu(false); toggles[0]?.focus();} });
  menu?.addEventListener('click',e => {if(e.target.closest('a')) setMenu(false);});
  setMenu(false);
  const updateHeader = () => document.documentElement.style.setProperty('--header-height', `${header?.getBoundingClientRect().height || 104}px`);
  updateHeader(); window.addEventListener('resize', updateHeader);
  document.querySelectorAll('img').forEach(img => img.addEventListener('load',updateHeader,{once:true}));
  document.querySelectorAll('.contact-form').forEach(form => form.addEventListener('submit', e => {
    e.preventDefault();
    const status = form.querySelector('.form-status');
    status.textContent = 'Meddelandet har inte skickats. Formuläret är ännu inte anslutet. Kontakta mig via LinkedIn.';
    status.tabIndex = -1; status.focus();
  }));
})();
