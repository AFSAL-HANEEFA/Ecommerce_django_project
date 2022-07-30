$(document).ready(function () {

    $('#rzp-button1').click(function (e) {
        e.preventDefault();
        $.ajax({
            method: 'GET',
            url: '/orders/razorpay/',
            success: function (data) {
                total_amount = (document.getElementById('total_amount').innerHTML).substring(1)
                var key = data.key

                var options = {

                    "key": key, // Enter the Key ID generated from the Dashboard
                    "amount": total_amount * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                    "currency": "INR",
                    "name": "Appleshop",
                    "description": "Thank you for shop with us",
                    "image": "https://commons.wikimedia.org/wiki/File:Apple_Computer_Logo_rainbow.svg",
                    // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                    "handler": function (response) {
                        // alert(response.razorpay_payment_id);
                        swal("Payment done!", "Your order placed!", "success")
                            .then(() => {
                                document.getElementById("payment_id").value = response.razorpay_payment_id;
                                document.getElementById("payment_mode").value = "RAZOR PAY";
                                $(".payment_hidden")[0].click();
                            });


                        // alert(response.razorpay_order_id);
                        // alert(response.razorpay_signature)

                    },
                    "prefill": {
                        "name": document.getElementById('address_name').innerHTML,
                        "email": "gaurav.kumar@example.com",
                        "contact": document.getElementById('address_mob').innerHTML
                    },
                    "notes": {
                        "address": "Razorpay Corporate Office"
                    },
                    "theme": {
                        "color": "#3399cc"
                    }
                };
                var rzp1 = new Razorpay(options);
                rzp1.on('payment.failed', function (response) {
                    alert(response.error.description);

                });
                rzp1.open();
            }

        })
    });
})