export function fadeOut(id) {
    return new Promise((resolve) => {
        var element = document.getElementById(id);
        var newOpacity = 1;
        var timer = setInterval(function () {
            if (newOpacity <= 0.1) {
                console.log(newOpacity)
                clearInterval(timer);
                element.style.display = 'none';
                resolve(); 
            }
            element.style.opacity = newOpacity;
            element.style.filter = 'alpha(opacity=' + newOpacity * 100 + ")";
            newOpacity -= newOpacity * 0.1;
        }, 50);
    });
}

export function fadeIn(id) {
    console.log(id)
    return new Promise((resolve) => {
        var element = document.getElementById(id);
        var newOpacity = 0;
        element.style.display = 'block';
        var timer = setInterval(function () {
            console.log(newOpacity)
            if (newOpacity >= 1) {
                clearInterval(timer);
                resolve(); 
            }
            element.style.opacity = newOpacity;
            element.style.filter = 'alpha(opacity=' + newOpacity * 100 + ")";
            newOpacity += 0.1;
        }, 50);
    });
}

export const symbols = {
    'X': 'O',
    'O': 'X'
  }