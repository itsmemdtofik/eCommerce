$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

document.addEventListener("DOMContentLoaded", function(){
    window.addEventListener('scroll', function(){
        if(this.window.scrollY > 50){
            this.document.getElementById('navbar_top').classList.add('fixed-top');
            navbar_height = this.document.querySelector('.navbar').offsetHeight;
            this.document.body.style.paddingTop = navbar_height + 'px';
        }else{
            this.document.getElementById('navbar_top').classList.remove('fixed-top');
            this.document.body.style.paddingTop = '0';
        }
    })
})