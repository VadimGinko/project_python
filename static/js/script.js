function swa(){
    var b = document.getElementById('overlay');
	b.style.visibility = 'visible';
	b.style.opacity = '1';
	b.style.transition = 'all 0.7s ease-out 0s';
}

function swa2(){
    var b = document.getElementById('overlay');
	b.style.visibility = 'hidden';
	b.style.opacity = '0';
}

$(document).ready(function(){
$("a[href*=#]").on("click", function(e){
var anchor = $(this);
$('html, body').stop().animate({
scrollTop: $(anchor.attr('href')).offset().top
}, 777);
e.preventDefault();
return false;
});
});