<template>
  <div class="hello">
    Welcome page
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
