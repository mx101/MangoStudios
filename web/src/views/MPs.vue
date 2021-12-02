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
            All filters({{this.numFilters}})
        </div>

        <div class="col">
            <ul class="navbar-nav ms-auto">
            <li class="nav-item dropdown">
                <a class="nav-link mx-3 dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    MP
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" >mp_intro</a></li>
                    <li><a class="dropdown-item" >mp_stickers</a></li>
                    <li><a class="dropdown-item" >mp_lists</a></li>
                    <li><a class="dropdown-item" >mp_traversals</a></li>
                    <li><a class="dropdown-item" >mp_mosaics</a></li>
                    <li><a class="dropdown-item" >mp_mazes</a></li>
                </ul>
            </li>
            </ul>
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
                <!-- <li class="nav-item dropdown">
                    
                    <a class="nav-link mx-3 dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Major
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" >CS</a></li>
                        <li><a class="dropdown-item" >CS + X</a></li>
                        <li><a class="dropdown-item" >Physics</a></li>
                        <li><a class="dropdown-item" >Electrical Engineering</a></li>
                    </ul>
                </li> -->
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
            Insert graph here
        </div>

        <div class="col">
            <b>Personal Forecast</b>
            <br>
            <div class="row">
                Completed POTDs
                <br>
            </div>
            <div class="row">
                <input name="input" class="form-control" type="number" step="1" min="0" max="99" autocomplete="off" v-model="completed_potds" style="width: auto; font-size: 1em; text-align: center;"> 
            </div>

            <div class="row">
                Autograder runs used
                <br>
            </div>
            <div class="row">
                <input name="input" class="form-control" type="number" step="1" min="0" max="99" autocomplete="off" v-model="autograders_used" style="width: auto; font-size: 1em; text-align: center;"> 
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
        } else if (field == "behavior") {
            this.behavior = ""
        }

        this.buildFileName(this.exam)
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