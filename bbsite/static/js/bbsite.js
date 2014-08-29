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
	/*
	$('#load-more-ifo').click(function(event) {
		
		var offset = 8;
		var limit = 4;
		var csrftoken = getCookie('csrftoken');

		console.log(csrftoken);

		function csrfSafeMethod(method) {
    		// these HTTP methods do not require CSRF protection
    		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}

		$.ajaxSetup({
			crossDomain: false,
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});

		$.ajax({
			url: 'informations',
			type: 'POST',
			dataType: "json",
			data: {offset: offset, limit: limit},
			
			success:function(response){
					 var json_response = JSON.parse(response);
				    // now get the variables from the json_response
				    alert(json_response);
			},
    		complete:function(){},
    		error:function (xhr, textStatus, thrownError){
        		alert("error doing something");
    		}
		});
	});*/
});
/*
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}*/

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



