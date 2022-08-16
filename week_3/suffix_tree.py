from logging import root


class SuffixTree:
    terminal = '$'
    root = None
    active_point = None
    input = []
    remaining = 0
    end = None

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
        self.end = End(-1)
        self.active_point = ActivePoint(root)
        for i in range(len(self.input)):
            self.start_phase(i)
        self.set_index(root, 0, len(input))
    
    def start_phase(self, i):
        last_internal_node = None
        self.end.end += 1
        self.remaining += 1
        while self.remaining > 0:
            if self.active_point.active_length == 0:
                if self.active_point.active_node.children[self.input[i]] != None:
                    self.active_point.active_edge = self.active_point.active_node.children[input[i]].start
                    self.active_point.active_length += 1
                    break
                else:
                    self.root.children[input[i]] = SuffixNode(i, self.end)
                    self.remaining -= 1
            else:
                c = self.get_next_character(i)
                if c != 0:
                    if c == self.input:
                        edge = self.select_edge()
                        if last_internal_node != None:
                            last_internal_node.suffix_link = edge
                        self.walk_down(i)
                        break
                    else:
                        edge = self.select_edge()
                        current_start = edge.start
                        edge.start += self.active_point.active_length
                        internal_node = SuffixNode(current_start, End(current_start + self.active_point.active_length - 1))
                        leaf_node = SuffixNode(i, self.end)
                        internal_node.children[input[edge.start]] = edge
                        internal_node.children[input[leaf_node.start]] = leaf_node
                        internal_node.index = -1
                        self.active_point.active_node.children[input[internal_node.start]] = internal_node        
                        if last_internal_node != None:
                            last_internal_node.suffix_link = internal_node
                        last_internal_node = internal_node
                        internal_node.suffix_link = self.root
                else:
                    edge = self.select_edge()
                    edge.children[input[i]] = SuffixNode(i, self.end)
                    if last_internal_node != None:
                        last_internal_node.suffix_link = edge
                    last_internal_node.suffix_link = edge 
                if self.active_point.active_node != self.root:
                    self.active_point.active_node = self.active_point.active_node.suffix_link
                else:
                    self.active_point.active_edge += 1
                    self.active_point.active_length -= 1
                self.remaining -= 1

    def get_next_character(self, i):
        edge = self.select_edge()
        if self.edge_size(edge) >= self.active_point.active_length:
            return input[edge.start + self.active_point.active_length]
        elif (self.edge_size(edge) + 1) == self.active_point.active_length:
            if edge.children[self.input[i] != None]:
                return self.input[i]
        else:
            self.active_point.active_point = edge
            self.active_point.active_edge = self.active_point.active_edge + self.edge_size(edge) + 1
            return self.get_next_character(i)
        return 0

    def select_edge(self):
        return self.active_point.active_node.children[self.input[self.active_point.active_edge]]

    def edge_size(self, edge):
        return edge.end.end - edge.start
    
    def set_index(self, root, val, size):
        if root == None: return
        val = val + root.end.end - root.start + 1
        if root.index != -1:
            root.index = size - val
            return
        for node in root.children:
            self.set_index(node, val, size)
        



class SuffixNode:
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


class ActivePoint:
    active_node = None
    active_edge = None
    active_length = None

    def active_point(self, node):
        self.active_node = node
        self.active_edge = -1
        self.active_length = 0
    
    def active_point(self, active_node, active_edge, active_length):
        self.active_node = active_node
        self.active_edge = active_edge
        self.active_length = active_length