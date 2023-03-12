$(document).ready(function() {
    let anim = true;
    $('.contentAnswers button').each(function() {
        $(this).on('click', function(e) {
            if (anim == true)
                $(this).addClass("scale-out-center");
                anim = false;
        });
    });

    setTimeout(() => {
        $('.homePageInfo').addClass('slide-in-bck-center');
        setTimeout(() => {
            $('.quizStart').addClass('wobble-hor-bottom');
        }, 500);
    }, 1000);
})