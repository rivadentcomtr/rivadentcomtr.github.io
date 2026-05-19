(function ($) {

    $(document).on("submit", "#infoUpdateLanguage", function (event) {
        event.preventDefault();
        var serialized = $(this).serializeArray();
        serialized.push({
            name: 'csrf',
            value: Cookies.get('csrf_token')
        });
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: serialized,
            url: url + 'Languages/update_ajax',
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

    $(document).on("submit", "#infoAddLanguage", function (event) {
        event.preventDefault();
        var serialized = $(this).serializeArray();
        serialized.push({
            name: 'csrf',
            value: Cookies.get('csrf_token')
        });
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: serialized,
            url: url + 'Languages/add_ajax',
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

    $(".lang-status").change(function () {

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
            url: url + 'Languages/status',
            success: function (result) {
                if (result.status === true && status == 0) {
                    Swal.fire({
                        title: 'Devre Dışı Bırakıldı.',
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                    });
                } else if (result.status === true && status == 1) {
                    Swal.fire({
                        title: 'Aktif Edildi.',
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

})(jQuery);