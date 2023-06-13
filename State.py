# this class only for the first time setup init state for problem and is given to every search
class State:
    def __init__(self, pipes: list, parent, g_n: int, prev_action: tuple):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n
        self.prev_action = prev_action
        self.set_cost()

    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.pipes[pipe_dest_ind].add_ball(self.pipes[pipe_src_ind].remove_ball())

    def __hash__(self):
        hash_strings = []
        for i in self.pipes:
            hash_strings.append(i.__hash__())
        hash_strings = sorted(hash_strings)
        hash_string = ''
        for i in hash_strings:
            hash_string += i + '###'
        return hash_string

    def set_cost(self):
        if self.parent is not None:
            self.cost = self.parent.cost + abs(self.prev_action[0] - self.prev_action[1])
        else:
            self.cost = 0

    def __lt__(self, other):
        return 1

    def h(self):
        count = 0
        for i in self.pipes:
            counttmp = 1
            if not i.is_empty():
                color = i.stack[0]
                for j in range(1, len(i.stack)):
                    if i.stack[j] == color:
                        counttmp += 1
                    else:
                        break
                count += (counttmp ** 2)
        return -count