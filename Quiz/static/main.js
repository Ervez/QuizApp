$(document).ready(function() {
    let anim = true;
    $('.contentAnswers button').each(function() {
        $(this).on('click', function(e) {
            if (anim == true)
                $(this).addClass("scale-out-center");
                anim = false;
        });
    });
})