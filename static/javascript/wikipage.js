$(document).ready(function () {
    $(".button").height("50px")
    .width("50px")
	.addClass("rotated2")
	.hover(
		function () {
			$(this).toggleClass("rotated");
			$(this).toggleClass("rotated2");
		}
	);
    $(window).resize(function () {
        $(".button").height(function () {
            return $(this).width();
        })
    });
});
