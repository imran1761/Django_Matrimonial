$(function() {
    var ink, d, x, y;
    $(".ripplelink").click(function(e) {
        if ($(this).find(".ink").length === 0) {
            $(this).prepend("<span class='ink'></span>");
        }

        ink = $(this).find(".ink");
        ink.removeClass("animate");

        if (!ink.height() && !ink.width()) {
            d = Math.max($(this).outerWidth(), $(this).outerHeight());
            ink.css({
                height: d,
                width: d
            });
        }

        x = e.pageX - $(this).offset().left - ink.width() / 2;
        y = e.pageY - $(this).offset().top - ink.height() / 2;

        ink.css({
            top: y + 'px',
            left: x + 'px'
        }).addClass("animate");
    });
});
$('[data-toggle="tooltip"]').tooltip({
    trigger: 'hover',
    'placement': 'top'
});

$(document).ready(function() {
    $("#headerlogin").click(function() {
        $("#headerloginForm").validate({
            rules: {
                username: {
                    required: true
                },
                password: {
                    required: true
                }
            },
            // Specify the validation error messages
            messages: {
                username: {
                    required: "Please enter Your name.",
                },
                password: {
                    required: "Please enter Your Password.",
                }
            },
            submitHandler: function(form) {
                form.submit();
            }

        });
    });

});