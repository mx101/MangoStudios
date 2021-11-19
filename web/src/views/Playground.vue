<template>
  <div id="playground">
  Playground here
  <br>
  <BST/>
  </div>
</template>

<script>
import BST from "../components/BST.vue"

export default {
  name: 'Playground',
  components: {
    BST
  }
}
</script>
<!-- styling for the component -->
<style>
    #playground {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
    }
</style>
