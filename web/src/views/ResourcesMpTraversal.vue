<template>
  <div id="playground">
  <h1 style="padding-left:30px;">
    mp_traversal
  </h1>
  <h2 style="padding-left:30px;padding-bottom:50px;font-size:40px">
    MP Resources
  </h2>
  <div style="text-align:center">
    <div id="jumbotron-container" class="row">
      <div id="jumbotron" class="col">
        <h2>Summary</h2>
        <h3 style="text-align:left">Binary Search alogorithm is an efficent way to locate a node in a binary tree. 
            <br>This is stuff relating to mp mp_traversals
            <br>This mp's goal are these and you need to know these techniques.
            </h3>
      </div>
    </div>
  <h2 style="padding-bottom:50px;font-size:50px">
    Explore
  </h2>
    <div id="jumbotron-container" class="row">
      <a href="#/Playground/BFSTreePlayground" class="col me-4">
      <div id="jumbotronHover">
        <h2 style="text-align:center">BFS Tree Visualization</h2>
      </div>
      </a>

      <a href="#/Playground/DFSTreePlayground" class="col">
      <div id="jumbotronHover">
        <h2 style="text-align:center">DFS Tree Visualization</h2>
      </div>
      </a>
    </div>
  </div>
  </div>
</template>

mounted () {
  window.scrollTo(0, 0)
}

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
    #jumbotronHover {
        height: 300px;
        background-color: #A7C7E7;
        text-align: center;
        border-radius: 50px;
        padding: 130px 0;
        box-shadow: 2px 2px 22px rgba(0, 0, 0, 0.2);
        transition: 0.3s;
    }
    #jumbotronHover:hover {
        box-shadow: 2px 2px 22px rgba(0, 0, 0, 0.8);
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
    #playground a {
      color: inherit;
      text-decoration: none;
    }
</style>
