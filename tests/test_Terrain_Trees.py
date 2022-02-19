import Terrain_Trees


def dfs(root, mesh):
    if root.is_leaf():
        if root.indexes_vertices() != False:
            print(root.get_v_start())
            print(root.get_v_end())
            for vid in range(root.get_v_start(), root.get_v_end()):
                vertex = mesh.get_vertex(vid)
                for index in range(0, 3):
                    print(vertex.get_c(index))
            vt = root.get_VT(mesh)
            print(vt)
    else:
        for i in range(0, 4):
            child = root.get_son(i)
            if child != None:
                dfs(child, mesh)


if __name__ == '__main__':
    py_tree = Terrain_Trees.PyPRT_Tree(1, 4)
    py_mesh = Terrain_Trees.PyMesh()
    py_tree.get_mesh(py_mesh)

    py_reader = Terrain_Trees.PyReader()
    py_reader.Py_read_mesh(py_tree, '../modules/Terrain_Trees/data/devil_0.tri')
    py_tree.build_tree()

    # py_tree.get_leaves_number()
    py_reindexer = Terrain_Trees.PyReindexer()
    py_reindexer.reindex_tree_and_mesh(py_tree, False, False)

    root = Terrain_Trees.PyNode_V()
    py_tree.get_root(root)

    dfs(root, py_mesh)
