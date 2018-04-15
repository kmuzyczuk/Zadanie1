class v:
	def __init__(self, name, value, parent=None, childs=None):
		self.name=name
		self.parent=parent
		self.value=value
		self.childs=[]
	def CheckRoot(self):     #checks if the node is the root
		if self.parent==None:
			return True
		else:
			return False
	def vChild(self, child1):     #adds a child
		(self.childs).append(child1)
		if child1.CheckRoot==False and child1.parent!=self:
			((child1.parent).childs).remove(child1)
		child1.parent=self
	def vParent(self, parent1):   #sets the parent
		parent1.vChild(self)
	def FindRoot(self):   #finds root no matter in which node we start function
		if self.parent==None:
			return self
		else:
			root=self.parent
			while root.parent!=None:
				root=root.parent
			return root
	def ValueList(self, B=[]):  #creates list with values in the subtree with root=self
		B.append(self.value)
		for child in self.childs:
			child.ValueList(B)
		return B
	def Sum(self):    #counts the sum of values in the subtree
		list1=self.ValueList(B=[])
		sum=0
		for item in list1:
			sum=sum+item
		return sum
	def Average(self):   #calculates the average value in the subtree
		list2=self.ValueList(B=[])
		l=len(list2)
		sum=self.Sum()
		return sum/l
	def Median(self):   #calculates the median in the subtree
		D=self.ValueList(B=[])
		sortD=sorted(D)
		l=len(D)
		if l%2==1:
			x=(l-1)/2
			return sortD[int(x)]
		else:
			x1=l/2
			x2=x1-1
			return (sortD[int(x1)]+sortD[int(x2)])/2
	def SumAverageMedian(self):
		print ("Subtree starting in %s" %(self.name))
		print ("Sum= %f" %(self.Sum()))
		print ("Average= %f" %(self.Average()))
		print ("Median= %f" %(self.Median()))

	
#Test1	
print ("Test1:" )

a=v("A",3)
b=v("B",5,"A")
c=v("C",15,"A")
d=v("D",23,"B")
e=v("E",-4,"B")
f=v("F",2,"C")
g=v("G",34,"A")
h=v("H",-2,"C")
i=v("I",-32,"C")
j=v("J",26,"H")
k=v("K",15,"E")
l=v("L",7,"E")
m=v("M",-4,"D")
e.vChild(k)
e.vChild(l)
d.vChild(m)
a.vChild(b)
a.vChild(c)
b.vChild(d)
b.vChild(e)
c.vChild(f)
a.vChild(g)
c.vChild(h)
c.vChild(i)
h.vChild(j)

b.SumAverageMedian()

root=m.FindRoot()
root.SumAverageMedian()


#Test2
print ("\nTest2:")

a=v("A",1)
b=v("B",54)
c=v("C",125)
d=v("D",-43, None, ["E"])
e=v("E",-8,"D", ["A","B"])
f=v("F",22)
g=v("G",346)
h=v("H",-222)
i=v("I",-132)
j=v("J",260)
k=v("K",0, "J")
l=v("L",1, "J")
m=v("M",-3,"J")
a.vParent(e)
b.vParent(e)
e.vParent(d)
j.vChild(k)
j.vChild(l)
j.vChild(m)
d.vParent(f)
j.vParent(f)
d.vChild(i)
b.vChild(h)
g.vParent(l)

j.SumAverageMedian()
d.SumAverageMedian()


