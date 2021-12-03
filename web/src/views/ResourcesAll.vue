<template>
  <div id="playground">
  <h1 style="padding-left:30px;">
    MP Resources
  </h1>
  <div style="text-align:center; padding-top:100px;">
    <div id="jumbotron-container" class="row">
      <div id="jumbotron" class="col">
        <h2>Summary</h2>
        <h3 style="text-align:left">
            <br>Mps contain a lot of algorithms and complex ideas.
            <br>Within this page contains major conceptual ideas that are present in mps in this class
            <br>
            <br>To help with these tough conceptual ideas, explore visualizations to help visualize what is occuring with these algorithms
            </h3>
      </div>
    </div>
    <a href="#/Playground/mp_lists" class="col me-4">
      <h2 style="padding-bottom:10px; padding-top:10px; font-size:50px" class="hover">
        mp_lists
      </h2>
    </a>
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

    <a href="#/Playground/mp_traversal" class="col me-4">
      <h2 style="padding-bottom:10px; padding-top:10px; font-size:50px" class="hover">
        mp_traversal
      </h2>
    </a>
    <div id="jumbotron-container" class="row" style="padding-top:30px; padding-bottom:100px;">
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

<script>

export default {
  name: 'Playground',
  mounted() {
    window.scrollTo(0, 0)
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
