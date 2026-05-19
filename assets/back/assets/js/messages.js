(function($) {

    $(".seen-message").click(function(){
        var id = $(this).data("id");
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
            url: url + 'Site_settings/seen_message',
            success: function(result) {
                if (result.status === true) {
                    $(".seen-button-"+id).removeClass("btn-success");
                    $(".seen-button-"+id).addClass("btn-secondary");
                }
            }
        });
    });

    $(".delete-message").jConfirm().on('confirm', function(e){
        var id = $(this).data("id");
        var data = [
        {
            name: 'csrf',
            value: Cookies.get('csrf_token')
        },{
            name : 'id',
            value : id
        }]

        $.ajax({
            method: 'post',
            dataType: 'json',
            data: data,
            url: url + 'Site_settings/delete_message',
            success: function(result) {
                if (result.status === true) {
                    $('#delete'+id).remove();
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