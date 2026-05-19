(function ($) {
    $(document).on("submit", "#infoHomepage", function (event) {
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
            url: url + 'Admin/update_home_page',
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

