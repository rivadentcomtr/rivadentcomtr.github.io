const url = $('#system-url').data('url');


$(window).on("load", function () {

    $(function () {
        recaptcha();
        setInterval(function () {
            recaptcha();
        }, 10000);
    })

    function recaptcha() {
        grecaptcha.ready(function () {
            grecaptcha.execute($('#secret-key').attr('data-key'), {
                action: 'validate_captcha'
            })
                .then(function (token) {
                    $('input[name="g-recaptcha"]').val(token)
                });
        });
    }

});


$(function () {


    $(document).on("submit", "#infoContact", function (event) {
        event.preventDefault();
        var btn = $(this).find('button[type="submit"]');
        btn.attr('disabled', true);
        var serialized = $(this).serializeArray();
        serialized.push({
            name: 'csrf',
            value: Cookies.get('csrf_token')
        });
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: serialized,
            url: url + 'Ajax/contact_message',
            success: function (result) {
                if (result.status === true) {
                    Swal.fire({
                        title: result.success,
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: false,
                        allowOutsideClick: false
                    });
                    setTimeout(
                        function () {
                            window.location.reload()
                        }, 2000);
                } else {
                    btn.attr('disabled', false);
                    Swal.fire({
                        title: $('#form-error-text').data('text'),
                        icon: 'warning',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                        html: result.error
                    });
                }
            },
            error: function () {
                btn.attr('disabled', false);
                Swal.fire({
                    title: $('#server-error').data('text'),
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    });

    $(document).on("submit", "#infoQuestion", function (event) {
        event.preventDefault();
        var btn = $(this).find('button[type="submit"]');
        btn.attr('disabled', true);
        var serialized = $(this).serializeArray();
        serialized.push({
            name: 'csrf',
            value: Cookies.get('csrf_token')
        });
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: serialized,
            url: url + 'Ajax/fast_question',
            success: function (result) {
                if (result.status === true) {
                    Swal.fire({
                        title: result.success,
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: false,
                        allowOutsideClick: false
                    });
                    setTimeout(
                        function () {
                            window.location.reload()
                        }, 2000);
                } else {
                    btn.attr('disabled', false);
                    Swal.fire({
                        title: $('#form-error-text').data('text'),
                        icon: 'warning',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                        html: result.error
                    });
                }
            },
            error: function () {
                btn.attr('disabled', false);
                Swal.fire({
                    title: $('#server-error').data('text'),
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    });

    var chat = [];
    $('.live-support-chat-item').on('change', '.live-support-question', function () {
        $('.live-support-question-area').find('input').prop('disabled', true);
        var slug = $('#slug').val();
        var id = $(this).val();
        var name = $('#user-1').val();
        chat.push(id);
        var data = [
            {
                name: 'csrf',
                value: Cookies.get('csrf_token')
            }, {
                name: 'id',
                value: id
            }, {
                name: 'name',
                value: name
            }, {
                name: 'slug',
                value: slug
            }]
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: data,
            url: url + 'Live_support/livesupport',
            success: function (result) {
                if (result.status === true) {
                    if (result.data.question_reply.question) {
                        $('.live-support-question-area').remove()
                        $('.live-support-chat-item > ul').append(result.question)
                    }
                    if (result.data.question_reply.reply) {
                        $('.live-support-chat-item > ul').append(result.wait)

                        $('.live-support-chat-item').animate({
                            scrollTop: $('.live-support-chat-item')[0].scrollHeight
                        }, 0);

                        setTimeout(function () {
                            $('.live-support-chat-left.wait').remove();

                            $('.live-support-chat-item > ul').append(result.reply);
                            $('.live-support-chat-item > ul').append(result.whatsap);

                            $('.live-support-chat-item').animate({
                                scrollTop: $('.live-support-chat-item')[0].scrollHeight
                            }, 0);
                        }, 1000); // 50 saniye

                    }
                    var arr = [];
                    setTimeout(function () {
                        if (result.data.short_question) {
                            $('.live-support-chat-item > ul').append(result.short_question);

                            $('.live-support-chat-item').animate({
                                scrollTop: $('.live-support-chat-item')[0].scrollHeight
                            }, 0);
                        }
                    }, 1000)
                } else {
                    Swal.fire({
                        title: result.error,
                        icon: 'error',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: false,
                        allowOutsideClick: false
                    });
                }
            },
            error: function () {
                Swal.fire({
                    title: 'Bağlantı Hatası.',
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    })

    $('.live-support-chat-item').on('click', '#user_add_live_chat', function (event) {
        event.preventDefault();
        chat = JSON.stringify(chat)
        var policlinic_id = $('.live-support-chat-area').attr('data-policlinic');
        var link = $(this).attr('href');
        var name = $('#user-1').val();
        var data = [
            {
                name: 'csrf',
                value: Cookies.get('csrf_token')
            }, {
                name: 'policlinic_id',
                value: policlinic_id
            }, {
                name: 'livesupport_id',
                value: chat
            }, {
                name: 'name',
                value: name
            }]
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: data,
            url: url + 'Live_support/livesupport_add',
            success: function (result) {
                if (result.status === true) {
                    $('#user_add_live_chat').css('pointer-events', 'none');
                    window.open(link, "_blank");
                } else {
                    Swal.fire({
                        title: result.error,
                        icon: 'error',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        allowOutsideClick: false
                    });
                }
            },
            error: function () {
                Swal.fire({
                    title: 'Bağlantı Hatası.',
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    })

    $(document).on("submit", "#infoComment", function (event) {
        event.preventDefault();
        var btn = $(this).find('button[type="submit"]');
        btn.attr('disabled', true);
        var serialized = $(this).serializeArray();
        serialized.push({
            name: 'csrf',
            value: Cookies.get('csrf_token')
        });
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: serialized,
            url: url + 'Ajax/send_comment',
            success: function (result) {
                if (result.status === true) {
                    Swal.fire({
                        title: result.success,
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: false,
                        allowOutsideClick: false
                    });
                    setTimeout(
                        function () {
                            window.location.reload()
                        }, 2000);
                } else {
                    btn.attr('disabled', false);
                    Swal.fire({
                        title: $('#form-error-text').data('text'),
                        icon: 'warning',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                        html: result.error
                    });
                }
            },
            error: function () {
                btn.attr('disabled', false);
                Swal.fire({
                    title: $('#server-error').data('text'),
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    });

    $('.policlinic_select').on("change", function (event) {
        let policlinic_id = $(this).val();
        let data = [
            {
                name: 'csrf',
                value: Cookies.get('csrf_token')
            }, {
                name: 'policlinic_id',
                value: policlinic_id
            }
        ];
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: data,
            url: url + 'Ajax/get_team',
            success: function (result) {
                if (result.status === true) {
                    let selected = $('#team_select option:first')[0].outerHTML;
                    $('#team_select').html("")
                    var arr = []
                    $.each(result.team, function (index, val) {
                        arr += selected
                        arr += '<option value="' + val.id + '">' + val.title + '</option>'
                    })
                    $('#team_select').html(arr)
                } else {
                    let selected = $('#team_select option:first')[0].outerHTML;
                    $('#team_select').html(selected)
                }
            },
            error: function () {
                Swal.fire({
                    title: $('#server-error').data('text'),
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    })

    $(document).on("submit", "#infoMeeting", function (event) {
        event.preventDefault();
        var btn = $(this).find('button[type="submit"]');
        btn.attr('disabled', true);
        var serialized = $(this).serializeArray();
        serialized.push({
            name: 'csrf',
            value: Cookies.get('csrf_token')
        });
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: serialized,
            url: url + 'Ajax/create_appointment',
            success: function (result) {
                if (result.status === true) {
                    Swal.fire({
                        title: result.success,
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: false,
                        allowOutsideClick: false
                    });
                    setTimeout(
                        function () {
                            window.location.reload()
                        }, 2000);
                } else {
                    btn.attr('disabled', false);
                    Swal.fire({
                        title: $('#form-error-text').data('text'),
                        icon: 'warning',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                        html: result.error
                    });
                }
            },
            error: function () {
                btn.attr('disabled', false);
                Swal.fire({
                    title: $('#server-error').data('text'),
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    });

});