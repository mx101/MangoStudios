<template>
  <div id="exams">
  <h1>
      Exams, until data input is fixed, can only switch between given form selects for Exam 1
  </h1>
  <div style="width:20%; float:left; height:100%">
      <select class="form-select" style="width:auto;" v-model="exam" @change="buildFileName">
    <option disabled value="">THIS DOES NOTHING</option>
    <option>Exam 1</option>
    <option>Exam 2</option>
    <option>Exam 3</option>
    <option>Final</option>
  </select>
  <select class="form-select" style="width:auto;" v-model="major" @change="buildFileName">
    <option disabled value="">Select Major</option>
    <option>CS</option>
    <option>ECE</option>
    <option>English</option>
    <option>Math</option>
    <option>Physics</option>
  </select>
  <select class="form-select" style="width:auto;" v-model="year" @change="buildFileName">
    <option disabled value="">Select Year</option>
    <option>Freshman</option>
    <option>Sophomore</option>
    <option>Junior</option>
    <option>Senior</option>
    <option>Graduate</option>
  </select>
  </div>
  <div style="width:80%; float:right">
      <img :src="image" />
  </div>
  
  <br>
  
  </div>
</template>

<script>
import image from "../assets/logo.png"

function getImgUrl(changing_to) {
    var images = require.context('../assets/exams/', false, /\.png$/)
    return images('./' + changing_to + ".png")
}

export default {
  name: 'Exams',
  data: function () {
      return {
          image: image,
          major: "",
          year: "",
          exam: ""
      }
  },
  methods: {
    changeGraph (event) {
        var files = event.target.files || event.dataTransfer.files;
        if (!files.length)
            return;
        this.createImage(files[0]);
    },
    createImage (file) {
        console.log(file)
        var reader = new FileReader();

        reader.onload = (e) => {
            this.image = e.target.result;
        };
        reader.readAsDataURL(file);
    },
    getImgUrl(graph_to_get) {
        var images = require.context('../assets/exams/', false, /\.png$/)
        return images('./' + graph_to_get + ".png")
    },
    buildFileName () {
        var filename = "exam1"
        if (this.major.length != 0) {
            filename = filename + "_" + this.major
        }
        if (this.year.length != 0) {
            switch(this.year) {
                case "Freshman":
                    filename = filename + "_" + "1"
                    break
                case "Sophomore":
                    filename = filename + "_" + "2"
                    break
                case "Junior":
                    filename = filename + "_" + "3"
                    break
                case "Senior":
                    filename = filename + "_" + "4"
                    break
                case "Graduate":
                    filename = filename + "_" + "5"
                    break
            }
            
        }
        console.log(filename)
        this.image = getImgUrl(filename)
    }
  }
}
</script>
<!-- styling for the component -->
<style>
    #about {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
    }
</style>
