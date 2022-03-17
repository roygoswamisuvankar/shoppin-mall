import matplotlib.pyplot as plt
from matplotlib import *
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    img_png = buffer.getvalue()
    graph = base64.b64encode(img_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,5))
    plt.title('Sales Items')
    plt.hist(x)
    plt.xticks(rotation=45)
    plt.xlabel('Product Name ')
    plt.ylabel('Product Quantity')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_bar_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7, 5))
    plt.title('Products in Stock')
    plt.bar(x,y)
    addlabels(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Product Name ')
    plt.ylabel('Product Quantity')
    plt.tight_layout()
    graph = get_graph()
    return graph

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

def simplegraph(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7, 5))
    plt.title('Overall sells')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.xlabel('Date increase')
    plt.ylabel('Product Names')
    plt.tight_layout()
    graph = get_graph()
    return graph

def highsell(x):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7, 5))
    plt.title('Highly sells products')
    plt.hist(x)
    plt.xticks(rotation=45)
    plt.xlabel('Products Names')
    plt.ylabel('Highly sells')
    plt.tight_layout()
    graph = get_graph()
    return graph
