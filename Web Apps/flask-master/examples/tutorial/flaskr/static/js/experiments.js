function myFunction() {
    "use strict";
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

function myFruits(id, value) {
    var x = document.getElementById(id);
    var i = x.selectedIndex;
    document.getElementById("demo").innerHTML = x.options[i].text;
    document.getElementById("fruit").innerHTML = "Fruit #" + value + ":";
}

function myChart01(datax, datay1, datay2) {
    
    document.getElementById("output").innerHTML = "Y1-Data: " + datay1[0];
    var ctx = document.getElementById('canvas').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: datax,
            datasets: [{
                fill: false,
                label: "CN",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: datay1      


            }, {
                fill: false,
                label: "US",
                backgroundColor: 'rgb(25, 120, 101)',
                borderColor: 'rgb(25, 120, 101)',
                data: datay2
            }]
        },

        // Configuration options go here
        options: {}
    });
}

function dispchart(jdata) {
    var ctx = document.getElementById('canvas01').getContext('2d');
    new Chart(ctx, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [{
                fill: false,
                label: "CN",
                backgroundColor: 'rgb(2, 2, 2)',
                borderColor: 'rgb(2, 2, 2)',
                data: jdata
            }, {
                fill: false,
                label: "US",
                backgroundColor: 'rgb(25, 120, 101)',
                borderColor: 'rgb(25, 120, 101)',
                data: [0, 7, 3, 2, 17, 37, 42]
            }]
        },

        // Configuration options go here
        options: {}
    });
}

function myInit(datax, datay1, datay2, jdata) {
    myChart01(datax, datay1, datay2);
    dispchart(jdata);
    console.log(datax, datay1, datay2, jdata)
}