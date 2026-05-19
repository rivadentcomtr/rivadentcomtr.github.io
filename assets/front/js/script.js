$(document).ready(function () {
    $('.accordion-btn').click(function () {
        var btn = $(this).closest('.accordion-item-box').find('.accordion-text');
        if ($(this).hasClass('active')) {
            $(this).addClass('active');
            btn.stop(true, false).slideDown(300);
            $('.accordion-btn').removeClass('active');
            $('.accordion-text').stop(true, false).slideUp(300);
        } else {
            $('.accordion-btn').removeClass('active');
            $('.accordion-text').stop(true, false).slideUp(300);
            $(this).addClass('active');
            btn.stop(true, false).slideDown(300);
        }
    });
    $(document).scroll(function () {
        var window_top = $(window).scrollTop();
        if (window_top >= 500) {
            $('header').addClass('header_sticky');
            $('body').css('padding-top', '42px');
        } else {
            $('body').css('padding-top', '');
            $('header').removeClass('header_sticky');
        }
    });
    $('.live-support-btn').click(function () {
        $('.live-support-chat-area').slideDown("slow");
        $(this).addClass('d-none')
        $('body').addClass('overflow-hidden')
    })
    $('.live-support-exit-btn').click(function () {
        $('.live-support-chat-area').slideUp("slow");
        $('.live-support-btn').removeClass('d-none')
        $('body').removeClass('overflow-hidden')
    })
    $('.lang-trg').click(function () {
        $('.lang-options').toggleClass('active');
    })
    $(document).click(function (e) {
        if ($('.lang-options').hasClass('active')) {
            if (!$(e.target).is('.lang-options, .languages *')) {
                $('.lang-options').toggleClass('active');
            }
        }
    })
    $(window).scroll(function () {
        var footer_element = $('.footer-element').outerHeight();
        if ($(window).scrollTop() + $(window).height() > $(document).height() - footer_element) {
            $('.whatsapp-chat-box').addClass('d-none');
            $('.live-support-item').addClass('d-none');
        } else {
            $('.whatsapp-chat-box').removeClass('d-none');
            $('.live-support-item').removeClass('d-none');
        }
    })
    $('.mobile-menu-btn').click(function () {
        $('.header-mobile-area').addClass('active');
        $('body').addClass('overflow-hidden');
        $('.bcg-color-area').addClass('active');
    })
    $('.mobile-close-btn').click(function () {
        $('.header-mobile-area').removeClass('active');
        $('body').removeClass('overflow-hidden');
        $('.bcg-color-area').removeClass('active');
    })
    $('.bcg-color-area').click(function () {
        $('.header-mobile-area').removeClass('active');
        $('body').removeClass('overflow-hidden');
        $('.bcg-color-area').removeClass('active');

    })
    $('.clinic-select').change(function () {
        var poliklinik_url = $(this).val();
        if (poliklinik_url) {
            window.location.href = poliklinik_url;
        }
    })
    if (active == 'treatment' || active == 'blogs') {
        $('.treatment-content-text').find('h2').each(function (index) {
            $(this).attr('id', 'treatment-' + (index + 1));
        });
        $('.treatment-content-text').find('h2').each(function () {
            $('.treatment-contents-list').append('<li><a href="#' + $(this).attr('id') + '">' + $(this).text() + '</a></li>')
        });
        $(document).on('click', '.treatment-contents-list a', function (event) {
            event.preventDefault();
            var header_height = $('header').outerHeight(true);
            var target = $(this).attr('href');

            $('html, body').animate({
                scrollTop: $(target).offset().top - header_height
            }, 100);
        });
    }
    new WOW().init();

    $(document).on('click', '.mobile-in-list-trg', function() {
    	$(this).closest('li').find('.mobile-in-list').toggleClass('active')
    })

})