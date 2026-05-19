(function ($) {

    let image_add;
    image_add = new Dropzone('#dpz-images-file', {
        url: $(this).attr('action'),
        acceptedFiles: "image/jpeg,image/png,image/jpg",
        timeout: 300000,
        init: function() {
            var dropzone_ = this;

            this.on("sending", function(file, xhr, formData) {
                formData.append("csrf", Cookies.get('csrf_token'));
            });
        }
    })
    image_add.on("success", function (file, response) {
        const myJSON = JSON.parse(response);
        $('.dz-default').remove();
        if (myJSON.status == true) {
            $('#infoImage').prepend([
                '<div class="col-lg-2 mb-2" id="del-' + myJSON.id + '">\n' +
                '    <div class="gallery-item">\n' +
                '        <img loading="lazy" src="' + site_url + myJSON.item + '">\n' +
                '    </div>\n' +
                '    <div class="gallery-options d-flex justify-content-between" style="margin-top:5px">\n' +
                '        <div class="copy-btna-area">\n' +
                '            <button class="btn btn-primary copy-btn" data-image-url="' + site_url + myJSON.item + '" type="button">\n' +
                '                <i class="ft-copy"></i>\n' +
                '            </button>\n' +
                '        </div>\n' +
                '        <span class="btn btn-danger gallery-img-delete" data-id="' + myJSON.id + '">\n' +
                '            <i class="la la-trash"></i>\n' +
                '        </span>\n' +
                '    </div>\n' +
                '</div>'
            ])
        }
    })

    if($('#dpz-file').length > 0) {
        var myDropzone = new Dropzone('#dpz-file', {
            url: $(this).attr('action'),
            maxFiles: 1,
            init: function() {
                var dropzone_ = this;

                this.on("sending", function(file, xhr, formData) {
                    formData.append("csrf", Cookies.get('csrf_token'));
                });

                this.on("maxfilesexceeded", function(file) {
                    this.removeAllFiles();
                    this.addFile(file);
                });

            }
        });
    }

    $('#infoImage').on('click', '.copy-btn', function () {
        var image_url = $(this).attr('data-image-url');
        navigator.clipboard.writeText(image_url)
        .then(function () {
            Swal.fire({
                title: 'Kopyalandı.',
                icon: 'success',
                showConfirmButton: false,
                showCancelButton: false,
                showCloseButton: true,
                timer: 1000,
            });
        })
        .catch(function (err) {
            Swal.fire({
                title: 'Kopyalanamadı',
                icon: 'warning',
                showConfirmButton: false,
                showCancelButton: false,
                showCloseButton: true,
                timer: 3000,
                html: result.error
            });
        });
    })

    $(document).on('click', '.gallery-img-delete', function (e) {
        $('.gallery-img-delete').jConfirm().on('confirm', function (e) {
            var id = $(this).attr("data-id");
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
                    url: url + 'Images/delete',
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
    })

})(jQuery);

