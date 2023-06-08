###빈껍데기 노드 틀 생성! : data를 가지고, 양쪽 다리가 None인 노드 ###
class Node: #루트가 data인 Node

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0  #해당 노드를 root로 가지는 트리의 hieght. AVL에서 BF비교를 위해 필요

###AVL 시작###
class AVL : #금쪽이들만 오는 공간임.
    def __init__(self):
        self.root = None #그래서 시작할 땐 없음. 채워 넣으면서 AVL 시작. root Node로 이름지어 부르기 가능
        #매번 삽입이 아니라, .root를 불러와서 바꿔줘야함.
    
    def height(self, node):
        if node == None: #노드가 없으면 높이가 없지요? 오류 방지를 위해, 정의에 맞게 설정해줍니다.
            return -1
        else :
            return node.height #AVL.height = node.height 정상이면, 루트 노드로부터의 높이를 이야기합니다.

    def balance(self, node):
        return self.height(node.left)-self.height(node.right)
    
    ##일반적으로 삽입하는 경우
    def insert(self, node, data): #이때 node는 root를 의미함
        if node == None:
            return Node(data) #빈자리면 해당 자리에 노드 생성할게요~
        if node.data < data :
            node.right = self.insert(node.right, data)
        if node.data > data :
            node.left = self.insert(node.left, data)