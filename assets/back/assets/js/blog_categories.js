(function ($) {

    $(document).on("submit", "#infoBlog_categoryAdd", function (event) {
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
            url: url + 'Blog_category/add_ajax',
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

    $(document).on("submit", "#infoBlog_categoryUpdate", function (event) {
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
            url: url + 'Blog_category/update_ajax',
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

    $(".blog-status").change(function () {
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
            url: url + 'Blog_category/status',
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

    $(".delete-blog").jConfirm().on('confirm', function (e) {
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
            url: url + 'Blog_category/delete',
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

    $('.change-position_sp').sortable({
        update: function(event, ui) {
            $(this).children().each(function(index){
                if($(this).attr('data-position') != (index+1)){
                    $(this).attr('data-position',(index+1)).addClass('updated');
                }
            });
            saveNewPositions()
        }
    });

    function saveNewPositions() {
        var positions = [];
        var data = [];

        $('.updated').each(function () {
            positions.push([$(this).attr('data-index'), $(this).attr('data-position'),$(this).attr('data-page'),$(this).attr('data-offset')]);
            $(this).removeClass('updated');
        });
        $.ajax({
            method: 'post',
            dataType: 'json',
            data: {
                positions: positions,
                csrf: Cookies.get('csrf_token')
            },
            url: url + 'Blog_category/update_position',
            success: function(result) {
                if (result.status === true) {
                    $.each(result.position, function( index, value ) {
                        $('.position_area_'+index).find('.current-position').html(value);
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
    }


})(jQuery);