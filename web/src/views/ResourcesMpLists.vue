<template>
  <div id="playground">
  <h1 style="padding-left:30px;">
    mp_lists
  </h1>
  <h2 style="padding-left:30px;padding-bottom:50px;font-size:40px">
    MP Resources
  </h2>
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
  <h2 style="padding-bottom:50px;font-size:50px">
    Explore
  </h2>
    <div id="jumbotron-container" class="row">
      <a href="#/Playground/PreorderPlayground" class="col me-4">
      <div id="jumbotronHover">
        <h2 style="text-align:center">Preorder Traversal</h2>
      </div>
      </a>

      <a href="#/Playground/InorderPlayground" class="col me-4">
      <div id="jumbotronHover">
        <h2 style="text-align:center">Inorder Traversal</h2>
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
