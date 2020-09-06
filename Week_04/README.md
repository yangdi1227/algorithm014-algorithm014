### 总结：

本周内容主要涉及到三个知识点：树的历遍，主要形式为 DFS, BFS，重新加固了一下。学习了一下贪心算法，就是每一步都是局部最优以求全局最优。最大确定是并不是总是全局最优，且不能改已经走过的路线，这个缺点将在 DP 的部分进行修正。二分法，市那大特点，有序，单调性，有下标。

#### DFS, BFS 的模板

```
#DFS
visited = set()

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited
    	return

	visited.add(node)

	# process current node here.
	...
	for next_node in node.children():
		if next_node not in visited:
			dfs(next_node, visited)

#非递归写法，需要手动维护一个栈
def DFS(self, tree):

	if tree.root is None:
		return []

	visited, stack = [], [tree.root]

	while stack:
		node = stack.pop()
		visited.add(node)

		process (node)
		nodes = generate_related_nodes(node)
		stack.push(nodes)

	# other processing work
	...
#BFS 模板
# Python
def BFS(graph, start, end):
    visited = set()
	queue = []
	queue.append([start])
	while queue:
		node = queue.pop()
		visited.add(node)
		process(node)
		nodes = generate_related_nodes(node)
		queue.push(nodes)
	# other processing work
	...
```

#### 二分查找代码：

二分查找, 二分法，市那大特点，有序，单调性，有下标。应用方向为快排，找数值等等。需要注意旋转的二分算法。eg.

```
# Python
left, right = 0, len(array) - 1
while left <= right:
	  mid = (left + right) / 2
	  if array[mid] == target:
		    # find the target!!
		    break or return result
	  elif array[mid] < target:
		    left = mid + 1
	  else:
		    right = mid - 1
```

#### 回溯:

贪心算法，用的不多，有利于对 DP 的理解