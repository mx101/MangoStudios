import { createRouter, createWebHashHistory } from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import About from '@/views/About'
import Playground from '@/views/Playground'
import Exams from '@/views/Exams'
import FinalGrades from '@/views/FinalGrades'
import ResourcesMpLists from '@/views/ResourcesMpLists'
import ResourcesMpTraversal from '@/views/ResourcesMpTraversal'
import ResourcesAll from '@/views/ResourcesAll'

import PreorderPlayground from '@/views/PreorderPlayground'
import MPs from '@/views/MPs'
import InorderPlayground from '@/views/InorderPlayground'
import PostorderPlayground from '@/views/PostorderPlayground'
import BSTPlayground from '@/views/BSTPlayground'

import BFSTreePlayground from '@/views/BFSTreePlayground'
import DFSTreePlayground from '@/views/DFSTreePlayground'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: About
  },
  {
    path: '/Overview',
    name: 'Overview',
    component: About
  },
  {
    path: '/Playground/BinarySearchTree',
    name: 'Playground',
    component: Playground
  },
  {
    path: '/Playground/mp_lists',
    name: 'ResourcesMpLists',
    component: ResourcesMpLists
  },
  {
    path: '/Playground/mp_traversal',
    name: 'ResourcesMpTraversal',
    component: ResourcesMpTraversal
  },  
  {
    path: '/Playground/ResourcesAll',
    name: 'ResourcesAll',
    component: ResourcesAll
  },
  {
    path: '/Playground/PreorderPlayground',
    name: 'PreorderPlayground',
    component: PreorderPlayground
  },  
  {
    path: '/Playground/InorderPlayground',
    name: 'InorderPlayground',
    component: InorderPlayground
  },
  {
    path: '/Playground/PostorderPlayground',
    name: 'PostorderPlayground',
    component: PostorderPlayground
  },
  {
    path: '/Playground/BSTPlayground',
    name: 'BSTPlayground',
    component: BSTPlayground
  },
  {
    path: '/Playground/BFSTreePlayground',
    name: 'BFSTreePlayground',
    component: BFSTreePlayground
  },
  {
    path: '/Playground/DFSTreePlayground',
    name: 'DFSTreePlayground',
    component: DFSTreePlayground
  },
  {
    path: '/Exams',
    name: 'Exams',
    component: Exams
  },
  {
    path: '/FinalGrades',
    name: 'FinalGrades',
    component: FinalGrades
  },
  {
    path:'/MPs',
    name: 'MPs',
    component: MPs
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  linkExactActiveClass: 'is-active'
})

export default router