function setThemeToLight() {
    document.querySelector('header').style.backgroundColor = 'lightgray';
    document.querySelector('.bton').style.backgroundColor = 'black';
    const keke = document.querySelectorAll('a');
    for (let i = 0; i < keke.length; i++) {
        keke[i].style.color = 'black';
    }
    document.getElementById('logotype').innerHTML = '<img class="logo" src="images/logoblack.png" alt="logo"/>';
}
function setThemeToDark() {
    document.querySelector('header').style.backgroundColor = '#24252A';
    document.querySelector('.bton').style.backgroundColor = 'rgba(0, 136, 169, 1)';
    const keke = document.querySelectorAll('a');
    for (let i = 0; i < keke.length; i++) {
        keke[i].style.color = '#edf0f1';
    }
    document.getElementById('logotype').innerHTML = '<img class="logo" src="images/logo.png" alt="logo"/>';
}

