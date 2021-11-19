<template>
  <div>
    <form>
      <input name="input" type="number" value="50" step="1" min="0" max="99" autocomplete="off" style="width: auto; font-size: 1em;"> 
      <input name="submit" type="submit" style="margin: 0 0.75em" value="Watch Search" v-on:click="animate_path">
    </form>
    <div id="bst" />
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

  inorder(node) {
    if (node !== null) {
      this.inorder(node.left)
      console.log(node.value)
      this.inorder(node.right)
    }
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


export default {
  name: 'BST',
  data: () =>({
    tree_:null
  }),
  components: {

  },
  mounted() {
    this.generate_bst()
  },
  methods: {
    animate_path() {
      /*var svg = d3.select("#bst")
      var searchFor1 = 24
      
      if(searchFor1) {
        var path = this._tree.getSearchPath(searchFor1);
        // var recurs1 = path.length
        var pathNodes = nodes.filter(n => path.includes(n.value))
        var pathLinks = links.filter(l => path.includes(l.value))
        
        for(let j = 0; j < path.length; j++) {
          g
          .selectAll('line.path')
          .data(pathLinks)
          .enter()
          .append('line')
          .attr('class', 'path')
          .attr('x1', d => d.parent.x)
          .attr('y1', d => d.parent.y)
          .attr('x2', d => d.x)
          .attr('y2', d => d.y)
          .attr('stroke', 'steelblue')
          .attr('stroke-width', 2)
          .attr('stroke-dasharray', d => length(d))
          .attr('stroke-dashoffset', d => length(d))
          .transition()
          .duration(500)
          .delay((d, i) => i * 500 + 1000)
          // .attr('stroke-dashoffset', d => 0)

        g
          .selectAll('circle.path')
          .data(pathNodes)
          .enter()
          .append('circle')
          .attr('class', 'path')
          .attr('r', radius)
          .attr('fill', '#FFF')
          .attr('transform', d => `translate(${d.x},${d.y})`)
          .attr('stroke', 'steelblue')
          .attr('stroke-width', 2)
          .attr('stroke-dasharray', 2 * Math.PI * radius)
          .attr('stroke-dashoffset', 2 * Math.PI * radius)
          .transition()
          .duration(500)
          .delay((d, i) => i * 500)
          .attr('stroke-dashoffset', 0)
          
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
        }
      }
      
      return svg.node() */
    },
    generate_bst() {
      const width = 800
      const height = 600
      const margin = 20
      const radius = 10
      
      const bst = new BinarySearchTree()
      const data = d3.shuffle(d3.range(0, 100))
      
      data.forEach(d => {
        bst.insert(d)
      })
      
      const tree = d3.tree().size([width, height])
      const root = d3.hierarchy(bst.root, function(d) {
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
      this.tree = bst
      
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

      var searchFor1 = 24
      
      if(searchFor1) {
        var path = bst.getSearchPath(searchFor1);
        // var recurs1 = path.length
        var pathNodes = nodes.filter(n => path.includes(n.value))
        var pathLinks = links.filter(l => path.includes(l.value))
        
        for(let j = 0; j < path.length; j++) {
          g
          .selectAll('line.path')
          .data(pathLinks)
          .enter()
          .append('line')
          .attr('class', 'path')
          .attr('x1', d => d.parent.x)
          .attr('y1', d => d.parent.y)
          .attr('x2', d => d.x)
          .attr('y2', d => d.y)
          .attr('stroke', 'steelblue')
          .attr('stroke-width', 2)
          .attr('stroke-dasharray', d => length(d))
          .attr('stroke-dashoffset', d => length(d))
          .transition()
          .duration(500)
          .delay((d, i) => i * 500 + 1000)
          // .attr('stroke-dashoffset', d => 0)

        g
          .selectAll('circle.path')
          .data(pathNodes)
          .enter()
          .append('circle')
          .attr('class', 'path')
          .attr('r', radius)
          .attr('fill', '#FFF')
          .attr('transform', d => `translate(${d.x},${d.y})`)
          .attr('stroke', 'steelblue')
          .attr('stroke-width', 2)
          .attr('stroke-dasharray', 2 * Math.PI * radius)
          .attr('stroke-dashoffset', 2 * Math.PI * radius)
          .transition()
          .duration(500)
          .delay((d, i) => i * 500)
          .attr('stroke-dashoffset', 0)
          
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
        }
      }
      
      return svg.node()
    }
  }
}
</script>