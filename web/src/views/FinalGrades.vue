<template>
  <div id="exams" >
  <h1 style="padding-left:30px">
      <br>
      Final Grades
  </h1>
  <div class="row" style="text-align: center; width: 100%">
    <div class="col" style="text-align: center; width: auto">
        <img :src="image" />
    </div>
    <div class="col" v-if="this.image != null" style="text-align: center; width: auto">
        <h2>
            <br>
            Average Grade
        </h2>
        <h2>
            <br>
            {{this.avg}}
        </h2>
    </div>
    <div class="col" v-if="this.image != null" style="text-align: center; width: auto">
    <div class="row">
    <select class="form-select" style="width:auto;" v-model="major" @change="buildFileName('')">
        <option disabled value="">Select Major</option>
        <option>CS</option>
        <option>ECE</option>
        <option>English</option>
        <option>Math</option>
        <option>Physics</option>
    </select>
    <a v-on:click="clearField('major')" 
        v-if="this.major.length != 0" 
        type="button" 
        class="btn btn-primary btn-sm" 
        aria-label="Close">Clear
    </a>
    </div>
    <br>
    <br>
    <div class="row">
    <select class="form-select" style="width:auto;" v-model="year" @change="buildFileName('')">
        <option disabled value="">Select Year</option>
        <option>Freshman</option>
        <option>Sophomore</option>
        <option>Junior</option>
        <option>Senior</option>
        <option>Graduate</option>
    </select>
    <a v-on:click="clearField('year')" 
        v-if="this.year.length != 0" 
        type="button" 
        class="btn btn-primary btn-sm" 
        aria-label="Close">Clear
    </a>
    </div>
    <br>
    <br>
    <div class="row">
    <select class="form-select" style="width:auto;" v-model="behavior" @change="buildFileName('')">
        <option disabled value="">Select Behaviors</option>
        <option>POTDs Completed</option>
        <option>Autograders used</option>
    </select>
    <a v-on:click="clearField('behavior')" 
        v-if="this.behavior.length != 0" 
        type="button" 
        class="btn btn-primary btn-sm" 
        aria-label="Close">Clear
    </a>
    </div>
    </div>
  </div>
  </div>
</template>

<script>
import image from "../assets/final_grade/final_grade.png"

function getImgUrl(changing_to) {
    var images = require.context('../assets/final_grade/', false, /\.png$/)
    return images('./' + changing_to + ".png")
}

export default {
  name: 'FinalGrades',
  data: function () {
      return {
          image: image,
          major: "",
          year: "",
          exam: "final_grade",
          avg: "B",
          behavior: "",
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
    buildFileName (selectExam) {
        var filename = selectExam
        if (selectExam.length == 0) {
            filename = this.exam
        }
        if (this.behavior.length != 0) {
            filename = filename + "_potds"
        } else {
            // implement clear POTDS behavior case
        }
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
        return selectExam
    }, clearField(field) {
        if (field == "major") {
            this.major = ""
        } else if (field == "year") {
            this.year = ""
        } else if (field == "behavior") {
            this.behavior = ""
        }

        this.buildFileName(this.exam)
    },
  }
}
</script>
<!-- styling for the component -->
<style scoped>
    .row {
        display: table;
        
    }

    .col {
        display: table-cell;
        vertical-align: middle;
    }

    #about {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
    }
</style>
