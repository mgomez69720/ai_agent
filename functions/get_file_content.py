import os


def get_file_content(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory)
    target_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    """print(working_directory)
    print(file_path)
    print(abs_working_dir)
    print(os.path.join(working_directory, file_path)) 
    print(target_file_path)"""



    if not target_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    try:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(f.read()) >= MAX_CHARS:   # if os.path.getsize(abs_file_path) > MAX_CHARS:
                return f'{file_content_string}[...File "{file_path}" truncated at 10000 characters]'
            else :
                return f'{file_content_string}'
        
    except Exception as e:
        return f"Error:{e}"





