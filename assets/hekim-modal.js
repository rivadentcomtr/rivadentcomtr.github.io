$(function () {
    var isEn = document.documentElement.lang === 'en';

    $(document).off('submit', '#infoQuestion').on('submit', '#infoQuestion', function (event) {
        event.preventDefault();

        if (!$('#cbx').is(':checked')) {
            Swal.fire({
                title: isEn ? 'KVKK Consent Required' : 'KVKK Onayı Gerekli',
                text:  isEn
                    ? 'Please read and accept the KVKK Privacy Notice.'
                    : 'Lütfen KVKK Aydınlatma Metni\'ni okuyup onaylayınız.',
                icon: 'warning',
                showConfirmButton: true,
                showCloseButton: true
            });
            return;
        }

        var name    = $('input[name="name_surname"]', this).val().trim();
        var email   = $('input[name="email"]', this).val().trim();
        var phone   = $('input[name="phone"]', this).val().trim();
        var doctor  = $('select[name="team"] option:selected', this).text().trim();
        var msg     = $('textarea[name="message"]', this).val().trim();

        var waEl      = document.getElementById('hekim-wa-data');
        var waNumber  = waEl ? waEl.getAttribute('data-wa')     : '';
        var clinicName= waEl ? waEl.getAttribute('data-clinic') : 'RivaDent';

        if (!waNumber) {
            Swal.fire({
                title: isEn ? 'Error' : 'Hata',
                text:  isEn ? 'Clinic information not found.' : 'Klinik bilgisi bulunamadı.',
                icon: 'error',
                showConfirmButton: true
            });
            return;
        }

        var text = isEn
            ? 'Hello ' + clinicName + ',\n\nI would like to ask a question:\n\n'
                + 'Full Name: '  + name   + '\n'
                + 'E-mail: '     + email  + '\n'
                + 'Phone: '      + phone  + '\n'
                + 'Doctor: '     + doctor + '\n'
                + 'Question: '   + msg
            : 'Merhaba ' + clinicName + ',\n\nSoru göndermek istiyorum:\n\n'
                + 'Ad Soyad: '   + name   + '\n'
                + 'E-posta: '    + email  + '\n'
                + 'Telefon: '    + phone  + '\n'
                + 'Hekim: '      + doctor + '\n'
                + 'Sorum: '      + msg;

        window.open(
            'https://api.whatsapp.com/send/?phone=' + waNumber
            + '&text=' + encodeURIComponent(text),
            '_blank'
        );
    });
});
