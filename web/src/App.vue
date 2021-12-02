<template>
  <div id="app">
    <nav id="navbar" class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">

            <a class="navbar-brand" href="#/Overview">CS 225++</a>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">

                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link mx-3 " aria-current="page" href="#/Overview">Overview</a>
                    </li>

                    <li class="nav-item dropdown">
                        <a class="nav-link mx-3 dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            MP Resources
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                          <li><a class="dropdown-item" href="#/Playground">All</a></li>
                          <div class="dropdown-divider"></div>
                          <li><a class="dropdown-item" href="#/Playground">mp_intro</a></li>
                          <li><a class="dropdown-item" href="#/Playground/BinarySearchTree">mp_stickers</a></li>
                          <li><a class="dropdown-item" href="#/Playground/mp_lists">mp_lists</a></li>
                          <li><a class="dropdown-item" href="#/Playground">mp_traversals</a></li>
                          <li><a class="dropdown-item" href="#/Playground">mp_mosaics</a></li>
                          <li><a class="dropdown-item" href="#/Playground">mp_mazes</a></li>
                        </ul>
                    </li>

                    <li class="nav-item dropdown">
                        <a class="nav-link mx-3 dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            Stats
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="#/Labs">Labs</a></li>
                            <li><a class="dropdown-item" href="#/MPs">MPs</a></li>
                            <li><a class="dropdown-item" href="#/Exams">Exams</a></li>
                            <div class="dropdown-divider"></div>
                            <li><a class="dropdown-item" href="#/FinalGrades">Final Grades</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      show: true,
      dropActive: false
    }
  },
  methods: {
    toggleNavbar () {
      this.show = !this.show
    },
    toggleDrop () {
      this.dropActive = !this.dropActive
    }
  },
  components: {
    // DropdownPage
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@100;500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Spartan&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;500;600;700;800&display=swap');

#navbar {
	/* font-family: "Josefin Sans", sans-serif; */
	font-family: "Spartan", sans-serif;
	font-weight: 500;
	letter-spacing: 1px;
	background-color: #002855;
}

#intro-section {
	height: 100vh;
	width: 100vw;
	padding: 2.5% 7.5% 5%;
	font-family: "Montserrat", sans-serif;
}

#intro-section h1 {
	font-size: calc(4em + 1vw);
	font-weight: 700;
}

#intro-section h2 {
	font-size: calc(1em + 1vw);
	font-weight: 600;
	letter-spacing: 2px;
}

#app {
  font-family: "Spartan", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.navbar-nav > li{
  padding-left:30px;
  padding-right:30px;
}

.router-link-exact-active {
        border-bottom: 1px solid #123456;
    }

.router-link-active {
    border: 1px solid #fff;
    color: #fff !important;
  }
</style>
