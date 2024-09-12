from modules import writer
import os
import time

try:
    w = writer.Writer()
    w.print_class_var()
    w.print_text("This is Mikaela's demo project")
    w.print_from_file(os.path.join(os.getcwd(), r"_internal/assets/text.txt"))
    w.print_env_var()
except Exception as e:
    print(e)
time.sleep(10)