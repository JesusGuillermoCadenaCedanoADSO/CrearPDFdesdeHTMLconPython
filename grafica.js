var horas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24];
var Limite =    [35000,	35000,	35000,	35000,	35000, 35000,
                35000,	35000,	35000,	35000,  35000,	35000,
                35000,	35000,	35000,  35000,	35000,	35000,
                35000,	35000,  35000,	35000,	35000,	35000];
var concentraciones = [ 378.05,	366.59,	386.07,	579.68,
                    	370.03,	289.84,	277.24,	378.05,
                        382.63,	184.44,	286.40,	186.73,
                        93.94,	92.79,	775.57,	1157.06,
                        1065.41,1126.13,375.76, 92.79,
                        91.65,	91.65,	97.38,	91.65]
var limit=[100000, 100000, 100000, 100000 ,100000]
var ctx = document.getElementById("myChart");

var myChart = new Chart(ctx, {
    type: 'bar',
   data: {
       datasets: [{
           label: 'Concentración CO (μg/m³ std)',
           data: concentraciones,
           // this dataset is drawn below
           order: 2,
           borderColor: 'rgb(40, 155, 245)',
           backgroundColor: 'rgb(40, 155, 245)'
       }, {
           label: 'res 2254/2017 (μg/m³ std)',
           data: Limite,
           type: 'line',
           // this dataset is drawn on top
           order: 1,
           fill: false,
           borderColor: 'rgb(245, 118, 40)',
           backgroundColor: 'rgb(245, 118, 40)'
       }],
       labels: horas
   },
   options: {
    responsive:true,
    scales: {
        xAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Horas",
              fontSize:14
             },
          },
         ],
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Concentración CO (μg/m³ std)",
              fontSize:14
             },
            stacked: "true",
          },
         ],
      },
      title: {
        display: true,
        text: 'Concentración Monóxido de carbono',
        fontSize:14
      },
      legend: {
        position: 'bottom',
      },
   }
  });

