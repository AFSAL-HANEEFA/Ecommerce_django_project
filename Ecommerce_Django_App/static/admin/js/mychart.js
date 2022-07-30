$(document).ready(function () {

    var token = $('input[name=csrfmiddlewaretoken]').val()
    $.ajax({
        method: 'POST',
        url: '/super-admin/',
        data: {
            csrfmiddlewaretoken: token


        },

        success: function (chart_data) {
            var order_status = chart_data.order_status
            var monthly_sale = chart_data.monthly_sale
            const orderData = {
                labels: [

                    'Success',
                    'Shipped',
                    'Deliverd',
                    'Cancelled',

                ],
                datasets: [{
                    label: 'My First Dataset',
                    data: order_status,
                    backgroundColor: [

                        'rgb(18, 14, 135)',
                        'rgb(205, 224, 61',
                        'rgb(9, 145, 16)',
                        'rgb(145, 7, 10)',

                    ],
                    hoverOffset: 1
                }]
            };

            const orderConfig = {
                type: 'doughnut',
                data: orderData,
            };

            const orderChart = new Chart(
                document.getElementById('order-status-chart'),
                orderConfig
            );


            const labels = [
                'Sixth Last 30dys',
                'Fifth Last 30dys',
                'Fourth Last 30dys',
                'Third Last 30dys',
                'Second Last 30dys',
                'Last 30dys',
            ];

            const data = {
                labels: labels,
                datasets: [{
                    label: 'Sales in Rs',
                    backgroundColor: 'rgb(119, 50, 168)',
                    borderColor: 'rgb(9, 156, 31)',
                    data: monthly_sale,
                }]
            };

            const config = {
                type: 'bar',
                data: data,
                options: {}
            };
            const myChart = new Chart(
                document.getElementById('sales-chart'),
                config
            );

        }

    })


})
