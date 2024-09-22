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

$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var quantityElement = this.parentNode.children[2];
    
    $.ajax({
        url: '/pluscart',
        type: 'GET',
        data: {
            id: id
        },
        success: function(data) {
            quantityElement.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.total_amount;
        }
    });
});

$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var quantityElement = this.parentNode.children[2];
    
    $.ajax({
        url: '/minuscart',
        type: 'GET',
        data: {
            id: id
        },
        success: function(data) {
            quantityElement.innerText = data.quantity;
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.total_amount;
        }
    });
});

$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var element = this;
    
    $.ajax({
        url: '/removecart',
        type: 'GET',
        data: {
            id: id
        },
        success: function(data) {
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.total_amount;
            element.parentNode.parentNode.parentNode.parentNode.remove();
        }
    });
});

$("#search-form").submit(function(event) {
    event.preventDefault();
    var search = $("#search1").val();
    // console.log(search);
    $.ajax({
        url: 'search',
        type: 'GET',
        data: {
            search:search
        },
    })
});
