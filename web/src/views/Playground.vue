<template>
  <div id="playground">
  <h1 style="padding-left:30px;padding-bottom:100px">
    Binary Search Tree
  </h1>
  <div style="text-align:center">

    <div id="jumbotron-container" class="row">
      <div id="jumbotron" class="col">
        <h2>Summary</h2>
        <h3 style="text-align:left">Binary Search alogorithm is an efficent way to locate a node in a binary tree. 
            <br>Utlizing the fact that the binary tree is sorted, the tree compares the value searching for with the value on the node currently on to decide which side of the tree to continue searching.
            <br>
            <br>As such, the area of search is cut in half with every comparison.
            <br>
            <br>For MPs where Binary Search Tree understanding is important, understanding the order of comparison and which nodes would be traversed is most important
            </h3>
      </div>
    </div>
    <BST/>
    <br><br><br>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/_CM7vN1D6dw?start=50" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
  </div>
</template>

<script>
import BST from "../components/BSTTraversal.vue"

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
    /* text-align: center; */
    color: #2c3e50;
    margin-top: 60px;
    }
    #jumbotron-container {
        width: 100%;
        padding: 0% 5% 5% 5%;
    } 
    #jumbotron {
        background-color: #f8fafa;
        text-align: center;
        border-radius: 50px;
        padding: 2% 4%;
        box-shadow: 2px 2px 22px rgba(0, 0, 0, 0.2);
    }
    #playground h1 {
        font-size: calc(4em + 1vw);
        font-weight: 700;
        margin: 0;
    }
    #playground h2 {
        font-size: calc(1em + 1vw);
        font-weight: 600;
        letter-spacing: 2px;
        /* margin: 0; */
    }
    #playground h3 {
        font-size: calc(0.5em + 1vw);
        font-weight: 400;
    }
</style>
