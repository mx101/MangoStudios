<template>
    <div id="mps">
    <h1 style="padding-left:30px">
        <br>
        MPs
    </h1>

    <div class="row" style="width:75%">
        <div class="col">
            Cute filter image
        </div>

        <div class="col">
            All filters({{this.numFilters}})
        </div>

        <div class="col">
            <select class="form-select" style="width:auto;" v-model="mp" @change="updateData()">
                <option disabled value="">MP</option>
                <option>mp_intro</option>
                <option>mp_stickers</option>
                <option>mp_lists</option>
                <option>mp_traversals</option>
                <option>mp_mosaics</option>
                <option>mp_mazes</option>
            </select>
        </div>
        
        <div class="col">
            <ul class="navbar-nav ms-auto">
            <li class="nav-item dropdown">
                <a class="nav-link mx-3 dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Student Behaviors
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" >Labs</a></li>
                    <li><a class="dropdown-item" >POTDS</a></li>
                    <li><a class="dropdown-item" >Exams</a></li>
                    <li><a class="dropdown-item" >Final Grade</a></li>
                </ul>
            </li>
            </ul>
        </div>
        
        <div class="col">
            <ul class="navbar-nav ms-auto">
            <li class="nav-item dropdown">
                <a class="nav-link mx-3 dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Major
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" >CS</a></li>
                    <li><a class="dropdown-item" >CS + X</a></li>
                    <li><a class="dropdown-item" >Physics</a></li>
                    <li><a class="dropdown-item" >Electrical Engineering</a></li>
                </ul>
            </li>
            </ul>
        </div>
        
        <div class="col">
            <ul class="navbar-nav ms-auto">
            <li class="nav-item dropdown">
                <a class="nav-link mx-3 dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Year
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" >Freshman</a></li>
                    <li><a class="dropdown-item" >Sophomore</a></li>
                    <li><a class="dropdown-item" >Junior</a></li>
                    <li><a class="dropdown-item" >Senior</a></li>
                </ul>
            </li>
            </ul>
        </div>
    </div>

    <div class="row" style="width:100%">
        <div class="col">
            <div id="my_dataviz"></div>
        </div>

        <div class="col">
            <b>Personal Forecast</b>
            <br>
            <div class="row">
                Completed POTDs
                <br>
                <input name="input" class="form-control" type="number" step="1" min="0" max="135" autocomplete="off" v-model="completed_potds" @change="changeExpectedGrade()" style="width: auto; font-size: 1em; text-align: center;"> 
            </div>

            <div class="row">
                Autograder runs used
                <br>
                <input name="input" class="form-control" type="number" step="1" min="0" max="10" autocomplete="off" v-model="autograders_used" @change="changeExpectedGrade()" style="width: auto; font-size: 1em; text-align: center;"> 
            </div>

            <div class="row">
                Expected Grade
                <br>
                {{this.expectedGrade}}%
            </div>
        </div>
    </div>

    <div class="row" style="width:75%">
        <div class="col">
            Average grade {{this.avgGrade}}% +- {{this.gradeStdDev}}
        </div>

        <div class="col">
            Average POTDS {{this.avgPotds}}% +- {{this.potdsStdDev}}
        </div>
    </div>
    </div>
</template>

<script>
import * as d3 from 'd3'
    
function updateData_begin() {
    // Clear previous content
    var dataCSV = "/mp/mp1.csv"

    console.log(dataCSV)
    d3.select("svg").remove();

    // set the dimensions and margins of the graph
    const margin = {top: 80, right: 80, bottom: 80, left: 80},
        width = 500 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    const svg = d3.select("#my_dataviz")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform",
            `translate(${margin.left}, ${margin.top})`);

    // get the data
    console.log("loading data")

    d3.csv(dataCSV).then( function(data) {
        // X axis: scale and draw:
        const x = d3.scaleLinear()
            .domain([0, d3.max(data, function(d) { return +d.score })])  
            .range([0, width]);
        svg.append("g")
                .attr("transform", `translate(0, ${height})`)
                .call(d3.axisBottom(x))
                .append("text")
                .attr("x", width/2)
                .attr("y", +40)
                .attr("fill", "#002855")
                .attr("font-weight", "bold")
                .attr("font-size", "15px")
                .attr("font-family", "Montserrat")
                .text("Grade Percentage (%)");
        
        // set the parameters for the histogram
        const histogram = d3.histogram()
            .value(function(d) { return d.score; })   // I need to give the vector of value
            .domain(x.domain())  // then the domain of the graphic
            .thresholds(x.ticks(10)); // then the numbers of bins
    
        // And apply this function to data to get the bins
        const bins = histogram(data);

        console.log("data", data)
    
        // Y axis: scale and draw:
        const y = d3.scaleLinear()
            .range([height, 0]);
            y.domain([0, d3.max(bins, function(d) { return d.length; })]);   // d3.hist has to be called before the Y axis obviously
        svg.append("g")
            .call(d3.axisLeft(y))
            .append("text")
            .attr("x", -height/2 + 80)
            .attr("y", -40)
            .attr("fill", "#002855")
            .attr("font-weight", "bold")
            .attr("font-size", "15px")
            .attr("font-family", "Montserrat")
            .attr("transform", "rotate(-90)")
            .text("Number of Students");
    
        // Add a tooltip div. Here I define the general feature of the tooltip: stuff that do not depend on the data point.
        // Its opacity is set to 0: we don't see it by default.
        const tooltip = d3.select("#my_dataviz")
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "#002855")
        .style("color", "white")
        .style("border-radius", "5px")
        .style("padding", "10px")
    
        // A function that change this tooltip when the user hover a point.
        // Its opacity is set to 1: we can now see it. Plus it set the text and position of tooltip depending on the datapoint (d)
        const showTooltip = function(event,d) {
        tooltip
            .transition()
            .duration(100)
            .style("opacity", 1)

        tooltip
            .html("Range: " + d.x0 + "% - " + d.x1 + "%")
            .style("font-family", "Montserrat")
            .style("left", (event.x) + "px")
            .style("top", (event.y) + "px")
        }
        const moveTooltip = function(event,d) {
            console.log(d)
        tooltip
        .style("left", (event.x) + 12.5 + "px")
        .style("top", (event.y) + -12.5 + "px")
        }
        // A function that change this tooltip when the leaves a point: just need to set opacity to 0 again
        const hideTooltip = function(event,d) {
            console.log(d)
        tooltip
            .transition()
            .duration(100)
            .style("opacity", 0)
        }

        // append the bar rectangles to the svg element
        svg.selectAll("rect")
            .data(bins)
            .join("rect")
            .attr("x", 1)
            .attr("transform", function(d) { return `translate(${x(d.x0)}, ${y(d.length)})`})
            .attr("width", function(d) { return x(d.x1) - x(d.x0) - 2; })
            .attr("height", function(d) { return height - y(d.length); })
            .attr("fill", "#0068DE")
            .attr("opacity", "0.35")
            // .attr("stroke", "black")
            // .attr("stroke-width", "1px")

            // Show tooltip on hover
            .on("mouseover", showTooltip )
            .on("mousemove", moveTooltip )
            .on("mouseleave", hideTooltip )
    });
}

export default {
  name: 'MPs',
  data: function () {
      return {
          numFilters: 0,
          expectedGrade:0,
          avgGrade: 0,
          gradeStdDev: 0,
          avgPotds: 0,
          potdsStdDev: 0,
          completed_potds: 0,
          autograders_used: 0,
          major: "",
          year: "",
          student_behaviors: "",
          mp: "mp_intro",
      }
  },
  mounted() {
    //   updateData(data2);
    //   updateData(data3);
    //   updateData(data4);
    //   updateData(data5);
    updateData_begin();
  },
  methods: {
    getImgUrl(changing_to) {
        var images = require.context('../assets/exams/', false, /\.jpg$/)
        return images('./' + changing_to + ".jpg")
    },
    clearField(field) {
        if (field == "major") {
            this.major = ""
        } else if (field == "year") {
            this.year = ""
        } else if (field == "student_behaviors") {
            this.student_behaviors = ""
        } else {
            this.mp = ""
        }

        this.buildFileName(this.exam)
    },
    changeExpectedGrade () {
        if (this.completed_potds > 135) {
            this.completed_potds = 135
        }
        if (this.autograders_used > 12) {
            this.autograders_used = 12
        }
        if (this.completed_potds < 0) {
            this.completed_potds = 0
        }
        if (this.autograders_used < 0) {
            this.autograders_used = 0
        }
        this.expectedGrade = Math.floor(62 + (this.completed_potds/130)*29 + (this.autograders_used/9)*12);
    },
    updateData() {
        // Clear previous content
        var dataCSV = "/mp/"

        switch(this.mp) {
            case "mp_intro":
                dataCSV = dataCSV + "mp1"
                break
            case "mp_stickers":
                dataCSV = dataCSV + "mp2"
                break
            case "mp_lists":
                dataCSV = dataCSV + "mp3"
                break
            case "mp_traversals":
                dataCSV = dataCSV + "mp4"
                break
            case "mp_mosaics":
                dataCSV = dataCSV + "mp5"
                break
            case "mp_mazes":
                dataCSV = dataCSV + "mp6"
                break
        }

        dataCSV = dataCSV + ".csv"

        console.log(dataCSV)
        d3.select("svg").remove();

        // set the dimensions and margins of the graph
        const margin = {top: 80, right: 80, bottom: 80, left: 80},
            width = 500 - margin.left - margin.right,
            height = 500 - margin.top - margin.bottom;

        // append the svg object to the body of the page
        const svg = d3.select("#my_dataviz")
        .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
        .append("g")
            .attr("transform",
                `translate(${margin.left}, ${margin.top})`);

        // get the data
        console.log("loading data")

        d3.csv(dataCSV).then( function(data) {
            // X axis: scale and draw:
            const x = d3.scaleLinear()
                .domain([0, d3.max(data, function(d) { return +d.score })])  
                .range([0, width]);
            svg.append("g")
                    .attr("transform", `translate(0, ${height})`)
                    .call(d3.axisBottom(x))
                    .append("text")
                    .attr("x", width/2)
                    .attr("y", +40)
                    .attr("fill", "#002855")
                    .attr("font-weight", "bold")
                    .attr("font-size", "15px")
                    .attr("font-family", "Montserrat")
                    .text("Grade Percentage (%)");
            
            // set the parameters for the histogram
            const histogram = d3.histogram()
                .value(function(d) { return d.score; })   // I need to give the vector of value
                .domain(x.domain())  // then the domain of the graphic
                .thresholds(x.ticks(10)); // then the numbers of bins
        
            // And apply this function to data to get the bins
            const bins = histogram(data);

            console.log("data", data)
        
            // Y axis: scale and draw:
            const y = d3.scaleLinear()
                .range([height, 0]);
                y.domain([0, d3.max(bins, function(d) { return d.length; })]);   // d3.hist has to be called before the Y axis obviously
            svg.append("g")
                .call(d3.axisLeft(y))
                .append("text")
                .attr("x", -height/2 + 80)
                .attr("y", -40)
                .attr("fill", "#002855")
                .attr("font-weight", "bold")
                .attr("font-size", "15px")
                .attr("font-family", "Montserrat")
                .attr("transform", "rotate(-90)")
                .text("Number of Students");
        
            // Add a tooltip div. Here I define the general feature of the tooltip: stuff that do not depend on the data point.
            // Its opacity is set to 0: we don't see it by default.
            const tooltip = d3.select("#my_dataviz")
            .append("div")
            .style("opacity", 0)
            .attr("class", "tooltip")
            .style("background-color", "#002855")
            .style("color", "white")
            .style("border-radius", "5px")
            .style("padding", "10px")
        
            // A function that change this tooltip when the user hover a point.
            // Its opacity is set to 1: we can now see it. Plus it set the text and position of tooltip depending on the datapoint (d)
            const showTooltip = function(event,d) {
            tooltip
                .transition()
                .duration(100)
                .style("opacity", 1)

            tooltip
                .html("Range: " + d.x0 + "% - " + d.x1 + "%")
                .style("font-family", "Montserrat")
                .style("left", (event.x) + "px")
                .style("top", (event.y) + "px")
            }
            const moveTooltip = function(event,d) {
                console.log(d)
            tooltip
            .style("left", (event.x) + 12.5 + "px")
            .style("top", (event.y) + -12.5 + "px")
            }
            // A function that change this tooltip when the leaves a point: just need to set opacity to 0 again
            const hideTooltip = function(event,d) {
                console.log(d)
            tooltip
                .transition()
                .duration(100)
                .style("opacity", 0)
            }

            // append the bar rectangles to the svg element
            svg.selectAll("rect")
                .data(bins)
                .join("rect")
                .attr("x", 1)
                .attr("transform", function(d) { return `translate(${x(d.x0)}, ${y(d.length)})`})
                .attr("width", function(d) { return x(d.x1) - x(d.x0) - 2; })
                .attr("height", function(d) { return height - y(d.length); })
                .attr("fill", "#0068DE")
                .attr("opacity", "0.35")
                // .attr("stroke", "black")
                // .attr("stroke-width", "1px")

                // Show tooltip on hover
                .on("mouseover", showTooltip )
                .on("mousemove", moveTooltip )
                .on("mouseleave", hideTooltip )
        });
    }
  }
}
</script>