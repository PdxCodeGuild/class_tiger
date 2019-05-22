/*

Toggle switch for Dark mode functionality

*/


const toggleSwitch = document.querySelector('#checkbox');
const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
const themeText = document.getElementById('theme-text');

function switchTheme(e) {
  if (e.target.checked) {
    document.documentElement.setAttribute('data-theme','dark');
    localStorage.setItem('theme','dark');
    themeText.innerText = 'DARK MODE';
  } else {
    document.documentElement.setAttribute('data-theme','light');
    localStorage.setItem('theme','light')
    themeText.innerText = 'LIGHT MODE';
  }
}

if (currentTheme) {
  document.documentElement.setAttribute('data-theme',currentTheme);

  if(currentTheme === 'dark'){
    toggleSwitch.checked = true;
    themeText.innerText = 'DARK MODE';

  } else {
    themeText.innerText = 'LIGHT MODE';
  }
}
toggleSwitch.addEventListener('change', switchTheme, false);
