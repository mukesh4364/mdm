class UnionFind:
    """
    Disjoint Set (Union-Find) data structure.
    """

    def __init__(self):

        self.parent = {}

    def make_set(self, item):

        self.parent[item] = item

    def find(self, item):

        if self.parent[item] != item:

            self.parent[item] = self.find(
                self.parent[item]
            )

        return self.parent[item]

    def union(
        self,
        item1,
        item2,
    ):

        root1 = self.find(item1)

        root2 = self.find(item2)

        if root1 != root2:

            self.parent[root2] = root1
