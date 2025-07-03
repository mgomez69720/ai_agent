import os

def write_file(working_directory, file_path, content):

    abs_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    full_path_without_file = os.path.dirname(target_file_path)
    
    """print(working_directory)
    print(file_path)
    print(abs_working_dir)
    print(os.path.join(working_directory, file_path)) 
    print(target_file_path)
    print(full_path_without_file)"""


    if not target_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file_path): 
        try:
            os.makedirs(full_path_without_file, exist_ok=True)  
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(target_file_path) and os.path.isdir(target_file_path):
        return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(target_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        # It's important to return a success string so that our LLM knows that the action 
        # it took actually worked. Feedback loops, feedback loops, feedback loops!
    except Exception as e:
            return f"Error: writing to file: {e}"
    

     