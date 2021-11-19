<template>
  <div id="about">
  <!-- 
        Introduction Section:
            - CS 225 Title
            - Data Structures description
            - Page Overview (ex: "Syllabus, Professors, Course Breakdown")
            - Main Statistics: (ex: Average GPA, Average Letter Grade, Hours Per Week)
     -->
    <section id="intro-section">
        <!-- CS 225 Title -->
        <div class="row">
            <h1>CS 225</h1>
        </div>

        <!-- Data Structures -->
        <div class="row">
            <h2>Data Structures</h2>
        </div>
        <br>
        <!-- Learning Goals -->
        <div class="row">
            <h3><strong>#</strong> Implement classic and adapted data structures and algorithms</h3>
            <h3><strong>#</strong> Navigate, organize, compile C++ projects of moderate complexity in Linux. </h3>
            <h3><strong>#</strong> Use basic editing and debugging tools such as GDB and Valgrind. </h3>
            <!-- <h3># Analyze the efficiency of implementation choices.</h3> -->
            <h3><strong>#</strong> Decompose a problem into its supporting data structures such as lists, stacks, queues, trees, etc. </h3>
            <h3><strong>#</strong> Solve problems involving graph search, tree traversal, optimization, data organization, etc. </h3>
        </div>
        <br>
        <!-- Buttons -->
        <div id="button-container" class="row">
            <div id="buttons">
                <a class="button button-transparent" href="https://courses.engr.illinois.edu/cs225/sp2021/
                ">COURSE WEBPAGE</a>
                <a class="button button-transparent" href="https://courses.engr.illinois.edu/cs225/sp2021/policy/syllabus/
                ">SYLLABUS</a>
                <a class="button button-transparent" href="https://courses.engr.illinois.edu/cs225/sp2021/staff/
                ">INSTRUCTORS</a>
            </div>
        </div>
        <br>
        <!-- Average GPA, Average Letter Grade, Hours Per Week -->
        <div id="jumbotron-container" class="row">

            <!-- Average GPA -->
            <div id="jumbotron" class="col me-4">
                <h2>Avg GPA</h2>
                <h1>3.2<span style="color: rgb(152, 152, 152); font-size: 2rem;">/4.00</span></h1>
            </div>

            <!-- Average Letter Grade -->
            <div id="jumbotron" class="col me-4">
                <h2>Avg Letter Grade</h2>
                <h1>B</h1>
            </div>

            <!-- Hours Per Week -->
            <div id="jumbotron" class="col">
                <h2>Hours Per Week</h2>
                <h1>15.0<span style="color: rgb(152, 152, 152); font-size: 2rem;">hrs</span></h1>
            </div>
        </div>
    </section>


    <!-- 
        Statistics Section:
            - Statistics Title
            - Doughnut Chart
            - Bar Chart
     -->
     <section id="statistics-section">

        <!-- Statistics Title -->
        <div class="row">
            <h1 class="display-5 fw-bold" style="text-align: center;">Course Overview</h1>
            <hr class="mb-4"> 
        </div>

        <!-- Data Visualizations -->
        <div class="row justify-content-center">

            <!-- Doughnut Chart -->
            <div id="jumbotron" class="col-md-5 p-4 me-4">
                <h2 class="mb-2">Grade Distribution</h2>
                <canvas id="doughnutChart" width="335" height="235"></canvas>
            </div>
            
            <!-- Bar Chart -->
            <div id="jumbotron" class="col-md-5 p-4">
                <h2 class="mb-2">Grade Distribution</h2>
                <canvas id="barChart" width="335" height="235"></canvas>
            </div>
        </div>

    </section> 


    <!-- Statistic Section Continued -->
    <section id="statistics-section">
       
        <div id="jumbotron-container" class="row justify-content-center">
            <div id="jumbotron" class="col-md p-5 mb-4 me-4">
                <h2>Most Common Letter Grade</h2>
                <h1>A</h1>
            </div>

            <div id="jumbotron" class="col-md p-5 mb-4">
                <h2 class="w-auto">Percentage of A's</h2>
                <h1>60.78%</h1>
            </div>
        </div>

        <div id="jumbotron-container" class="row justify-content-center">
            <div id="jumbotron" class="col-md p-5 me-4">
                <h2>Total Enrollments</h2>
                <h1>2,008<span style="color: rgb(152, 152, 152); font-size: 2rem;"> students</span></h1>
            </div>
    
            <div id="jumbotron" class="col-md p-5">
                <h2>Total Withdrawals</h2>
                <h1>54<span style="color: rgb(152, 152, 152); font-size: 2rem;"> students</span></h1>
            </div>
        </div>

    </section>
  </div>
</template>

<script>
import Chart from "chart.js";

export default {
  name: 'About',
  mounted() {
    this.fillInCharts()
  },
  methods: {
    fillInCharts() {
      
      var A = '1222';
      var B = '355';
      var C = '203';
      var D = '138';
      var F = '90';
      // var W = '2';

      new Chart(document.getElementById("doughnutChart").getContext('2d'), 
      {
          type: 'doughnut',
          data: {

              labels: ['A', 'B', 'C', 'D', 'F'],
              datasets: 
              [ {
                  data: 
                  [ parseInt(A), parseInt(B), parseInt(C), parseInt(D), parseInt(F) ],
                  // backgroundColor: ['#1DA462', '#4C8BF5', '#FFCD46', '#FFA700', '#DD5144']
                  backgroundColor: ['#93c47d', '#6d9eeb', '#ffd966', '#f6b26b', '#e06666']
              }]
          },
          options: 
          {
              title: 
              {
                  text: "Chart Title",
                  display: false
              },
              animation: { animateScale: true },
              responsive: true
          }
      });

      new Chart(document.getElementById("barChart").getContext('2d'), 
        {
            type: 'bar',
            data: {
                labels: ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'],
                datasets: [ {
                    data: [279, 807, 136, 123, 144, 88, 71, 88, 44, 37, 45, 56, 90],
                    backgroundColor: ['#38761d', '#6aa84f', '#93c47d', '#b6d7a8', '#ffe599', '#ffd966', '#f1c232', '#f9cb9c', '#f6b26b', '#e69138', '#ea9999', '#e06666', '#cc0000']
                }]
            },
            options: {
                title: {
                    text: "Title",
                    display: false
                },
                legend: {
                  display: false
                },
                animation: {
                    animateScale: true
                },
                responsive: true
            }
        });

    }
  }
}
</script>
<!-- styling for the component -->
<style scoped>
    #about {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: left;
    color: #2c3e50;
    margin-top: 0px;
    }
    body {
    max-width: 100%;
    overflow-x: hidden;
    }
    /* Navigation Bar */
    #navbar {
        font-family: "Spartan", sans-serif;
        font-weight: 500;
        letter-spacing: 1px;
        background-color: #002855;
    }
    /* Intro Section */
    #intro-section {
        height: 100vh;
        width: 100vw;
        padding: 5% 7.5% 5%;
        font-family: "Montserrat", sans-serif;
    }
    #intro-section h1 {
        font-size: calc(4em + 1vw);
        font-weight: 700;
        margin: 0;
    }
    #intro-section h2 {
        font-size: calc(1em + 1vw);
        font-weight: 600;
        letter-spacing: 2px;
        /* margin: 0; */
    }
    #intro-section h3 {
        font-size: calc(0.5em + 1vw);
        font-weight: 400;
    }
    .button {
        /* background-color: #389bc2; */
        background-color: #87cfff;
        border: none;
        color: white;
        padding: 16px 32px;
        margin-top: 1%;
        margin-right: 1%;
        margin-bottom: 2%;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: 500;
        letter-spacing: 5px;
        -webkit-transition-duration: 0.4s;
        transition-duration: 0.4s;
        cursor: pointer;
        outline: none;
        border-radius: 30px;
    }
    .button-transparent {
        background-color: #002855;
        color: white;
        border: 1px solid #002855;
    }
    .button:hover {
        background-color: #b2daff;
        text-decoration: none;
        color: #002855;
        border-color: #002855;
    }
    /* #jumbotron-container {
        display: flex;
        justify-content: space-around;
    } */
    #jumbotron {
        background-color: #f8fafa;
        text-align: center;
        border-radius: 25px;
        padding: 2% 1%;
        box-shadow: 2px 2px 22px rgba(0, 0, 0, 0.2);
    }
    /* Statistics Section */
    #statistics-section {
        height: 100vh;
        width: 100vw;
        padding: 5% 7.5% 5%;
        font-family: "Montserrat", sans-serif;
    }
    #statistics-section h1 {
        font-size: calc(3em + 1vw);
        font-weight: 600;
        margin: 0;
    }
    #statistics-section h2 {
        font-size: calc(1em + 1vw);
        font-weight: 600;
        letter-spacing: 2px;
        /* margin: 0; */
    }
    #statistics-section h3 {
        font-size: calc(0.5em + 1vw);
        font-weight: 400;
    }
</style>
