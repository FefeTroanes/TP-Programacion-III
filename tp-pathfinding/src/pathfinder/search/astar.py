from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Inicializando el nodo con la posicion inicial
        node = Node("", grid.start, 0)

        #Inicializando un diccionario para los explorados
        explored = {}

        #Añadiendo el estado a los explorados con el costo
        explored[node.state] = node.cost

        #Creando la frontera con la clase "Cola Prioridad"
        #,añadiendo el nodo y el costo
        frontera = PriorityQueueFrontier()
        frontera.add(node,node.cost)

        #frontera.add(node,node.cost+h(node))

        #Si no le ponemos la heuristica es identico a ucs
        while not frontera.is_empty():

            nodo = frontera.pop()
            if grid.end==nodo.state:
                return Solution(nodo,explored)

            for accion,estado in grid.get_neighbours(nodo.state).items():
                costo = nodo.cost + grid.get_cost(nodo.state)

                if estado not in explored or costo < explored[estado]:
                    nodo_actual = Node("",estado,costo,nodo,accion)
                    explored[estado] = costo
                    frontera.add(nodo_actual,nodo_actual.cost)

                    #frontera.add(nodo_actual,nodo_actual.cost+h(nodo_actual))

        return NoSolution(explored)
#SOLO FALTA VER LO DE LA HEURISTICA
