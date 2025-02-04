import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPath(root, path, k):
    if root is None:
        return False
    path.append(root)
    if root.data == k or findPath(root.left, path, k) or findPath(root.right, path, k):
        return True
    path.pop()
    return False

def lca(root, n1, n2):
    path1 = []
    path2 = []
    if not findPath(root, path1, n1) or not findPath(root, path2, n2):
        return None
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

def find_lca():
    try:
        n1 = int(entry1.get())
        n2 = int(entry2.get())
        ans = lca(root, n1, n2)
        if ans is None:
            messagebox.showinfo("Result", "No common ancestor found")
        else:
            messagebox.showinfo("Result", f"The LCA of {n1} and {n2} is {ans.data}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integers")

def visualize_tree():
    G = nx.DiGraph()
    add_edges(G, root)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=15, font_color="black", font_weight="bold", arrows=True)
    canvas.draw()

def add_edges(G, node):
    if node is not None:
        if node.left:
            G.add_edge(node.data, node.left.data)
            add_edges(G, node.left)
        if node.right:
            G.add_edge(node.data, node.right.data)
            add_edges(G, node.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(8)
    root.left.right.right = Node(9)
    root.right.left = Node(6)
    root.right.right = Node(7)

    app = tk.Tk()
    app.title("LCA Finder")

    tk.Label(app, text="Enter first node:").grid(row=0, column=0)
    entry1 = tk.Entry(app)
    entry1.grid(row=0, column=1)

    tk.Label(app, text="Enter second node:").grid(row=1, column=0)
    entry2 = tk.Entry(app)
    entry2.grid(row=1, column=1)

    tk.Button(app, text="Find LCA", command=find_lca).grid(row=2, column=0, columnspan=2)

    fig = plt.figure(figsize=(5, 4))
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

    tk.Button(app, text="Visualize Tree", command=visualize_tree).grid(row=4, column=0, columnspan=2)

    app.mainloop()
