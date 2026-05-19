$(document).ready(function () {
    var swiper = new Swiper(".treatment-swiper", {
        slidesPerView: 3,
        spaceBetween: 10,
        autoplay: true,
        loop: true,
        pagination: {
            el: ".swiper-treatment-pagination"
        },
        navigation: {
            nextEl: ".treatment-next-btn",
            prevEl: ".treatment-prev-btn",
        },
        breakpoints: {
            0: {
                slidesPerView: 1,
            },
            767: {
                slidesPerView: 2,
            },
            1199: {
                slidesPerView: 3,
            }
        }
    });
    var swiper = new Swiper(".team-swiper", {
        slidesPerView: 4,
        autoplay: true,
        spaceBetween: 10,
        navigation: {
            nextEl: ".team-next-btn",
            prevEl: ".team-prev-btn",
        },
        pagination: {
            el: ".swiper-team-pagination",
            clickable: true,
        },
        breakpoints: {
            0: {
                slidesPerView: 2,
            },
            575: {
                slidesPerView: 2,
            },
            991: {
                slidesPerView: 3,
            },
            1199: {
                slidesPerView: 4,
            }
        }
    });
    var swiper_comment = new Swiper(".comment-swiper", {
        slidesPerView: 3,
        spaceBetween: 10,
        navigation: {
            nextEl: ".comment-next-btn",
            prevEl: ".comment-prev-btn",
        },
        pagination: {
            el: ".swiper-comment-pagination",
            clickable: true,
        },
        breakpoints: {
            0: {
                slidesPerView: 1,
            },
            767: {
                slidesPerView: 2,
            },
            1199: {
                slidesPerView: 3,
            }
        },
        on: {
            init: function () {
                setEqualHeight();
            },
            resize: function () {
                setEqualHeight();
            }
        }
    });
    var swiper = new Swiper(".blog-swiper", {
        slidesPerView: 3,
        spaceBetween: 20,
        navigation: {
            nextEl: ".blog-next-btn",
            prevEl: ".blog-prev-btn",
        },
        pagination: {
            el: ".swiper-blog-pagination",
            clickable: true,
        },
        breakpoints: {
            0: {
                slidesPerView: 1,
            },
            767: {
                slidesPerView: 2,
            },
            1199: {
                slidesPerView: 3,
            }
        }
    });
    var swiper = new Swiper(".instagram-swiper", {
        slidesPerView: 6,
        spaceBetween: 0,
        navigation: {
            nextEl: ".instagram-next-btn",
            prevEl: ".instagram-prev-btn",
        },
        pagination: {
            el: ".swiper-instagram-pagination",
            clickable: true,
        },
        breakpoints: {
            0: {
                slidesPerView: 2,
            },
            575: {
                slidesPerView: 4,
            },
            767: {
                slidesPerView: 5,
            },
            1199: {
                slidesPerView: 6,
            }
        }
    });

    var swiper = new Swiper(".policlinic-swiper", {
        slidesPerView: 4,
        spaceBetween: 10,
        loop: true,
        navigation: {
            nextEl: ".policlinic-next-btn",
            prevEl: ".policlinic-prev-btn",
        },
        pagination: {
            el: ".swiper-policlinic-pagination",
            clickable: true,
        },
        breakpoints: {
            0: {
                slidesPerView: 1,
            },
            575: {
                slidesPerView: 2,
            },
            991: {
                slidesPerView: 3,
            },
            1199: {
                slidesPerView: 4,
            }
        }
    });

    var swiper = new Swiper(".about_slider", {
        loop: true,
        spaceBetween: 20,
        autoplay: {
            delay: 5000,
        },
        pagination: {
            el: ".swiper-about-pagination",
            clickable: true,
        },
    });

    function setEqualHeight() {
        var maxHeight = 0;
        $('.comment-swiper').find('.swiper-slide').each(function () {
            $(this).css('height', 'auto');
            maxHeight = Math.max(maxHeight, $(this).outerHeight());
        });
        $('.comment-swiper').find('.swiper-slide').each(function () {
            $(this).css('height', maxHeight + 'px');
        });
    }
})