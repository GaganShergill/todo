let day = new Date().getDate();
let calendar = document.getElementById('calendar_date');
calendar.textContent = day;

let taskStatus = document.getElementById("taskStatus");
taskStatus.textContent = taskDone.toString() + "/" + totTask.toString()

let myChart = document.getElementById('myChart').getContext('2d')
let pieChart = new Chart(myChart, {
  type: 'pie',
  data: {
    datasets: [{
      data: [taskDone, totTask-taskDone],
      backgroundColor: ['rgb(255, 255, 255)', 'transparent']
    }]
  },
  options: {
    tooltips: {enabled: false}
  }
});
