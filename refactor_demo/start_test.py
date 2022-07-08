
import refactor_demo
import tempfile
import hashlib
import shutil

def test_process_and_write():
    """
    First test to make sure I can use tmp files
    """
    # setup
    tmpDir = tempfile.TemporaryDirectory()
    print(tmpDir)

    # test
    refactor_demo.process_and_write("foo", tmpDir.name)

    # assertion phase
    f = open(tmpDir.name+"/data.txt", "r")
    data = f.read()
    print( data )
    assert data == "foo\n"
    

def test_process_and_write_multiple():
    """
    refactor_demo.process_and_write_multiple is an example function that mixes processing and data writes.

    The processing is trivial: reverse the string. It writes the results to multiple files, making assertions a pain.
    """
    # setup
    tmpDir = tempfile.mkdtemp()
    print(tmpDir)

    # test
    refactor_demo.process_and_write_multiple("foo", tmpDir)

    # assertion phase
    f = open(tmpDir+"/data.txt", "r")
    data = f.read()
    print( data )
    assert data == "foo\n"
    
    f = open(tmpDir+"/reverse.txt", "r")
    data = f.read()
    print( data )
    assert data == "oof\n"


def test_process_and_write_multiple_hashes():
    """
    Replaces the checking of file contents with hashes.  This makes our checks work for arbitrary file types like images.
    """
    # setup
    tmpDir = tempfile.mkdtemp()
    print(tmpDir)

    # test
    refactor_demo.process_and_write_multiple("foo", tmpDir)

    # assertion phase
    f = open(tmpDir+"/data.txt", "rb")
    data = f.read()
    result = hashlib.md5(data).hexdigest()
    assert result == "d3b07384d113edec49eaa6238ad5ff00"
    
    f = open(tmpDir+"/reverse.txt", "rb")
    data = f.read()
    result = hashlib.md5(data).hexdigest()
    assert result == "5432fa9294c227de83e6a85127d0a95b"

    shutil.rmtree(tmpDir)


def test_process_and_write_virtual_hashes_match():
    """
    This removes the filesystem dependency.  Write the data into a dictionary keyed by the "filenames"

    Note that the md5 hashes are the same as when we read them off disk.
    """
    # setup
    v_files = {}

    # test
    refactor_demo.process_and_write_virtual("foo", v_files)

    # assertion phase
    data = v_files["data.txt"]

    result = hashlib.md5(str.encode(data)).hexdigest()
    assert result == "d3b07384d113edec49eaa6238ad5ff00"
    
    data = v_files["reverse.txt"]
    # Because the reverse.txt key was encoded as bytes, we have to .getbuffer() for md5 to accept it
    result = hashlib.md5(data.getbuffer()).hexdigest()
    assert result == "5432fa9294c227de83e6a85127d0a95b"

def test_process_and_write_virtual_hashes_no_match():
    """
    Change the data passed in and verify the hashes no longer match.
    """
    # setup
    v_files = {}

    # test
    refactor_demo.process_and_write_virtual("bar", v_files)

    # assertion phase
    data = v_files["data.txt"]

    result = hashlib.md5(str.encode(data)).hexdigest()
    assert result != "d3b07384d113edec49eaa6238ad5ff00"
    
    data = v_files["reverse.txt"]
    # Because the reverse.txt key was encoded as bytes, we have to .getbuffer() for md5 to accept it
    result = hashlib.md5(data.getbuffer()).hexdigest()
    assert result != "5432fa9294c227de83e6a85127d0a95b"

def test_process_and_write_virtual_hashes():
    """
    refactored_orchestration passes back a proper object, but we can still check the hashes.  We could also do more intuitive and idiomatic assertions here.

    From the object, we could have a different class to write to the filesystem.
    """
    # setup

    # test
    bundle = refactor_demo.refactored_orchestration("foo")

    # assertion phase
    result = hashlib.md5(str.encode(bundle.data)).hexdigest()
    assert result == "d3b07384d113edec49eaa6238ad5ff00"
    
    result = hashlib.md5(str.encode(bundle.reverse)).hexdigest()
    assert result == "5432fa9294c227de83e6a85127d0a95b"

def test_full_circle():
    """
    re-use the original test to make sure our refactored code works *exactly* the same as the original
    """
    # setup
    tmpDir = tempfile.mkdtemp()
    print(tmpDir)

    # test
    refactor_demo.orchestrate_and_write("foo", tmpDir)

    # assertion phase
    f = open(tmpDir+"/data.txt", "rb")
    data = f.read()
    result = hashlib.md5(data).hexdigest()
    assert result == "d3b07384d113edec49eaa6238ad5ff00"
    f.close()

    f = open(tmpDir+"/data.txt", "r")
    data = f.read()
    print( data )
    assert data == "foo\n"
    
    f = open(tmpDir+"/reverse.txt", "rb")
    data = f.read()
    result = hashlib.md5(data).hexdigest()
    assert result == "5432fa9294c227de83e6a85127d0a95b"

    shutil.rmtree(tmpDir)