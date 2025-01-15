const form = document.getElementById('form');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    const jdata = {};
    formData.forEach((value, key) => {jdata[key] = value});
    console.log(jdata);

    fetch('/submit', { 
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(jdata),
    }).then(response => response.text()).then(data => {
      // Handle the response from Flask
      console.log(data);
      window.location.href = data+"?"+"email"+"="+jdata['emailId'];
    }).catch((error) => {
      console.error('Error:', error);
    });
});
