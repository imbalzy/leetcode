class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        a=[root]
        while a:
            b=a
            a=[]
            for node in b:
                if node.left:
                    a.append(node.left)
                if node.right:
                    a.append(node.right)
            for i in range(len(a)-1):
                a[i].next=a[i+1]
        return root
