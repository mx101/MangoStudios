<template>
  <div id="playground">
  <h1 style="padding-left:30px" id="concept">
    Depth First Search Binary Tree
  </h1>
  <h2 class="hover" style="padding-left:30px;font-size:40px" v-on:click="testing" id="parentconcept">
    mp_traversal
  </h2>

  <div style="text-align:center; padding-top:100px">

    <div id="jumbotron-container" class="row">
      <div id="jumbotron" class="col">
        <h2>Summary</h2>
        <h3 style="text-align:left">
            Depth First Search (DFS) is a way to search trees and graphs for a value.
            <br>It is especially useful when the tree/graph is not sorted
            <br>
            <br>A key attribute of DFS is that it will always search extremly deep
            <br>As such, this is better for deeper trees and graphs
            </h3>
      </div>
    </div>
    <BST/>
    <br><br><br>
  </div>
  </div>
</template>

componentDidMount() {
  window.scrollTo(0, 0)
}

<script>
import BST from "../components/DFSTree.vue"
import * as d3 from 'd3'

export default {
  name: 'Playground',
  components: {
    BST
  },
  mounted() {
    window.scrollTo(0, 0)
  },
  methods: {
    testing() {
      console.log("test")
      
      d3.select("#concept")
        .style("opacity", 1)
        .transition()
        .duration(500)
        .style("opacity", 0)
        .style('font-size', '0px')
        .transition()
        .duration(100)
        .on("end", function() {window.location.href = "#/Playground/mp_traversal"});

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
        .style('padding-left', '30px')
        
    }
  }
}
</script>
<!-- styling for the component -->
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
</style>