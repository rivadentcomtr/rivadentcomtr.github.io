$(document).ready(function() {

    $('.reply-btn').click(function() {
        var id = $(this).data('reply-target');
        $(id).toggleClass('d-none');
    });

});