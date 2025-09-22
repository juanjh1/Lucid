from pathlib import Path


class FileManager():

    @staticmethod
    def open_file(path: Path) -> str:
        absolute_path = FileManager._validate_readable_path(path)
        with open(absolute_path, "r") as file: 
            return file.read()
     
    @staticmethod
    def _validate_readable_path(path: Path) -> Path:
        if not path.exists() or not path.is_file():
            raise RuntimeError(f"Path does not exist or is not a file: {path.absolute()}")
        return path.absolute()
     
    @staticmethod
    def save_file(path: Path, content: str) :
        absolute_path = FileManager._validate_readable_path(path)
        with open(absolute_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    @staticmethod       
    def _validate_writeable_path(path: Path) -> Path:
        parent = path.parent
        if not parent.exists():
            raise RuntimeError(f"Directory does not exist: {path.absolute()}")
        return path.absolute()
