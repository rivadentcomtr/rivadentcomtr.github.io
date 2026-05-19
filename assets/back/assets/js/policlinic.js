(function ($) {

    $(document).on("submit", "#infoPoliclinicAdd", function (event) {
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
            url: url + 'Policlinic/add_ajax',
            success: function (result) {
                if (result.status === true) {
                    Swal.fire({
                        title: 'Ekleme Başarılı!',
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

    $(document).on("submit", "#infoPoliclinicUpdate", function (event) {
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
            url: url + 'Policlinic/update_ajax',
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
            url: url + 'Policlinic/image_status',
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

    $(".policlinic-status").change(function () {
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
            url: url + 'Policlinic/status',
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
    });

    $(".delete-policlinic").jConfirm().on('confirm', function (e) {
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
            url: url + 'Policlinic/delete',
            success: function (result) {
                if (result.status === true) {
                    $('#delete' + id).remove();
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

    $('.change-position_sp').sortable({
        update: function (event, ui) {
            $(this).children().each(function (index) {
                if ($(this).attr('data-position') != (index + 1)) {
                    $(this).attr('data-position', (index + 1)).addClass('updated');
                }
            });
            saveNewPositions()
        }
    });

    function saveNewPositions() {
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
            url: url + 'Policlinic/update_position',
            success: function (result) {
                window.location.reload();
            },
            error: function () {
                window.location.reload();
            }
        });
    }

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
            url: url + 'Policlinic/update_position_images',
            success: function (result) {
                window.location.reload();
            },
            error: function () {
                window.location.reload();
            }
        });
    }


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
            url: url + 'Policlinic/delete_images',
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

    $('.for-blue-input').on('input', function () {
        var text = $(this).val();
        var name = $(this).attr('name');
        var target = $(this).closest('.form-group').find('.blue-item')
        var splitText = text.split(' ');
        var arr = [];
        $.each(splitText, function (index, value) {
            if (value != '') {
                arr += ('<span class="text-blue-area"><input type="radio" id="' + name + '_text_' + index + '" name="blue_' + name + '" value="' + value + '"><label for="' + name + '_text_' + index + '"">' + value + '</label></span>')
            }
        });
        $(target).html(arr)
    })


})(jQuery);