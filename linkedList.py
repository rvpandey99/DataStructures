class Node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=Node()

	def append(self,data):
		newNode=Node(data)
		curNode=self.head
		while curNode.next!=None:
			curNode=curNode.next
		curNode.next=newNode

	def length(self):
		total=0
		curNode=self.head
		while curNode.next!=None:
			curNode=curNode.next
			total+=1
		return total

	def display(self):
		l=[]
		curNode=self.head
		while curNode.next!=None:
			curNode=curNode.next
			l.append(curNode.data)
		print(l)