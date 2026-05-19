(function ($) {
    $(document).on("submit", "#infoAbout", function (event) {
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
            url: url + 'About/about_ajax',
            success: function (result) {
                if (result.status === true) {
                    Swal.fire({
                        title: 'Güncelleme Başarılı!',
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                    });
                    setTimeout(
                        function () {
                            window.location.reload();
                        }, 1000);
                } else {
                    btn.attr('disabled', false);
                    Swal.fire({
                        title: 'Başarısız',
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
                    title: 'Bağlantı Hatası.',
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    });
    $(document).on("change", '.show-hide', function (event) {
        var id = $(this).data("id");
        if ($(this).prop('checked')) {
            var status = 1;
        } else {
            var status = 0;
        }
        var data = [
            {
                name: 'csrf',
                value: Cookies.get('csrf_token')
            }, {
                name: 'status',
                value: status
            }, {
                name: 'id',
                value: id
            }]
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: data,
            url: url + 'About/image_status',
            success: function (result) {
                if (result.status === true && status == 0) {
                    Swal.fire({
                        title: 'Artık Sitede Görünmeyecek.',
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                    });
                } else if (result.status === true && status == 1) {
                    Swal.fire({
                        title: 'Artık Sitede Görünecek.',
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                    });
                } else {
                    Swal.fire({
                        title: 'Başarısız',
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
    $('.gallery-img-delete').jConfirm().on('confirm', function (e) {
        var id = $(this).data("id");
        var data = [
            {
                name: 'csrf',
                value: Cookies.get('csrf_token')
            }, {
                name: 'id',
                value: id
            }]

        $.ajax({
            method: 'post',
            dataType: 'json',
            data: data,
            url: url + 'About/delete_images',
            success: function (result) {
                if (result.status === true) {
                    $('#del-' + id).remove();
                    Swal.fire({
                        title: 'Silindi.',
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                    });
                } else {
                    Swal.fire({
                        title: 'Başarısız',
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
                Swal.fire({
                    title: 'Bağlantı Hatası.',
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });

    });
    $('.change-images-position_sp').sortable({
        update: function (event, ui) {
            $(this).children().each(function (index) {
                if ($(this).attr('data-position') != (index + 1)) {
                    $(this).attr('data-position', (index + 1)).addClass('updated');
                }
            });
            saveNewPositions2()
        }
    });

    function saveNewPositions2() {
        var positions = [];
        var data = [];

        $('.updated').each(function () {
            positions.push([$(this).attr('data-index'), $(this).attr('data-position')]);
            $(this).removeClass('updated');
        });

        $.ajax({
            method: 'post',
            dataType: 'json',
            data: {
                positions: positions,
                csrf: Cookies.get('csrf_token')
            },
            url: url + 'About/update_position_images',
            success: function (result) {
                window.location.reload();
            },
            error: function () {
                window.location.reload();
            }
        });
    }
})(jQuery);


