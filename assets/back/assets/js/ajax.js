(function($) {

    $('.copy-text').click(function () {
        var btn = $(this)
        var element = document.createElement("textarea");
        element.innerHTML = btn.data('copy')
        document.body.appendChild(element);
        element.select();
        document.execCommand("copy");
        element.parentNode.removeChild(element);
        btn.find('i').removeClass('ft-copy').addClass('ft-check')
        setTimeout(() => {
            btn.find('i').removeClass('fa-check').addClass('ft-copy')
        }, 500)
    })

    $(document).on("submit", "#infoProfileEdit", function(event){
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
            url: url + 'Site_settings/update_account',
            success: function(result) {
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

    $(document).on("submit", "#infoContact", function(event){
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
            url: url + 'Site_settings/update_contact',
            success: function(result) {
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
    
    $(".user-status").change(function(){

        var id = $(this).data("id");
        if($(this).prop('checked')) {
            var status = 1;
        } else {
            var status = 0;
        }

        var data = [
        {
            name: 'csrf',
            value: Cookies.get('csrf_token')
        },{
            name : 'status',
            value : status
        },{
            name : 'id',
            value : id
        }]
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: data,
            url: url + 'Site_settings/user_status',
            success: function(result) {
                if (result.status === true && status == 0) {
                    Swal.fire({
                        title: 'Erişim Engellendi.',
                        icon: 'success',
                        showConfirmButton: false,
                        showCancelButton: false,
                        showCloseButton: true,
                        timer: 3000,
                    });
                } else if (result.status === true && status == 1) {
                    Swal.fire({
                        title: 'Erişim İzni Verildi.',
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
            error: function() {
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