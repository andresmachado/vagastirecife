$(document).ready(function(){
    $("header nav ul").addClass('open');

    $(".mobile-btn").on("click", function(){
        $("header nav ul").slideToggle('slow', function(){
            $(this).toggleClass("open");
        });
    });
});