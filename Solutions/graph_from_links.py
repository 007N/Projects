"""Graph from links - Create a program that will create a graph or network from a series of links."""
""" I need:
Done - A way to get the first URL, > user input ?
- A way to find the links of the page, > HTML index of the <a> balise ? Regex for http://links ?
- A way to generate the graph, graphical lib to generate the links
    - http://networkx.github.io
    - http://igraph.org
    - http://graph-tool.skewed.de
Done - A way to stop the generation, or a way to generate by step the link.

- Credit :
    - Inspired by https://github.com/grimley517/Projects/blob/graph1/Graphs/GfmLinks.py
"""

from bs4 import BeautifulSoup
import urllib2



first_url = str(
    input("Please enter the link from which you want to start. >> "))
generation_limit = int(input("How many links would you like to follow ? >> "))
generation_step = 0


def checkNode(node, graph):
    '''Checks whether a node is in a graph > Errors could ensue'''
    if node in graph:
        return(True)
    else:
        return (False)


def parse_url(url, limit):
    while generation_step < generation_limit:
        html_web_page = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html_web_page)
        for link in soup.find_all('a'):
            print(link.get('href'))
        find all the links,
        add all the links from the page to the root url list[("http://example.com", "http://example.fr"), ("http://example.com", "http://example.ch"), ("http://example.com", "http://example.us"), ("http://example.com", "http://example.tk")]


def fromLinks(links):
    '''
    Takes a list of links in the form of tuples, or lists,
    with two elements describing the connected nodes and returns a graph in the form of a dictionary.

    Example input: [(1,2),(1,4),(2,3),(3,4)] or [[1,2],[1,4],(,3),(3,4)]

    Example output (fm input): {1:[2,4],2:[1,3],3:[2,4],4:[1,3]}
    '''
    # Set up an empty dictionary
    graph = {}
    # Iterate thru the input nodes
    for link in links:
        # Check if each node is in the graph, if it isnt add it.
        for node in link:
            if not checkNode(node, graph):
                graph[node] = []
        # For both ends of the node add the link to the other
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
    return graph


def create_graph():
    # Take the graph created, with it, do a png image to map the graph of
    # links.
