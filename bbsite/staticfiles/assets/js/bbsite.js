$(document).ready(function() {
	$(".information-text").dotdotdot({
		ellipsis	: '... ',
		watch		: true
	});

	$(".news-text").dotdotdot({
		ellipsis	: '... ',
		watch		: true
	});

	$(".all-news-text").dotdotdot({
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
	$('#test').weatherfeed(['532456'], {
		woeid: true,
		link: false
	});

	/*var interval = setInterval(changeImage, 2000);*/
});

$(function() {
	$('#load-more-info').click(function() {
		var defaultOffset = $(".information-box").children().length - 2;
		var offset = $("#loaded-informations").children().length + defaultOffset;
		var limit = 4;

		$.ajax({
			url: 'informations',
			type: 'POST',
			dataType: 'html',
			data: { 
				offset: offset, 
				limit: limit,
				csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
			},
			success: function(data) {
			    $(data).appendTo('#loaded-informations');

			    if ($(".hideLinkMoreInfo").val() == "hide") {
			    	$(".load-information").remove();
			    }
			}
		});
	});
});

$(document).ready(function(){
  $('.bxslider').bxSlider();
});



