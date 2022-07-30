$(document).ready(function () {

    // =========== add to cart ====================

    $('.add_to_cart_btn').click(function (e) {
        e.preventDefault();
        $('.cart_spinner').removeClass('visually-hidden')
        var product_id = $(this).closest('.add_to_cart').find('.product_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val()

        $.ajax({
            method: 'POST',
            url: '/cart/add-to-cart/',
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token

            },
            success: function (data) {
                $('.add_to_cart').load(location.href + " .add_to_cart");
                $('.cart_spinner').addClass('visually-hidden')
                $('.cart_num').load(location.href + " .cart_num");
            }
        })
    })

    // =============== qty plus in cart =============

    $(document).on('click', '.plus_btn', function (e) {
        e.preventDefault();
        var product_id = $(this).closest('.closest_cls').find('.product_id').val()
        var quantity = $(this).closest('.qty_cart').find('.qty_input').val();
        var token = $('input[name=csrfmiddlewaretoken').val()
        if (quantity < 5) {
            quantity++;
            $(this).closest('.qty_cart').find('.qty_input').val(quantity)
        }

        $.ajax({
            method: 'POST',
            url: '/cart/change-qty/',
            data: {
                'product_id': product_id,
                'quantity': quantity,
                csrfmiddlewaretoken: token
            },

            success: function (response) {
                $('.refresh_cart').load(location.href + ' .refresh_cart')
            }
        })
    })

    // =============== qty minus in cart =============

    $(document).on('click', '.minus_btn', function (e) {
        e.preventDefault;
        var product_id = $(this).closest('.closest_cls').find('.product_id').val()
        var quantity = $(this).closest('.qty_cart').find('.qty_input').val();
        var token = $('input[name=csrfmiddlewaretoken').val()

        if (quantity > 1) {
            quantity--
            $(this).closest('.qty_cart').find('.qty_input').val(quantity)
        }

        $.ajax({
            method: 'POST',
            url: '/cart/change-qty/',
            data: {
                'product_id': product_id,
                'quantity': quantity,
                csrfmiddlewaretoken: token
            },

            success: function (response) {
                $('.refresh_cart').load(location.href + ' .refresh_cart')
            }


        })
    })

    // =============== qty delete in cart =============

    $(document).on('click', '.dlt_btn', function (e) {
        e.preventDefault;
        var product_id = $(this).closest('.closest_cls').find('.product_id').val()
        var token = $('input[name=csrfmiddlewaretoken]').val()
        $.ajax({
            method: 'POST',
            url: '/cart/',
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },

            success: function (response) {
                $('.refresh_cart').load(location.href + ' .refresh_cart')
                $('.cart_num').load(location.href + " .cart_num");
            }

        })
    })

    // =========== address save =============

    $(document).on('click', '.address_save_btn', function (e) {
        e.preventDefault
        var token = $('input[name=csrfmiddlewaretoken]').val()
        var name = $('input[name=name]').val()
        var address = $("textarea[name=address]").val()
        var state = $('select[name=state]').val()
        var pin = $('input[name=pin]').val()
        var mob = $('input[name=mob]').val()

        if (name === '' || address === '' || state === '' || pin === '' || mob === '') {
            var footer = document.getElementById('address-footer')
            footer.innerHTML = '<p class="text-danger mt-3">All fields are required!</P>'
        }
        else if (mob.length != 10) {
            var footer = document.getElementById('address-footer')
            footer.innerHTML = '<p class="text-danger mt-3">Invalid mobile! Mobile number must be 10 digits</P>'
        }
        else if (pin.length != 6) {
            var footer = document.getElementById('address-footer')
            footer.innerHTML = '<p class="text-danger mt-3">Invalid pin code! PIN code must be 6 digits</P>'
        }
        else {
            document.getElementById('btn-close').click()

            $.ajax({
                method: 'POST',
                url: '/profiles/address/',
                data: {
                    csrfmiddlewaretoken: token,
                    'name': name,
                    'address': address,
                    'state': state,
                    'pin': pin,
                    'mob': mob
                },

                success: function (response) {
                    $('.load_address').load(location.href + ' .load_address')
                }
            })
        }
    })

    // =========== address delete =============

    $(document).on('click', '.address_delete_btn', function (e) {
        e.preventDefault;
        var token = $('input[name=csrfmiddlewaretoken]').val()
        var address_id = $(this).closest('.address_closest_cls').find('.address_id').val()
        $.ajax({
            method: 'POST',
            url: '/profiles/address-delete/',
            data: {
                csrfmiddlewaretoken: token,
                'address_id': address_id
            },

            success: function (data) {
                $('.load_address').load(location.href + ' .load_address')
            }
        })
    })

    // =========== address edit =============

    $(document).on('click', '.address_edit_btn', function (e) {
        e.preventDefault;
        $(".address_form").removeClass('address_remove')
        $(".address_form").addClass('address_add')
        var token = $('input[name=csrfmiddlewaretoken]').val()
        address_id = $(this).closest('.address_closest_cls').find('.address_id').val()
        $.ajax({
            method: 'POST',
            url: '/profiles/address-edit/',
            data: {
                csrfmiddlewaretoken: token,
                'address_id': address_id
            },

            success: function (data) {
                $('input[name=name]').val(data.name)
                $("textarea[name=address]").val(data.address)
                $('select[name=state]').val(data.state)
                $('input[name=pin]').val(data.pin)
                $('input[name=mob]').val(data.mob)
            }
        })
    })

    // =========== address default =============

    $(document).on('click', '.address_default_btn', function (e) {
        e.preventDefault;
        token = $('input[name=csrfmiddlewaretoken]').val()
        address_id = $(this).closest('.address_closest_cls').find('.address_id').val()

        $.ajax({
            method: 'POST',
            url: '/profiles/address-default/',
            data: {
                csrfmiddlewaretoken: token,
                'address_id': address_id
            },
            success: function (data) {
                $('.address_load').load(location.href + ' .address_load')
                $(".address_load1").load(location.href + ' .address_load1')
            }
        })
    })

    // ============ coupon apply ==============

    $(document).on('click', '.apply_coupon', function (e) {
        e.preventDefault();
        $('.coupon_spinner').removeClass('visually-hidden')
        var token = $('input[name=csrfmiddlewaretoken]').val()
        var copoun_code = $(this).closest('.coupon_container').find('.coupon_code_value').val()

        $.ajax({
            method: 'POST',
            url: '/offers/apply-coupon/',
            data: {
                csrfmiddlewaretoken: token,
                'code': copoun_code,
            },
            success: function (data) {

                if (data.status === 'Coupon Applied! Redeem coupon to get discount') {
                    $('.apply_coupon').addClass('d-none');
                    $('.redeem_coupon').removeClass('d-none');
                    $('.coupon_status').removeClass('text-danger');
                    $('.coupon_status').addClass('text-success');
                    $('.coupon_status').html(data.status);
                }
                else {
                    $('.coupon_status').html(data.status);
                    $('.coupon_status').removeClass('text-success');
                    $('.coupon_status').addClass('text-danger');
                }
                $('.coupon_spinner').addClass('visually-hidden');
            }
        })
    })

    // ============ coupon redeem ==============

    $('.redeem_btn').click(function () {
        location.reload(true)
    })
    $('.remove_coupon').click(function () {
        var token = $('input[name=csrfmiddlewaretoken]').val()

        $.ajax({
            method: 'POST',
            url: '/offers/remove-coupon/',
            data: {
                csrfmiddlewaretoken: token,
            },
            success: function (data) {
                location.reload(true)
            }
        })
    })
});