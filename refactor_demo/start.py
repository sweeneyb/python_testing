import tempfile
import io

def process_and_write(data: str, path: str): 
    """
    dummy to verify I can write to a file
    """
    print(data)
    f = open(path+"/data.txt", "w")
    f.write(data+"\n")
    f.close()


def process_and_write_multiple(data: str, path: str):
    """
    Simulate writing some data and processed data into the filesystem
    """
    reversed = data [::-1] # reverses a string
    f = open(path+"/data.txt", "w")
    f.write(data+"\n")
    f.close()
    f = open(path+"/reverse.txt", "w")
    f.write(reversed+"\n")
    f.close()

def process_and_write_virtual(data: str, files: dict):
    """
    This removes the dependency on the filesystem.  Instead, write bytes into a dict that serves as
    a sort of virtual filesystem.  
    """
    reversed = data [::-1] # reverses a string

    # example of string data like normal text
    files["data.txt"] = data + "\n"
    # convert a string to bytes to show how this might work for a binary thing like a picture
    files["reverse.txt"] = io.BytesIO(str.encode(reversed+"\n"))


# Make a class that represents the object of that virtual filesystem. We can easily (un)marshall into/out of an object like this.
class Bundle:
    def __init__(self, data = ""):
        self.data = data
        self.reverse = self.data [::-1] # reverses a string
        self.data = self.data+"\n"
        self.reverse = self.reverse+"\n"


def refactored_orchestration(data:str) -> Bundle: 
    """
    A much cleaner invocation that doesn't care where the results go
    """
    result = Bundle(data)
    return result

#  this is NOT exported
def persist_bundle_to_disk(bundle: Bundle, path: str):
    """
    A small utility to write files similar to the layout in process_and_write_multiple.
    Another implementation could write to a zip file, s3 bucket, etc.
    """
    f = open(path+"/data.txt", "w")
    f.write(bundle.data)
    f.close()
    f = open(path+"/reverse.txt", "w")
    f.write(bundle.reverse)
    f.close()


def orchestrate_and_write(data:str, path: str):
    """
    This has the exact same signature as process_and_write_multiple.
    We can confidently change the implementation without worrying anything broke.

    """
    bundle = refactored_orchestration(data)
    persist_bundle_to_disk(bundle, path)