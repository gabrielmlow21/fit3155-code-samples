class SuffixTree:
    terminal = '$'
    # active_point = ActivePoint()
    input = []
    remaining = 0
    end = 0

    def suffix_tree(self, input):
        input = self.add_unique(input)
    
    def add_unique(self, input):
        c = [0] * (len(input) + 1)
        for i in range(len(input)):
            c[i] = input[i]
        c[len(input)] = self.terminal
        return c
    
    def build_suffix_tree(self):
        root = SuffixNode(1, End(0))
        root.index = -1


class SuffixNode():
    max_characters = 256
    children = [None] * max_characters
    suffix_link = None
    start = 0
    end = 0
    index = 0
    def __init__(self, start, end):
        self.start = start
        self.end = end


class End:
    end = 0
    def __init__(self, end):
        self.end = end