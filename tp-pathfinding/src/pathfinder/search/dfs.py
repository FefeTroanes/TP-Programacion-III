from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Inicializando el nodo con la posicion inicial
        node = Node("", grid.start, 0)

        #Inicializando un diccionario para los explorados
        explored = {}

        #Añadiendo el estado a los explorados
        explored[node.state] = True

        #Creando la frontera con la clase "Pila" y añadiendo el nodo
        frontera = StackFrontier()
        frontera.add(node)

        #Igual a bfs, lo que cambia es que se usa una pila en vez de una cola
        while not frontera.is_empty():
            nodo = frontera.remove()

            #Test objetivo
            if nodo.state == grid.end:
                return Solution(nodo, explored)

            for accion,nuevo_estado in grid.get_neighbours(nodo.state).items():
                if nuevo_estado not in explored:
                    posible = Node("",nuevo_estado,nodo.cost + grid.get_cost(nodo.state),nodo,accion)
                    if grid.end == nuevo_estado:
                        return Solution(posible,explored)
                    explored[nuevo_estado] = True
                    frontera.add(posible)
        return NoSolution(explored)
