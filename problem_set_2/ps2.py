# 6.0002 Problem Set 5
# Graph optimization
# Name: Aloisio Valério
# Collaborators: None
# Time: 1h40

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? 
# A: Nodes represent buildings
# 
# What do the graph's edges represent?
# A: Edges represent paths between buildings
# 
# Where are the distances represented?
# A: Distances are represented in edges, as an attribute
#


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    print("Loading map from file...")

    map_digraph = Digraph()

    file = open(map_filename, encoding="utf-8")

    for line in file:
        line = line.strip('\n')
        split_line = line.split(" ")
        
        src = Node(split_line[0])
        dest = Node(split_line[1])
        edge = WeightedEdge(src, dest, split_line[2], split_line[3])

        if (not map_digraph.has_node(src)):
            map_digraph.add_node(src)
        
        if (not map_digraph.has_node(dest)):
            map_digraph.add_node(dest)
        
        map_digraph.add_edge(edge)      


    file.close()

    return map_digraph

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out
# test = load_map("test_load_map.txt")
# print(test)

#
# Problem 3: Finding the Shortest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer: Objective function is minimize distance travelled. 
# Contraints are the maximum outdoors and total distances and possible paths.
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    # TODO
    if (not (digraph.has_node(start) and digraph.has_node(end))):
        raise ValueError
    elif start == end:
        print("Update global variables appropriately - whatever that means - is it finishing the loop?")
    else:
        for edge in digraph.get_edges_for_node(start):
            print('Do something, bro!')
            # current_path = [[start.get_node(), ]]
            # construct a path including that node
            # recursively solve the rest of the path, from the child node to the end node
    
    shortest_path = None

    return shortest_path
    '''
    if start and end are not valid nodes:
        raise an error
    elif start and end are the same node:
        update the global variables appropriately
    else:
        for all the child nodes of start
            construct a path including that node
            recursively solve the rest of the path, from the child node to the end node
    
    return the shortest path
    '''

a = Node('a')
b = Node('b')
c = Node('c')

a_b = WeightedEdge(a, b, 10, 5)
b_c = WeightedEdge(b, c, 15, 2)
a_c = WeightedEdge(a, c, 12, 8)

test = Digraph()

test.add_node(a)
test.add_node(b)
test.add_node(c)

test.add_edge(a_b)
test.add_edge(b_c)
test.add_edge(a_c)

print(test.has_node(a))
print(test)
print(test.get_edges_for_node(a))

# print(get_best_path(test, a, b, [], 10, None, None))


# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    # TODO
    pass


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)

'''
if __name__ == "__main__":
    unittest.main()
'''