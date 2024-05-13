from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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

        #Lo unico que cambia a bfs y dfs es que se le agrega el costo por lo tanto
        #se usa cola por prioridad
        while not frontera.is_empty():
            nodo = frontera.pop()
            #Test objetivo
            if grid.end==nodo.state:
                return Solution(nodo,explored)

            for accion,estado in grid.get_neighbours(nodo.state).items():

                #Creamos el costo para despues compararlo con el costo del nuevo estado
                costo = nodo.cost + grid.get_cost(nodo.state)
                if estado not in explored or costo < explored[estado]:
                    nodo_actual = Node("",estado,costo,nodo,accion)

                    #Agregamos a los exlorados el estado con su costo
                    #y a la frontera el nodo y el costo
                    explored[estado] = costo
                    frontera.add(nodo_actual,costo)
        return NoSolution(explored)
