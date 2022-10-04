function counter(element){
    var target = element.parentElement.querySelector(".start");
    var toNum = parseFloat(target.innerText);
    target.innerText = toNum + 1;
}