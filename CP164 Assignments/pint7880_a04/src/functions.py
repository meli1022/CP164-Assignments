"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-02-06"
------------------------------------------------------------------------
"""

from Graph import Edge, Graph
from Priority_Queue_array import Priority_Queue

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    source._set_first()
    
    n = len(source)
    i = 0
    
    while i < n:
        value = source.remove()
        if value < key:
            target1.insert(value)
        else:
            target2.insert(value)
        
        i += 1
    return target1, target2




def pq_split_alt(source):
    """
    -------------------------------------------------------
    Splits a priority queue into two with values going to alternating
    priority queues. The source priority queue is empty when the method
    ends. The order of the values in source is preserved.
    Use: target1, target2 = pq_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
    Returns:
        target1 - a priority queue that contains alternating values
            from source (Priority_Queue)
        target2 - priority queue that contains  alternating values
            from source (Priority_Queue)
    -------------------------------------------------------
    """
    
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    
    
    while not source.is_empty:
        if not source.is_empty():
            target1.insert(source.remove())
        if not source.is_empty():
            target2.insert(source.remove())
        
    return target1, target2



def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    
    nodes = graph.node_names()
    visited_nodes = []
    
    edge_removed=[]
    edges = Priority_Queue()
    
    pos = 0
    l = len(nodes)
    while pos < (l-1):
        node_edges = graph.edges_by_node(start_node)
        
        for i in node_edges:
            edges.insert(i)
        visited_nodes.append(start_node)
        value = edges.remove()
        edge_removed.append(value)
        
        pos += 1
    distance = 0
    for i in edge_removed:
        distance += i.distance
    edges = edge_removed
    return edges,distance   
    
    