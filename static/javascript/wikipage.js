$(document).ready(function () {
	$(".button").css(
		"height", 
		$(".button").width()
	)
	.addClass("rotated2")
	.hover(
		function () {
			$(this).toggleClass("rotated");
			$(this).toggleClass("rotated2");
		}
	);
});