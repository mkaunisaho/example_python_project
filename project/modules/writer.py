import os
from dotenv import load_dotenv

load_dotenv()


class Writer():
    def __init__(self):
        print("Initializing Writer class!")
        self.class_var = 123
        pass

    def some_function(self):
        # do something
        pass

    def print_class_var(self) -> None:
        """_summary_
        """
        print(self.class_var)
        pass

    def print_text(self, text:str) -> None:
        """_summary_

        Args:
            text (str): _description_
        """
        print(text)
    
    def print_from_file(self, file_path:str) -> None:
        """_summary_

        Args:
            file_path (str): _description_
        """
        with open(file_path, "r") as f:
            print(f.read())
    
    def print_env_var(self) -> None:
        print(os.getenv("SUPER_SECRET_KEY"))