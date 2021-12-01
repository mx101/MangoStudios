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
            Insert graph here
        </div>

        <div class="col">
            Personal Forecast
            <br>
            <div class="row">
                Completed POTDs
                <br>
                (Selection Box)
            </div>

            <div class="row">
                Autograder runs used
                <br>
                (Selection Box)
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
          potdsStdDev:0,
      }
  },
  mounted() {

  },
  methods: {

  }
}
</script>