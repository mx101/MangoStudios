<template>
  <div id="playground">
  <h3>
    Binary Search Tree
  </h3>
  <BST/>

  <br><br><br>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/_CM7vN1D6dw?start=50" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
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
<style scoped>
    #playground {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
    }
</style>
