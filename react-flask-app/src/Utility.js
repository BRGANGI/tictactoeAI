export function fadeOut(id) {
    var element = document.getElementById(id);
    var newOpacity = 1;
    var timer = setInterval(function () {
        if (newOpacity <= 0.1){
            clearInterval(timer);
            element.style.display = 'none';
        }
        element.style.opacity = newOpacity;
        element.style.filter = 'alpha(opacity=' + newOpacity * 100 + ")";
        newOpacity -= newOpacity * 0.1;
    }, 50);
  }

  export function fadeIn(id) {
    var element = document.getElementById(id);
    var newOpacity = 0;
    element.style.display = 'block'; 
    var timer = setInterval(function () {
        if (newOpacity >= 1){
            clearInterval(timer);
        }
        element.style.opacity = newOpacity;
        element.style.filter = 'alpha(opacity=' + newOpacity * 100 + ")";
        newOpacity += 0.1; 
    }, 50);
}