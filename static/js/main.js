const mapBTN = document.getElementById('maps');
const adminBTN = document.getElementById('admin');


mapBTN.addEventListener('click', (event) => {
    window.location.href = '/maps';
});

adminBTN.addEventListener('click', (event) => {
  window.location.href = '/admin';
});