
from queue import PriorityQueue
from Solution import Solution
from Problem import Problem
from datetime import datetime



class Search:
    @staticmethod
    def dfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        explored = {}
        start_time = datetime.now()
        stack = []
        state = prb.initState
        stack.append(state)
        while len(stack) > 0:
            state = stack.pop(0)
            explored[state.__hash__()] = 1
            neighbors = prb.successor(state)
            for c in neighbors:
                if c.__hash__() not in explored.keys():
                    if prb.is_goal(c):
                        print(c.g_n)
                        return Solution(c, prb, start_time)
                    stack.append(c)
        return None
    def ids(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        for limit in range(0,10000):
            print(limit)
            explored = {}
            start_time = datetime.now()
            stack = []
            state = prb.initState
            stack.append(state)
            while len(stack) > 0:
                state = stack.pop(-1)
                explored[state.__hash__()] = 1
                neighbors = prb.successor(state)
                for c in neighbors:
                    if c.__hash__() not in explored.keys():
                        if prb.is_goal(c):
                            print(c.g_n)
                            return Solution(c, prb, start_time)
                        if state.g_n <= limit:
                            stack.append(c)
        return None



    def ucs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        explored = {}
        start_time = datetime.now()
        hq = PriorityQueue()
        state = prb.initState
        hq.put((state.cost, state))
        while not hq.empty():
            state = hq.get()[1]
            explored[state.__hash__()] = state
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                elif c.__hash__() not in explored.keys():
                    hq.put((c.cost, c))
        return None

    def A_star(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        explored = {}
        start_time = datetime.now()
        hq = PriorityQueue()
        state = prb.initState
        hq.put((state.g_n + state.h(), state))
        print(state.g_n + state.h())
        while not hq.empty():
            state = hq.get()[1]
            explored[state.__hash__()] = state
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    print(c.g_n)
                    return Solution(c, prb, start_time)
                elif c.__hash__() not in explored.keys():
                    hq.put((c.g_n + c.h(), c))
        return None

    def IDA_star(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        q = []
        q.append(prb.initState.g_n + prb.initState.h())
        while True:
            cut_off = min(q)
            print(cut_off)
            q = []
            explored = {}
            start_time = datetime.now()
            stack = []
            state = prb.initState
            stack.append(state)
            while len(stack) > 0:
                state = stack.pop(-1)
                explored[state.__hash__()] = 1
                neighbors = prb.successor(state)
                for c in neighbors:
                    if prb.is_goal(c):
                        print(c.g_n)
                        return Solution(c, prb, start_time)
                    if c.__hash__() not in explored.keys():
                        if c.g_n + c.h() <= cut_off:
                            stack.append(c)
                        elif c.g_n + c.h() > cut_off:
                            q.append(c.g_n + c.h())
        return None



