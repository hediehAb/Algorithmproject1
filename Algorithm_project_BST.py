
import array
import sys

def main():
    tree = BST()
    tree.insert(7)
    tree.insert(4)
    tree.insert(3)
    tree.insert(9)
    tree.insert(5)
    tree.insert(8)
    tree.insert(19)
    print(tree.make_array())
    print(len(tree.array_BST))
    # print(tree.root.left.value)
    # print(tree.array_BST)
    # tree.back_node(8)
    # tree.ahead_node(4) 
    # tree.deletion_node(9, tree.root)
    # tree.print_tree()
 
    tree1 = BST()
    tree1.insert(15)
    tree1.insert(2)
    tree1.insert(17)
    tree1.insert(7)
    tree1.insert(16)
    tree1.insert(20)
    tree1.insert(22)
    tree1.make_array()
    print(tree1.make_array())
    tree.mix(tree1)

    maxheap1 = MaxHeap(30)
    tree.add_to_maxheap(3, maxheap1)


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None
        self.array_BST = array.array("i",[])
        self.tree = []
        
    
    # check for being leaf
    def is_leaf(self,value, curr_node):
        if self.root is None:
            return self.root
        if value < curr_node.value :
            curr_node.left = self.is_leaf(value, curr_node.left)
        elif value > curr_node.value:
            curr_node.right = self.is_leaf(value, curr_node.right)
            
        else:
            return (curr_node.left == None) and (curr_node.right == None)
                
    #insert value
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_node(value, self.root)
    
        
        
    def insert_node(self, value, current_node):
        if value < current_node.value :
            if current_node.left == None:
                current_node.left = Node(value)
            else: 
                self.insert_node(value, current_node.left )
        elif value > current_node.value :
            if current_node.right == None:
                current_node.right = Node(value)
            else:
                self.insert_node(value, current_node.right)
        else:
            print(f"{value} already exist in tree !!!")

    #Make array
    def make_array(self):
        if self.root == None :
            return self.root
        else:
            if self.root.value not in self.array_BST:
                self.array_BST.append(self.root.value)
            self.make_array_(self.root)
        return self.array_BST
        

    def make_array_(self, root):
        if root.left != None:
            if (root.left.value) not in self.array_BST:
                self.array_BST.append(root.left.value)
        if root.right != None:
            if (root.right.value) not in self.array_BST:
                self.array_BST.append(root.right.value)
        if root.left != None:
            self.make_array_(root.left)
        if root.right != None:
            self.make_array_(root.right)

    #print back node of the node
    def back_node(self, value):
        curr_node = self.array_BST.index(value)
        print(self.array_BST[curr_node - 1])
    
    #print ahead nodeof the node
    def ahead_node(self, value):
        curr_node = self.array_BST.index(value)
        print(self.array_BST[curr_node + 1])

    # print tree
    def print_tree(self):
        print("tree: ")
        if self.root != None:
            self.print_tree_(self.root)
            
    
    def print_tree_(self, current_node):
        if current_node != None:
            self.print_tree_(current_node.left)
            print(current_node.value)
            self.tree.append(current_node.value)
            self.print_tree_(current_node.right)

    # deletion node 
    def deletion_node(self, value, curr_node):
        if self.root is None:
            return self.root
        if value < curr_node.value :
            curr_node.left = self.deletion_node(value, curr_node.left)
        elif value > curr_node.value:
            curr_node.right = self.deletion_node(value, curr_node.right)
            
        else:
            if curr_node.left == None:
                return curr_node.right
            elif curr_node.right == None:
                return curr_node.left

            curr_node.value = self.min_node(curr_node.right)

            curr_node.right = self.deletion_node( curr_node.value, curr_node.right)
            self.make_array()

        return curr_node
    
    def min_node(self, curr):
        min = curr.value
        while curr.left:
            min = curr.left.value
            curr = curr.left
        return min

    # mix two BSTs
    def mix(self, tree2):
        result_tree = self
        l = len(tree2.array_BST)
        for i in range(l):
            result_tree.insert(tree2.array_BST[i])
        result_tree.print_tree()


    # k largest nodes add to max heap
    def add_to_maxheap(self, k, maxheap):
        for i in range(1,k+1):
            maxheap.insert(self.tree[(-1 * i)])
        maxheap.print()





class MaxHeap:
 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
 
    def parent(self, node):
        return node // 2
 
    def leftChild(self, node):
        return node * 2
 
    def rightChild(self, node):
        return (node * 2) + 1
 
    def isLeaf(self, node):
        return (node >= (self.size//2) and node <= self.size)
 
    def swap(self, node1, node2):
         self.Heap[node1], self.Heap[node2] = (self.Heap[node2], self.Heap[node1])
 
    def maxHeapify(self, curr_node):
        if self.isLeaf(curr_node) == False:
            if (self.Heap[curr_node] < self.Heap[self.leftChild(curr_node)] or self.Heap[curr_node] < self.Heap[self.rightChild(curr_node)]):
                if (self.Heap[self.leftChild(curr_node)] > self.Heap[self.rightChild(curr_node)]):
                    self.swap(curr_node, self.leftChild(curr_node))
                    self.maxHeapify(self.leftChild(curr_node))
                else:
                    self.swap(curr_node, self.rightChild(curr_node))
                    self.maxHeapify(self.rightChild(curr_node))
 
    def insert(self, new_node):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = new_node
 
        curr_size = self.size
 
        while (self.Heap[curr_size] > self.Heap[self.parent(curr_size)]):
            self.swap(curr_size, self.parent(curr_size))
            curr_size = self.parent(curr_size)
 
    def print(self):
        for i in range(1, (self.size // 2) + 1):
            print(f"PARENT : {str(self.Heap[i])} \nLEFT CHILD : {str(self.Heap[2 * i])} \nRIGHT CHILD : {str(self.Heap[2 * i + 1])}")
 
    def extractMax(self):
 
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
            
        return popped
         

main()