// Global parameters:
// do not resize the chart canvas when its container does (keep at 600x400px)
// Chart.defaults.global.responsive = false;
// define the chart data
var chartData = {
  labels: JSON.parse(jinjaLabels),
  
  datasets: [{
    data: JSON.parse(jinjaValues),
    label: jinjaLegend,
    backgroundColor: "#50164F63",
    pointHoverRadius: 5,
    pointHoverBackgroundColor: "#164F63",
    pointRadius: 1,
    pointHitRadius: 10
    }]
}

console.log(jinjaLabels);
console.log(jinjaValues);


// get chart canvas
var ctx = document.getElementById("myChart").getContext("2d");

// create the chart using the chart canvas
var myChart = new Chart(ctx, {
  type: 'line',
  data: chartData,
});
