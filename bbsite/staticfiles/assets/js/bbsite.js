$(document).ready(function() {
	$(".information-text").dotdotdot({
		ellipsis	: '... ',
		watch		: true
	});

	$(".news-text").dotdotdot({
		ellipsis	: '... ',
		watch		: true
	});

	var $imgs = $(".header-slide").find("img");

	i = 0;

	function changeImage() {
	    var next = (++i % $imgs.length);
	    $($imgs.get(next - 1)).fadeOut(500);
	    $($imgs.get(next)).fadeIn(500);
	}

	/*var interval = setInterval(changeImage, 2000);*/
});
