$(document).ready(function () {
	var len = $(".topleft").width();
	$(".topleft, .topright, .bottomleft, .bottomright")
		.css("height", len);
	var wwidth = $(window).width();
	var wheight = $(window).height();
	$(".topleft, .bottomleft").css("left", wwidth/2);
	$(".topright, .bottomright").css("left", wwidth/2);
	$(".topleft, .topright").css("top", wheight/2);
	$(".bottomleft, .bottomright").css("top", wwidth/2);
});