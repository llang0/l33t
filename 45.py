class Node():
    def __init__(self, position, next=None) -> None:
        self.position = position
        self.next = next

    def __str__(self):
        return(f"{self.position} : {self.next}")

    
def jump(nums):
    nodes = []

    for i in range(len(nums)-1, -1, -1):
        if i == len(nums) -1:
            node = Node(i, [])
            nodes.append(node)
        else:
            next = [j + i + 1 for j in range(nums[i])]
            node = Node(i, next)
            nodes.append(node)

    goal = len(nums) - 1
    
    # for i in range(len(nodes)-1, -1, -1):
    #     print(nodes[i])
    # print()


    return search(nodes, goal, 0)


def search(nodes, goal, jumps):
    if goal == 0:
        return jumps
    else:
        for i in range(len(nodes)-1, -1, -1):
            if goal in nodes[i].next:
                # print(nodes[i])
                return search(nodes, nodes[i].position, jumps+1)
    



nums = [2,3,0,1,4]

print(jump(nums))
                
