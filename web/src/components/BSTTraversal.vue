<template>
  <div>
    <div style="display: flex; justify-content: center; align-items: center;">
      <button class="btn btn-primary" name="submit" type="submit" style="margin: 0 0.75em" value="Watch Search" v-on:click="animate_path">Watch Preorder Traversal</button>
    </div>

    <br>
    <div id="traversalstring" style="display: flex; justify-content: center; align-items: center;"/>
    <br>
    <div id="bst" style="display: flex; justify-content: center; align-items: center;"/>
  </div>
</template>

<script>

import * as d3 from 'd3'
class BinarySearchTree {
  constructor() {
    this.root = null
    this.path = []
  }

  insert(value) {
    var newNode = new Node(value)

    if (this.root === null) {
      this.root = newNode
    } else {
      this.insertNode(this.root, newNode)
    }
  }

  insertNode(node, newNode) {
    if (newNode.value < node.value) {
      if (node.left === null) {
        node.left = newNode
      } else {
        this.insertNode(node.left, newNode)
      }
    } else {
      if (node.right === null) {
        node.right = newNode
      } else {
        this.insertNode(node.right, newNode)
      }
    }
  }

  remove(value) {
    this.root = this.removeNode(this.root, value)
  }

  removeNode(node, key) {
    if (node === null) {
      return null
    } else if (key < node.value) {
      node.left = this.removeNode(node.left, key)
      return node
    } else if (key > node.value) {
      node.right = this.removeNode(node.right, key)
      return node
    } else {
      if (node.left === null && node.right === null) {
        node = null
        return node
      }
      if (node.left === null) {
        node = node.right
        return node
      } else if (node.right === null) {
        node = node.left
        return node
      }
      var aux = this.findMinNode(node.right)
      node.value = aux.value
      node.right = this.removeNode(node.right, aux.value)
      return node
    }
  }

  findMinMode(node) {
    if (node.left === null) {
      return node
    } else {
      return this.findMinNode(node.left)
    }
  }

  getRootNode() {
    return this.root
  }

  inorder(node, initial = false) {
    if (initial) {
      this.path = []
    }
    if (node !== null) {
      this.inorder(node.left)
      this.path.push(node.value)
      this.inorder(node.right)
    }
  }

  getInorder() {
    this.inorder(this.root, true)
    return this.getPath()
  }

  preorder(node, initial = false) {
    if (initial) {
      this.path = []
    }
    if (node !== null) {
      this.path.push(node.value)
      this.preorder(node.left)
      this.preorder(node.right)
    }
  }

  getPreorder() {
    this.preorder(this.root, true)
    return this.getPath()
  }

  postorder(node, initial = false) {
    if (initial) {
      this.path = []
    }
    if (node !== null) {
      this.postorder(node.left)
      this.postorder(node.right)
      this.path.push(node.value)
    }
  }

  getPostorder() {
    this.postorder(this.root, true)
    return this.getPath()
  }

  search(node, value, initial = false) {
    if (initial) {
      this.path = []
    }
    if (node === null) {
      return null
    } else if (value < node.value) {
      this.path.push(node.value)
      return this.search(node.left, value)
    } else if (value > node.value) {
      this.path.push(node.value)
      return this.search(node.right, value)
    } else {
      this.path.push(node.value)
      return node
    }
  }

  getPath() {
    return this.path
  }

  getSearchPath(value) {
    this.search(this.root, value, true)
    return this.getPath()
  }
}

class Node {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

// function special_length (d) {
//   return Math.sqrt(Math.pow(d.parent.x - d.x, 2) + Math.pow(d.parent.y - d.y, 2))
// }

export default {
  name: 'BST',
  data: () =>({
    tree_:null,
    search_value: 50
  }),
  components: {

  },
  mounted() {
    this.generate_bst()
  },
  methods: {
    clear_path() {
      const margin = 20
      var svg = d3.select("#bst")
      var g = svg
        .select('g')
        .attr('transform', `translate(${margin},${margin})`)
      
      g.selectAll("line.path").remove()
      g.selectAll("circle.path").remove()
      g.selectAll('text.path').remove()
    },
    pretraversal_recursion(curr_node) {
      if (curr_node == null) {
        return
      }
      console.log("Node Value", curr_node.value)
    },
    animate_path() {
      d3.select("#traversalstring").selectAll("*").remove();
      this.clear_path()
      const width = 800
      const height = 600
      const radius = 14
      const margin = 40
      const tree = d3.tree().size([width, height])
      this.tree_.inorder(this.tree_.root)

      const root = d3.hierarchy(this.tree_.root, function(d) {
        d.children = []
        if(d.left) {
          d.children.push(d.left)
        }
        if(d.right) {
          d.children.push(d.right)
        }
        return d.children
      })
      
      root.x0 = width / 2
      root.y0 = 0
      
      var treeData = tree(root)
      var nodes = treeData.descendants()
      var svg = d3.select("#bst")
      var g = svg
        .select('g')
        .attr('transform', `translate(${margin},${margin})`);
      var path = this.tree_.getPreorder();
      var pathNodes = nodes.filter(n => path.includes(n.data.value)).sort(function(a, b){
          var ai = 0;
          for(let k = 0; k < path.length; k++) {
            if (path[k] == a.data.value) {
              ai = k;
              break;
            }
          }

          var bi = 0;
          for(let k = 0; k < path.length; k++) {
            if (path[k] == b.data.value) {
              bi = k;
              break;
            }
          }
          return d3.ascending(ai, bi);
      })

      for(let k = 0; k < path.length - 1; k++) {
        d3.select("#traversalstring").append('traversalstring' + k)
        .text(path[k] + ', ')
        .style("opacity", 0)
        .style('font-size', '0px')
        .transition()
        .duration(500)
        .delay((k)*500)
        .style("opacity", 1)
        .style('font-size', '24px')
        .transition()
        .duration(29*500 + 1000 - k * 500)
        .transition()
        .duration(500)
        .style("opacity", 0)
        .remove()
      }
      d3.select("#traversalstring").append('traversalstringlast')
        .text(path[path.length - 1] + '')
        .style("opacity", 0)
        .style('font-size', '0px')
        .transition()
        .duration(500)
        .delay((29)*500)
        .style("opacity", 1)
        .style('font-size', '24px')
        .transition()
        .duration(1000)
        .transition()
        .duration(500)
        .style("opacity", 0)
        .remove()
        
      console.log("nodes", pathNodes)
      g
        .selectAll('circle.path')
        .data(pathNodes)
        .enter()
        .append('circle')
        .attr('class', 'path')
        .attr('r', radius)
        .attr('fill', '#FFF')
        .attr('transform', d => `translate(${d.x},${d.y})`)
        .attr('stroke', function(d, i) {
            if (i !== path.length - 1) {
              return 'steelblue';
            } else {
              return 'lawngreen';
            }  
        })
        .attr('stroke-width', 3)
        .attr('stroke-dasharray', 2 * Math.PI * radius)
        .attr('stroke-dashoffset', 2 * Math.PI * radius)
        .transition()
        .duration(500)
        .delay(function(d, i) {
            return i * 500;
        })
        .attr('stroke-dashoffset', 0)
        .transition()
        .duration(function(d, i) {
            return (path.length - 1)*500 + 1000 - i * 500;
        })
        .transition()
        .duration(500)
        .attr('stroke-dashoffset', 2 * Math.PI * radius)
        
      g.selectAll('text.path')
        .data(pathNodes)
        .enter()
        .append('text')
        .attr('class', 'path')
        .attr('text-anchor', 'middle')
        .attr('alignment-baseline', 'middle')
        .attr('transform', d => `translate(${d.x},${d.y + 1})`)
        .style('font-size', '14px')
        .text(d => d.data.value)
  
      return svg.node()
    },
    generate_bst() {
      const width = 800
      const height = 600
      const margin = 40
      const radius = 14
      
      this.tree_ = new BinarySearchTree()
      const data = d3.shuffle(d3.range(0, 30))
      
      data.forEach(d => {
        this.tree_.insert(d)
      })
      
      const tree = d3.tree().size([width, height])
      const root = d3.hierarchy(this.tree_.root, function(d) {
        d.children = []
        if(d.left) {
          d.children.push(d.left)
        }
        if(d.right) {
          d.children.push(d.right)
        }
        return d.children
      })
      
      root.x0 = width / 2
      root.y0 = 0
      
      var treeData = tree(root)
      var nodes = treeData.descendants()
      var links = treeData.descendants().slice(1)
      
      var svg = d3
        .select("#bst")
        .append('svg')
        .attr('width', width + margin * 2)
        .attr('height', height + margin * 2)

      var g = svg
        .append('g')
        .attr('transform', `translate(${margin},${margin})`)


      var link = g
        .selectAll('line.link')
        .data(links)
      
      var linkEnter = link
        .enter()
        .append('line')
        .attr('class', 'link')
        .attr('data-value', d => d.data.value)
        .attr('x1', d => d.parent.x)
        .attr('y1', d => d.parent.y)
        .attr('x2', d => d.x)
        .attr('y2', d => d.y)
        .attr('stroke', '#ddd')
        .attr('stroke-dasharray', '4px 8px')
      console.log(linkEnter)
      
      var node = g
        .selectAll('g.node')
        .data(nodes)
      
      var nodeEnter = node
        .enter()
        .append('g')
        .attr('class', 'node')
      
      nodeEnter
        .append('circle')
        .attr('data-value', d => d.data.value)
        .attr('r', radius)
        .attr('fill', '#FFF')
        .attr('stroke', '#ddd')
        .attr('transform', d => `translate(${d.x},${d.y})`)
      
      nodeEnter
        .append('text')
        .attr('text-anchor', 'middle')
        .attr('alignment-baseline', 'middle')
        .attr('transform', d => `translate(${d.x},${d.y + 1})`)
        .style('font-size', '14px')
        .text(d => d.data.value)
      // this.animate_path()


      return svg.node()
    }
  }
}
</script>