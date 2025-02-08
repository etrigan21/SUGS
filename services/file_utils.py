import os

class FileUtils(): 
    @staticmethod
    def create_path(directory: str):
        if not os.path.exists(directory): 
            os.makedirs(directory)


    @staticmethod 
    def delete_file(file_path: str): 
        try: 
            if os.path.exists(file_path): 
                os.remove(file_path)            
        except Exception as e: 
            print(str(e))
        