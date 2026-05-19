$(window).on("load", function() {

    $(function () {
        recaptcha();
        setInterval(function () {
            recaptcha();
        }, 10000);
    })

    function recaptcha() {
        grecaptcha.ready(function () {
           grecaptcha.execute($('#secret-key').data('key'), {action: 'validate_captcha'})
           .then(function (token) {
            $('input[name="g-recaptcha"]').val(token)
        });
       });
    }
    
});

(function($) {
    $(document).on("submit", "#infoForm", function(event){
        var btn = $(this).find('button[type="submit"]');
        btn.attr('disabled', true);
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
            url: url + 'Site_settings/login',
            success: function(result) {
                if (result.status === true) {
                    Swal.fire({
                        title: 'Giriş Başarılı. Yönlendiriliyorsunuz!',
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: false,
                        allowOutsideClick: false
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
                    title: 'Bağlantı Hatası. Lütfen Geliştirici İle İletişime Geçin!',
                    icon: 'error',
                    showConfirmButton: false,
                    showCancelButton: false,
                    showCloseButton: true
                });
            }
        });
    });
})(jQuery);