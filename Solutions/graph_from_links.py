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

from bs4 import *
import urllib2
import time
import re


link_list = []
first_url = str(
    raw_input("Please enter the link from which you want to start. >> "))
generation_limit = int(input("How many links would you like to follow ? >> "))
generation_step = 0
nbr_links = 0


def checkNode(node, graph):
    '''Checks whether a node is in a graph > Errors could ensue'''
    if node in graph:
        return(True)
    else:
        return (False)


def parse_url(url):
    try:
        url_request = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
    else:
        print 'URL is good! Following up...'
        # Use bs4 to get the web page and extract all the links.
        html_web_page = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html_web_page)
        # Need to find all the links that point to a link in the type like http://xxxx/
        for link in soup.find_all("a"):
            if link in link_list:
                print("That link is already registered, passing...")
                time.sleep(0.5)
            else:
                link_list.append(link.get('href'))
                print(link_list)
                time.sleep(0.5)


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
    for link in link_list:
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
    pass


def main(url,step,limit):
    link_list.append(url)
    """for each in enumerate(link_list):
        nbr_links += 1
    """
    while step < limit:
        for each_url in link_list:
            parse_url(each_url)
            step += 1

if __name__ == '__main__':
    main(first_url,generation_step,generation_limit)
