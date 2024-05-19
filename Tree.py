class TreeStore:
    def __init__(self, items):
        self.items = items
        self.tree = {}
        self.parents = {}
        for item in items:
            self.tree.setdefault(item["parent"], []).append(item)
            self.parents[item["id"]] = item['parent']
    def getAll(self):
        return self.items
    def getItem(self, id):
        for d in self.items:
            if d['id'] == id:
                return d
    def getChildren(self, id):
        result = [] 
        if id in self.tree:
            for child in self.tree[id]:
                result.append(child)
        return result
    def getAllParents(self, id):
        result = []
        while id in self.parents:
            parent_id = self.parents[id]
            parent = self.getItem(parent_id)
            if parent is None:
                break
            else:
                result.append(parent)
                id = parent['id']
        return result
        
items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]        

ts = TreeStore(items)

# Примеры использования:
print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))
