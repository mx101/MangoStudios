<template>
  <div id="playground">
  <h1 style="padding-left:5%" id="concept">
    mp_lists
  </h1>
  <h2 class="hover" style="padding-left:5%;font-size:40px" v-on:click="testing" id="parentconcept">
    MP Resources
  </h2>
  <div style="text-align:center; padding-top:100px">
    <div id="jumbotron-container" class="row">
      <div id="jumbotron" class="col">
        <h2>Summary</h2>
        <h3 style="text-align:left">Binary Search algorithms is an efficent way to locate a node in a binary tree. 
            <br>Utlizing the fact that the binary tree is sorted, the tree compares the value searching for with the value on the node currently on to decide which side of the tree to continue searching.
            <br>
            <br>As such, the area of search is cut in half with every comparison.
            <br>
            <br>For MPs where Binary Search Tree understanding is important, understanding the order of comparison and which nodes would be traversed is most important
            </h3>
      </div>
    </div>
  <h2 style="padding-bottom:30px; padding-top:30px; font-size:70px">
    Explore
  </h2>
    <div id="jumbotron-container" class="row" style="padding-top:30px;">
      <a href="#/Playground/PreorderPlayground" class="col me-4">
      <div id="jumbotronHover">
        <h2 style="text-align:center">Preorder Traversal</h2>
      </div>
      </a>

      <a href="#/Playground/InorderPlayground" class="col">
      <div id="jumbotronHover">
        <h2 style="text-align:center">Inorder Traversal</h2>
      </div>
      </a>
    </div>
    <div id="jumbotron-container" class="row" style="padding-bottom:60px;">

      <a href="#/Playground/BSTPlayground" class="col me-4">
      <div id="jumbotronHover">
        <h2 style="text-align:center">Binary Search Tree</h2>
      </div>
      </a>
      <a href="#/Playground/PostorderPlayground" class="col">
      <div id="jumbotronHover">
        <h2 style="text-align:center">Postorder Traversal</h2>
      </div>
      </a>
    </div>
  </div>
  </div>
</template>

<script>
import * as d3 from 'd3'

export default {
  name: 'Playground',

  mounted() {
    window.scrollTo(0, 0)
  },
  methods: {
    testing() {
      d3.select("#concept")
        .style("opacity", 1)
        .transition()
        .duration(500)
        .style("opacity", 0)
        .style('font-size', '0px')
        .transition()
        .duration(100)
        .on("end", function() {window.location.href = "#/Playground/ResourcesAll"});

      d3.select("#parentconcept")
        .attr('text-anchor', 'middle')
        .style('font-size', 'calc(2em + 1vw)')
        .style('font-weight', '600')
        .style('background', 'white')
        .transition()
        .duration(200)
        .style('font-size', 'calc(4em + 1vw)')
        .style('font-weight', '700')
        .style('letter-spacing', '0px')
        
    }
  }
}
</script>

<style scoped>
    #playground {
    font-family: "Montserrat", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /* text-align: center; */
    color: #2c3e50;
    margin-top: 60px;
    }
    #jumbotron-container {
        width: 100%;
        padding: 0% 5% 2% 5%;
    } 
    #jumbotron {
        background-color: #f8fafa;
        text-align: center;
        border-radius: 50px;
        padding: 2% 4%;
        box-shadow: 2px 2px 22px rgba(0, 0, 0, 0.2);
    }
    #jumbotronHover {
        height: 300px;
        background-color: #002855;
        background-image: url("../assets/button-background.png");
        background-position: center  !important;
        background-repeat: no-repeat   !important;
        background-size: cover   !important;

        text-align: center;
        border-radius: 50px;
        padding: 130px 0;
        box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.2);

        transition: 0.5s;
    }
    #jumbotronHover h2 {
        color: white;
    }

    #jumbotronHover:hover h2 {
        color: white;
        
    }

    #jumbotronHover:hover {
        background-color: #00AFDA;
        background-image: url("../assets/button-background-hover.png");
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

    #playground h2.mini {
        background:Gainsboro;
        font-size: calc(2em + 1vw);
        font-weight: 600;
        letter-spacing: 2px;
        transition: 0.3s;
        /* margin: 0; */
    }

    #playground h2.hover {
        background:Gainsboro;
        font-size: calc(2em + 1vw);
        font-weight: 600;
        letter-spacing: 2px;
        transition: 0.3s;
        /* margin: 0; */
    }
    #playground h2.hover:hover {
        color:lightseagreen;
        background:lightgray;
        cursor: pointer;
    }

    #playground h3 {
        font-size: calc(0.5em + 1vw);
        font-weight: 400;
    }
    #playground a {
      color: inherit;
      text-decoration: none;
    }
</style>