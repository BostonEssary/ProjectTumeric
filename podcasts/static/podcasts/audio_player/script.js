function changeButtonState(elem){
    var button = document.getElementsByTagName('button');
    for (i = 0; i < button.length; i++){
        button[i].classList.remove('active-button')
    }
    
    elem.classList.add('active-button');
}