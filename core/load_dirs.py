import pathlib
import abc 

class Position (abc.ABC):
    @abc.abstractmethod
    def get_value(self):
        pass
    @abc.abstractmethod
    def getChilds(self):
        pass


class ManageFiles:
    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.dirs_and_files  =  FileTree(self.path)

        
class FileTree:
    class FileNode(Position):
        def __init__(self, value):
             self._value = value
             self._childs = []

        def get_childs(self):
             return iter(self._childs)

        
        def add_child(self, path) :    
            if not isinstance(path, pathlib.Path):
                raise TypeError("path should be type pathlib.Path")  
            new_node = FileTree.FileNode(path)
            self._childs.append(new_node)
            return new_node;
        def get_value(self):
            return self._value
        
        def has_childs(self):
            return not len(self._childs) == 0 
    
    # This is the core of my sistem file manage         
    def __init__(self, root ):
          self.root = FileTree.FileNode(root)
          self._create_structure(self.root)

    def _create_structure(self, node):
        path = node.get_value()
        if  not isinstance(path, pathlib.Path):
            raise TypeError("path should be type pathlib.Path")  
        for subPath in path.iterdir():
            new_node = node.add_child(subPath)
            if subPath.is_dir():
                self._create_structure(new_node)

    
    
    def _get_root(self):
        return self.root

    def is_root(self, node):

        return self.root == node
          
     
   

if __name__ == "__main__":
    file_manager = ManageFiles("C:/Users/diazc/OneDrive/Documentos/codigo/lucid")

