from Tkinter import *
# import testing
from Capictor import *
from Node import *



class GUI:
    def __init__(self, root):
        self.variable = True
        frame = Frame(root)
        frame.pack()
        root.wm_title("Calculate This!")
        self.addSeries = Button(root, text="Add a capacitor!")
        self.calculatefun = Button(root, text="Calc")
        self.changeB = Button(root, text="Change")
        self.clearB = Button(root, text="CLEAR")
        self.moveB = Button(root, text="MOVE")
        # pack
        self.addSeries.pack()
        self.calculatefun.pack()
        self.changeB.pack()
        self.clearB.pack()
        self.moveB.pack()

        # Bind
        self.calculatefun.bind("<Button-1>", lambda event: printCap(event, listNode[0]))
        self.addSeries.bind("<Button-1>", lambda event: addB(event, listNode[len(listNode) - 1]))
        self.changeB.bind("<Button-1>", self.change)
        self.clearB.bind("<Button-1>", lambda event: clearNode(event, listNode[0]))
        self.moveB.bind("<Button-1>", self.move_to_node)

        self.S = Scrollbar(root, orient=HORIZONTAL)
        self.T = Text(root)
        self.T.pack(side=RIGHT, fill=Y)
        self.S.config(command=self.T.xview)
        self.T.config(xscrollcommand=self.S.set)
        self.T.config(wrap=NONE)
        quote = "Hello World----------------------------------------------------------------"
        self.T.insert(END, quote)
        self.T.see(END)

    def addText(self, text):
        self.T.insert(END, text)
        self.T.see(END)

    def change(self, event):
        print("Change")
        # Changing from Series to Parallel
        if self.variable:
            listNode.append(Node())
            listNode[0].append_a_node(Node('S',listNode[1]))
            self.addSeries.configure(text="ADD Parallel")
            self.addSeries.bind("<Button-1>", lambda event: addP(event, listNode[len(listNode) - 1]))
        # Changing from  Parallel to Series
        else:
            self.addSeries.configure(text="ADD Series")
            self.addSeries.bind("<Button-1>", lambda event: addB(event, listNode[len(listNode) - 1]))
        self.variable = not self.variable

    def move_to_node(self, event):
        print("move")
        del listNode[len(listNode)-1]
        if self.variable:
            self.addSeries.configure(text="ADD Parallel")
            self.addSeries.bind("<Button-1>", lambda event: addP(event, listNode[len(listNode) - 1]))
        # Changing from  Parallel to Series
        else:
            self.addSeries.configure(text="ADD Series")
            self.addSeries.bind("<Button-1>", lambda event: addB(event, listNode[len(listNode) - 1]))
        self.variable = not self.variable
        self.variable = not self.variable


def clearNode(event, nodeVar):
    nodeVar = Node()
    listNode[0] = nodeVar
    print ("CLEAR called")


def printCap(event, nodeVar):
    print ("Calculate Clicked")
    print("final ecap is " + str(calculate(nodeVar)))
    # while node is not None:
    #     print (str(node))
    #     node = node.next


def addP(event, node_var):
    if node_var.cargo is None:
        node_var.set_value('P', 10)
    else:
        node_var.append_a_node(Node('P', 10))
    print (str(node_var))
    return node_var


def addB(event, node_var):
    print("Add series Called")
    if node_var.cargo is None:
        node_var.set_value('S', 10)
    else:
        node_var.append_a_node(Node('S', 10))
    print (str(node_var))
    return node_var


# node = Node()
listNode = [Node()]
root = Tk()
b = GUI(root)
b.addText("Hello World?")
root.mainloop()
