from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary with the initial state
        explored = {}
        explored[node.state] = True

        # Return if the node contains a goal state
        if node.state == grid.end:
            return Solution(node, explored)

        # Initialize the frontier (a queue) with the initial node
        frontier = QueueFrontier()
        frontier.add(node)

        while True:
            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            current_node = frontier.remove()

            # BFS
            # Check if the current node contains a goal state
            if current_node.state == grid.end:
                return Solution(current_node, explored)

            successors = grid.get_neighbours(current_node.state).items()
            for action, neighbour_state in successors:
                if neighbour_state not in explored:
                    # Create a new neighbour
                    # new_neighbour = Node("", neighbour_state, sum(current_node.cost, grid.get_cost(neighbour_state)), current_node, action)

                    neighbour_node = Node("", neighbour_state , current_node.cost + grid.get_cost(neighbour_state), parent=current_node, action=action)
                    frontier.add(neighbour_node)
                    explored[neighbour_state] = True
        return NoSolution(explored)
