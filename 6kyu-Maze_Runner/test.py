import unittest
from problem import *

class Test(unittest.TestCase):
    def tests(self):
        maze = [[1,1,1,1,1,1,1],
                [1,0,0,0,0,0,3],
                [1,0,1,0,1,0,1],
                [0,0,1,0,0,0,1],
                [1,0,1,0,1,0,1],
                [1,0,0,0,0,0,1],
                [1,2,1,0,1,0,1]]

        self.assertEqual(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E"]), "Finish")
        self.assertEqual(maze_runner(maze,["N","N","N","N","N","E","E","S","S","E","E","N","N","E"]), "Finish")
        self.assertEqual(maze_runner(maze,["N","N","N","N","N","E","E","E","E","E","W","W"]), "Finish")
        self.assertEqual(maze_runner(maze,["N","N","N","W","W"]), "Dead")
        self.assertEqual(maze_runner(maze,["N","N","N","N","N","E","E","S","S","S","S","S","S"]), "Dead")
        self.assertEqual(maze_runner(maze,["N","E","E","E","E"]), "Lost")

if __name__ == '__main__':
   unittest.main()
