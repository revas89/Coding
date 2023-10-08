class TreeNode:
 def __init__(self, val, left=None, right=None):
   self.val = val
   self.left = left
   self.right = right

class Solution:
  def hasPath(self, root, sum) -> bool:
    if root is None:
        return False
    sum = sum-root.val
    if sum==0 and root.left is None and root.right is None:
        return True

    return self.hasPath(root.left,sum) or self.hasPath(root.right,sum)

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(sol.hasPath(root, 23)))
  print("Tree has path: " + str(sol.hasPath(root, 16)))
  
main()