(function($) {

    $(document).on("submit", ".infoSiteSettings", function(event){
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
            url: url + 'Site_settings/update_site_settings',
            success: function(result) {
                if (result.status === true) {
                    Swal.fire({
                        title: 'Güncelleme Başarılı!',
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: false,
                        timer: 3000,
                    });
                    setTimeout(
                        function(){
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
            error: function() {
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

})(jQuery);