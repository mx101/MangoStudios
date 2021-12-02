<template>
    <div id="mps">
    <h1 style="padding-left:30px">
        Machine Problems
    </h1>

    <div class="row" style="width:75%">
        <div class="col">
            <img src="../assets/filter_icon.jpg" width="100px" height="10em">
        </div>

        <div class="col">
            Filters({{this.numFilters}})
        </div>

        <div class="col">
                 <select class="form-select" style="width:auto;" v-model="mp" @change="buildFileName('')">
                    <option disabled value="">MP</option>
                    <option>mp_intro</option>
                    <option>mp_stickers</option>
                    <option>mp_lists</option>
                    <option>mp_traversals</option>
                    <option>mp_mosaics</option>
                    <option>mp_mazes</option>
                </select>
                <a v-on:click="clearField('mp')" 
                    v-if="this.mp.length != 0" 
                    type="button" 
                    class="btn btn-primary btn-sm" 
                    aria-label="Close">Clear
                </a>
        </div>
        
        <div class="col">
                 <select class="form-select" style="width:auto;" v-model="student_behaviors" @change="buildFileName('')">
                    <option disabled value="">Student Behaviors</option>
                    <option>Labs completed</option>
                    <option>POTDS completed</option>
                    <option>Exam Scores</option>
                    <option>Final Grade</option>
                </select>
                <a v-on:click="clearField('student_behaviors')" 
                    v-if="this.student_behaviors.length != 0" 
                    type="button" 
                    class="btn btn-primary btn-sm" 
                    aria-label="Close">Clear
                </a>
        </div>
        
        <div class="col">
                <select class="form-select" style="width:auto;" v-model="major" @change="buildFileName('')">
                    <option disabled value="">Major</option>
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
        
        <div class="col">
                <select class="form-select" style="width:auto;" v-model="year" @change="buildFileName('')">
                    <option disabled value="">Year</option>
                    <option>Freshman</option>
                    <option>Sophomore</option>
                    <option>Junior</option>
                    <option>Senior</option>
                </select>
                <a v-on:click="clearField('year')" 
                    v-if="this.year.length != 0" 
                    type="button" 
                    class="btn btn-primary btn-sm" 
                    aria-label="Close">Clear
                </a>
        </div>
    </div>

    <div class="row" style="width:100%">
        <div class="col">
            Insert graph here
        </div>

        <div class="col">
            <b>Personal Forecast</b>
            <br>
            <div class="row">
                Completed POTDs
                <br>
                <input name="input" class="form-control" type="number" step="1" min="0" max="99" autocomplete="off" v-model="completed_potds" @change="changeExpectedGrade()" style="width: auto; font-size: 1em; text-align: center;"> 
            </div>

            <div class="row">
                Autograder runs used
                <br>
                <input name="input" class="form-control" type="number" step="1" min="0" max="99" autocomplete="off" v-model="autograders_used" @change="changeExpectedGrade()" style="width: auto; font-size: 1em; text-align: center;"> 
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
          mp: "",
      }
  },
  mounted() {

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
  }
}
</script>


<style scoped>

#mps {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /* text-align: center; */
    color: #2c3e50;
    margin-top: 60px;
}


#mps h1 {
    font-size: calc(4em + 1vw);
    font-weight: 700;
    margin: 0;
}

</style>