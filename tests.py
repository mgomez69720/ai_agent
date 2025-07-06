from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

if __name__ == "__main__":

    # run_python_file
    print(run_python_file("calculator", "main.py"))
    print("------------------------------------------------------------M")
    print(run_python_file("calculator", "tests.py"))
    print("------------------------------------------------------------M")
    print(run_python_file("calculator", "../main.py"))
    print("------------------------------------------------------------M")
    print(run_python_file("calculator", "nonexistent.py"))
    print("------------------------------------------------------------M")




    # write_file
    """print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("------------------------------------------------------------")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("------------------------------------------------------------")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("------------------------------------------------------------")"""





    # get_file_content
    """#print(get_file_content("calculator", "lorem.txt"))

    print(get_file_content("calculator", "main.py"))
    print("------------------------------------------------------------")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("------------------------------------------------------------")
    print(get_file_content("calculator", "/bin/cat")) #this should return an error string
    print("------------------------------------------------------------")"""




    # get_files_info
    """    #1
    print('\n 1. get_files_info("calculator", ".")')
    print(get_files_info("calculator", ".") )
    
    #2
    print('\n 2. get_files_info("calculator", "pkg")')
    print(get_files_info("calculator", "pkg"))

    #3
    print('\n 3. get_files_info("calculator", "/bin")')
    print(get_files_info("calculator", "/bin") )

    #4
    print('\n 4. get_files_info("calculator", "../")')
    print(get_files_info("calculator", "../") )
    print("")"""