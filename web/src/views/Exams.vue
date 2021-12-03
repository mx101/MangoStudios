<template>
	<div id="exams">
		<h1>Exams</h1>
		<h2>Select a filter to explore exam data</h2>

		<div class="row" style="width: 75%">
			<div class="col">
				<select class="form-select" v-model="mp" @change="updateData()">
					<option>Exam 1</option>
					<option>Exam 2</option>
					<option>Exam 3</option>
				</select>
			</div>

			<div class="col">
				<select
					class="form-select"
					v-model="student_behaviors"
					@change="updateData()"
				>
					<option disabled value="">Student Behaviors</option>
					<option>POTDs Completed</option>
				</select>
				<a
					v-on:click="clearField('student_behaviors')"
					v-if="this.student_behaviors.length != 0"
					type="button"
					class="btn btn-primary btn-sm"
					aria-label="Close"
					>Clear
				</a>
			</div>

			<div class="col">
				<select class="form-select" v-model="major" @change="updateData()">
					<option disabled value="">Major</option>
					<option>Advertising</option>
					<option>CS</option>
					<option>ECE</option>
					<option>English</option>
					<option>Math</option>
					<option>Physics</option>
				</select>
				<a
					v-on:click="clearField('major')"
					v-if="this.major.length != 0"
					type="button"
					class="btn btn-primary btn-sm"
					aria-label="Close"
					>Clear
				</a>
			</div>

			<div class="col">
				<select class="form-select" v-model="year" @change="updateData()">
					<option disabled value="">Year</option>
					<option>Freshman</option>
					<option>Sophomore</option>
					<option>Junior</option>
					<option>Senior</option>
					<option>Graduate</option>
				</select>
				<a
					v-on:click="clearField('year')"
					v-if="this.year.length != 0"
					type="button"
					class="btn btn-primary btn-sm"
					aria-label="Close"
					>Clear
				</a>
			</div>
		</div>

		<div class="row" style="width: 100%">
			<div class="col">
				<div id="my_dataviz"></div>
			</div>

			<div style="margin-top: 10%" id="jumbotron" class="col">
				<h2>Personal Forecast</h2>
				<hr class="mb-0 mt-1" />
				<div id="forecast-padding" class="row">
					<h3>Completed POTDs</h3>
					<br />
					<input
						name="input"
						class="form-control"
						type="number"
						step="1"
						min="0"
						max="135"
						autocomplete="off"
						v-model="completed_potds"
						@change="changeExpectedGrade()"
					/>
				</div>

				<div id="forecast-padding" class="row">
					<h3>Expected Grade</h3>
					<br />
					<h1>{{ this.expectedGrade }}%</h1>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
/* eslint-disable */
import * as d3 from "d3";
import annotation from "../assets/js/d3-annotation.min.js";

export default {
	name: "MPs",
	data: function () {
		return {
			numFilters: 0,
			expectedGrade: 62,
			avgGrade: 0,
			gradeStdDev: 0,
			avgPotds: 0,
			potdsStdDev: 0,
			completed_potds: 0,
			major: "",
			year: "",
			student_behaviors: "",
			mp: "Exam 1",
			annotation: "Gradea aaa",
		};
	},
	mounted() {
		// let recaptchaScript = document.createElement('script')
		//   recaptchaScript.setAttribute('src', 'https://rawgit.com/susielu/d3-annotation/master/d3-annotation.min.js')
		//   document.head.appendChild(recaptchaScript)
		this.updateData();
	},
	methods: {
		getImgUrl(changing_to) {
			var images = require.context("../assets/exams/", false, /\.jpg$/);
			return images("./" + changing_to + ".jpg");
		},
		clearField(field) {
			if (field == "major") {
				this.major = "";
			} else if (field == "year") {
				this.year = "";
			} else if (field == "student_behaviors") {
				this.student_behaviors = "";
			}

			this.updateData();
		},
		changeExpectedGrade() {
			if (this.completed_potds > 135) {
				this.completed_potds = 135;
			}
			if (this.completed_potds < 0) {
				this.completed_potds = 0;
			}
			this.expectedGrade = Math.floor(72 + (this.completed_potds / 130) * 28);
		},
		updateData() {
			// Clear previous content
			var dataCSV = "/exam/";

			switch (this.mp) {
				case "Exam 1":
					dataCSV = dataCSV + "exam1";
					break;
				case "Exam 2":
					dataCSV = dataCSV + "exam2";
					break;
				case "Exam 3":
					dataCSV = dataCSV + "exam3";
					break;
			}

			if (this.student_behaviors.length > 0) {
				console.log("student behaviors selected");
				switch (this.student_behaviors) {
					case "Autograders Used":
						dataCSV = dataCSV + "_autogrades";
						break;
					case "POTDs Completed":
						dataCSV = dataCSV + "_potds";
						break;
				}
			}

			if (this.major.length > 0) {
				dataCSV = dataCSV + "_" + this.major;
			}

			if (this.year.length > 0) {
				console.log("student behaviors selected");
				switch (this.year) {
					case "Freshman":
						dataCSV = dataCSV + "_1";
						break;
					case "Sophomore":
						dataCSV = dataCSV + "_2";
						break;
					case "Junior":
						dataCSV = dataCSV + "_3";
						break;
					case "Senior":
						dataCSV = dataCSV + "_4";
						break;
					case "Graduate":
						dataCSV = dataCSV + "_5";
						break;
				}
			}

			dataCSV = dataCSV + ".csv";

			console.log(dataCSV);
			d3.select("svg").remove();

			// set the dimensions and margins of the graph
			const margin = { top: 40, right: 80, bottom: 80, left: 60 },
				width = 1100 - margin.left - margin.right,
				height = 800 - margin.top - margin.bottom;

			// append the svg object to the body of the page
			const svg = d3
				.select("#my_dataviz")
				.append("svg")
				.attr("width", width + margin.left + margin.right)
				.attr("height", height + margin.top + margin.bottom)
				.append("g")
				.attr("transform", `translate(${margin.left}, ${margin.top})`);

			// get the data
			console.log("loading data");
			if (this.student_behaviors.length == 0) {
				d3.csv(dataCSV).then(function (data) {
					// X axis: scale and draw:
					const x = d3
						.scaleLinear()
						.domain([
							0,
							d3.max(data, function (d) {
								return +d.score;
							}),
						])
						.range([0, width]);
					svg
						.append("g")
						.attr("transform", `translate(0, ${height})`)
						.call(d3.axisBottom(x))
						.append("text")
						.attr("x", width / 2)
						.attr("y", +40)
						.attr("fill", "#002855")
						.attr("font-weight", "bold")
						.attr("font-size", "15px")
						.attr("font-family", "Montserrat")
						.text("Grade Percentage (%)");

					// set the parameters for the histogram
					const histogram = d3
						.histogram()
						.value(function (d) {
							return d.score;
						}) // I need to give the vector of value
						.domain(x.domain()) // then the domain of the graphic
						.thresholds(x.ticks(10)); // then the numbers of bins

					// And apply this function to data to get the bins
					const bins = histogram(data);

					console.log("data", data);

					// Y axis: scale and draw:
					const y = d3.scaleLinear().range([height, 0]);
					y.domain([
						0,
						d3.max(bins, function (d) {
							return d.length;
						}),
					]); // d3.hist has to be called before the Y axis obviously
					svg
						.append("g")
						.call(d3.axisLeft(y))
						.append("text")
						.attr("x", -height / 2 + 80)
						.attr("y", -40)
						.attr("fill", "#002855")
						.attr("font-weight", "bold")
						.attr("font-size", "15px")
						.attr("font-family", "Montserrat")
						.attr("transform", "rotate(-90)")
						.text("Number of Students");

					// Add a tooltip div. Here I define the general feature of the tooltip: stuff that do not depend on the data point.
					// Its opacity is set to 0: we don't see it by default.
					const tooltip = d3
						.select("#my_dataviz")
						.append("div")
						.style("opacity", 0)
						.attr("class", "tooltip")
						.style("background-color", "#002855")
						.style("color", "white")
						.style("border-radius", "5px")
						.style("padding", "10px");

					// A function that change this tooltip when the user hover a point.
					// Its opacity is set to 1: we can now see it. Plus it set the text and position of tooltip depending on the datapoint (d)
					const showTooltip = function (event, d) {
						tooltip.transition().duration(100).style("opacity", 1);

						tooltip
							.html("Range: " + d.x0 + "% - " + d.x1 + "%")
							.style("font-family", "Montserrat")
							.style("left", event.x + "px")
							.style("top", event.y + "px");
					};
					const moveTooltip = function (event, d) {
						console.log(d);
						tooltip
							.style("left", event.x + 12.5 + "px")
							.style("top", event.y + -12.5 + "px");
					};
					// A function that change this tooltip when the leaves a point: just need to set opacity to 0 again
					const hideTooltip = function (event, d) {
						console.log(d);
						tooltip.transition().duration(100).style("opacity", 0);
					};

					// append the bar rectangles to the svg element
					svg
						.selectAll("rect")
						.data(bins)
						.join("rect")
						.attr("x", 1)
						.attr("transform", function (d) {
							return `translate(${x(d.x0)}, ${y(d.length)})`;
						})
						.attr("width", function (d) {
							return x(d.x1) - x(d.x0) - 2;
						})
						.attr("height", function (d) {
							return height - y(d.length);
						})
						.attr("fill", "#0068DE")
						.attr("opacity", "0.35")
						// .attr("stroke", "black")
						// .attr("stroke-width", "1px")

						// Show tooltip on hover
						.on("mouseover", showTooltip)
						.on("mousemove", moveTooltip)
						.on("mouseleave", hideTooltip);

					// Annotations
					const type = annotation.annotationCalloutElbow;

					const annotations1 = [
						{
							note: {
								title: "Average Grade",
								label: "The average exam grade was 76%",
								wrap: 125,
							},
							x: 860,
							y: 225,
							dy: 75,
							dx: 75,
							type: annotation.annotationCalloutElbow,
							connector: { end: "dot" },
						},
					];
					const annotations2 = [
						{
							note: {
								title: "Average Grade",
								label: "The average grade earned on Exam 2 was 79%",
								wrap: 125,
							},
							x: 300,
							y: 225,
							dy: 75,
							dx: 75,
							type: annotation.annotationCalloutElbow,
							connector: { end: "dot" },
						},
					];
					const annotations3 = [
						{
							note: {
								title: "Average Grade",
								label: "The average grade earned on Exam 3 was 72%",
								wrap: 125,
							},
							x: 600,
							y: 225,
							dy: 75,
							dx: 75,
							type: annotation.annotationCalloutElbow,
							connector: { end: "dot" },
						},
					];

					const makeAnnotations = annotation
						.annotation()
						.notePadding(10)
						.type(type)
						.annotations(annotations1);

					// Alter annotation color to white
					annotations1.map(function (d) {
						d.color = "#002855";
						return d;
					});

					d3.select("svg")
						.append("g")
						.attr("class", "annotation-group")
						.call(makeAnnotations);
				});
			} else {
				if (this.student_behaviors == "Autograders Used") {
					console.log("ag");
					d3.csv(dataCSV).then(function (data) {
						// Add X axis
						const x = d3
							.scaleLinear()
							.domain([
								d3.min(data, function (d) {
									return +d.autogrades;
								}) - 2.5,
								d3.max(data, function (d) {
									return +d.autogrades;
								}),
							])
							.range([0, width]);
						svg
							.append("g")
							.attr("transform", `translate(0, ${height})`)
							.call(d3.axisBottom(x))
							.append("text")
							.attr("x", width / 2)
							.attr("y", +40)
							.attr("fill", "#002855")
							.attr("font-weight", "bold")
							.attr("font-family", "Montserrat")
							.attr("font-size", "15px")
							.text("Autograders Used");

						// Add Y axis
						const y = d3
							.scaleLinear()
							.domain([
								d3.min(data, function (d) {
									return +d.score;
								}) - 2.5,
								d3.max(data, function (d) {
									return +d.score;
								}),
							])
							.range([height, 0]);
						svg
							.append("g")
							.call(d3.axisLeft(y))
							.append("text")
							.attr("x", -height / 2 + 80)
							.attr("y", -40)
							.attr("fill", "#002855")
							.attr("font-weight", "bold")
							.attr("font-size", "15px")
							.attr("font-family", "Montserrat")
							.attr("transform", "rotate(-90)")
							.text("MP Grade (%)");

						// Add a tooltip div. Here I define the general feature of the tooltip: stuff that do not depend on the data point.
						// Its opacity is set to 0: we don't see it by default.
						const tooltip = d3
							.select("#my_dataviz")
							.append("div")
							.style("opacity", 0)
							.attr("class", "tooltip")
							.style("background-color", "#002855")
							.style("color", "white")
							.style("border-radius", "5px")
							.style("padding", "10px");

						// A function that change this tooltip when the user hover a point.
						// Its opacity is set to 1: we can now see it. Plus it set the text and position of tooltip depending on the datapoint (d)
						const mouseover = function (event, d) {
							console.log(event);
							console.log(d);
							tooltip.style("opacity", 1);
						};

						const mousemove = function (event, d) {
							tooltip
								.html(
									`
                                MP Grade: <strong>${d.score}%</strong>
                                <br>
                                POTDs: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>${d.autogrades}</strong>
                            `
								)
								.style("font-family", "Montserrat")
								.style("left", event.x + 12.5 + "px")
								.style("top", event.y + -12.5 + "px");
						};

						// A function that change this tooltip when the leaves a point: just need to set opacity to 0 again
						const mouseleave = function (event, d) {
							console.log(event);
							console.log(d);
							tooltip.transition().duration(300).style("opacity", 0);
						};

						const hoverEffect = function (event, d) {
							svg.select(d).style("fill", "#002855");
						};

						// Add dots
						svg
							.append("g")
							.selectAll("dot")
							.data(
								data.filter(function (d, i) {
									return i < 200;
								})
							) // the .filter part is just to keep a few dots on the chart, not all of them
							.enter()
							.append("circle")
							.attr("cx", function (d) {
								return x(d.autogrades);
							})
							.attr("cy", function (d) {
								return y(d.score);
							})
							.attr("r", 8)
							.style("fill", "#0068DE")
							.style("opacity", 0.35)
							.style("stroke", "white")
							.on("mouseover", hoverEffect)
							.on("mouseover", mouseover)
							.on("mousemove", mousemove)
							.on("mouseleave", mouseleave);

						// Annotations
						const type = annotation.annotationCalloutElbow;

						const annotations = [
							{
								note: {
									title: "Positive Correlation",
									label:
										"Students who use more autogrades tend to earn higher MP grades",
									wrap: 125,
								},
								x: 300,
								y: 275,
								dy: 75,
								dx: 75,
								type: annotation.annotationCalloutElbow,
								connector: { end: "dot" },
							},
						];

						const makeAnnotations = annotation
							.annotation()
							.notePadding(10)
							.type(type)
							.annotations(annotations);

						// Alter annotation color to white
						annotations.map(function (d) {
							d.color = "#002855";
							return d;
						});

						d3.select("svg")
							.append("g")
							.attr("class", "annotation-group")
							.call(makeAnnotations);
					});
				} else {
					d3.csv(dataCSV).then(function (data) {
						// Add X axis
						const x = d3
							.scaleLinear()
							.domain([
								0,
								d3.max(data, function (d) {
									return +d.potds;
								}),
							])
							.range([0, width]);
						svg
							.append("g")
							.attr("transform", `translate(0, ${height})`)
							.call(d3.axisBottom(x))
							.append("text")
							.attr("x", width / 2)
							.attr("y", +40)
							.attr("fill", "#002855")
							.attr("font-weight", "bold")
							.attr("font-family", "Montserrat")
							.attr("font-size", "15px")
							.text("Number of POTDs Completed");

						// Add Y axis
						const y = d3
							.scaleLinear()
							.domain([
								25,
								d3.max(data, function (d) {
									return +d.score;
								}),
							])
							.range([height, 0]);
						svg
							.append("g")
							.call(d3.axisLeft(y))
							.append("text")
							.attr("x", -height / 2 + 80)
							.attr("y", -40)
							.attr("fill", "#002855")
							.attr("font-weight", "bold")
							.attr("font-size", "15px")
							.attr("font-family", "Montserrat")
							.attr("transform", "rotate(-90)")
							.text("MP Grade (%)");

						// Add a tooltip div. Here I define the general feature of the tooltip: stuff that do not depend on the data point.
						// Its opacity is set to 0: we don't see it by default.
						const tooltip = d3
							.select("#my_dataviz")
							.append("div")
							.style("opacity", 0)
							.attr("class", "tooltip")
							.style("background-color", "#002855")
							.style("color", "white")
							.style("border-radius", "5px")
							.style("padding", "10px");

						// A function that change this tooltip when the user hover a point.
						// Its opacity is set to 1: we can now see it. Plus it set the text and position of tooltip depending on the datapoint (d)
						const mouseover = function (event, d) {
							console.log(event);
							console.log(d);
							tooltip.style("opacity", 1);
						};

						const mousemove = function (event, d) {
							tooltip
								.html(
									`
                                MP Grade: <strong>${d.score}%</strong>
                                <br>
                                POTDs: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>${d.potds}</strong>
                            `
								)
								.style("font-family", "Montserrat")
								.style("left", event.x + 12.5 + "px")
								.style("top", event.y + -12.5 + "px");
						};

						// A function that change this tooltip when the leaves a point: just need to set opacity to 0 again
						const mouseleave = function (event, d) {
							console.log(event);
							console.log(d);
							tooltip.transition().duration(300).style("opacity", 0);
						};

						const hoverEffect = function (event, d) {
							svg.select(d).style("fill", "#002855");
						};

						// Add dots
						svg
							.append("g")
							.selectAll("dot")
							.data(
								data.filter(function (d, i) {
									return i < 100;
								})
							) // the .filter part is just to keep a few dots on the chart, not all of them
							.enter()
							.append("circle")
							.attr("cx", function (d) {
								return x(d.potds);
							})
							.attr("cy", function (d) {
								return y(d.score);
							})
							.attr("r", 8)
							.style("fill", "#0068DE")
							.style("opacity", 0.35)
							.style("stroke", "white")
							.on("mouseover", hoverEffect)
							.on("mouseover", mouseover)
							.on("mousemove", mousemove)
							.on("mouseleave", mouseleave);

						// Annotations
						const type = annotation.annotationCalloutElbow;

						const annotations = [
							{
								note: {
									title: "Slight Positive Correlation",
									label:
										"Students who do more POTDs tend to do better on Exams.",
									wrap: 125,
								},
								x: 300,
								y: 225,
								dy: 75,
								dx: 75,
								type: annotation.annotationCalloutElbow,
								connector: { end: "dot" },
							},
						];

						const makeAnnotations = annotation
							.annotation()
							.notePadding(10)
							.type(type)
							.annotations(annotations);

						// Alter annotation color to white
						annotations.map(function (d) {
							d.color = "#002855";
							return d;
						});

						d3.select("svg")
							.append("g")
							.attr("class", "annotation-group")
							.call(makeAnnotations);
					});
				}
			}
		},
	},
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@100;500&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Spartan&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;500;600;700;800&display=swap");

#navbar {
	/* font-family: "Josefin Sans", sans-serif; */
	font-family: "Spartan", sans-serif;
	font-weight: 500;
	letter-spacing: 1px;
	background-color: #002855;
}

#exams {
	height: 100vh;
	width: 100vw;
	padding: 2.5% 7.5% 5%;
	font-family: "Montserrat", sans-serif;
}

#exams h1 {
	font-size: calc(4em + 1vw);
	font-weight: 700;
	margin: 0;
}

#exams h2 {
	font-size: calc(1em + 1vw);
	font-weight: 600;
	letter-spacing: 2px;
}

#exams h3 {
	font-size: calc(0.25em + 1vw);
	font-weight: 500;
	text-align: left;
	margin-left: 0;
}

#jumbotron {
	background-color: #f8fafa;
	text-align: center;
	border-radius: 25px;
	padding: 2% 3%;
	box-shadow: 2px 2px 22px rgba(0, 0, 0, 0.2);
	height: 90%;
}

#forecast-padding {
	padding-left: 10%;
	padding-right: 10%;
	padding-top: 10%;
}

#app {
	font-family: "Spartan", sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	color: #2c3e50;
}

.navbar-nav > li {
	padding-left: 30px;
	padding-right: 30px;
}

.router-link-exact-active {
	border-bottom: 1px solid #123456;
}

.router-link-active {
	border: 1px solid #fff;
	color: #fff !important;
}
</style>
