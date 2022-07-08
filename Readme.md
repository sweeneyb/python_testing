
Super-simple repo to demo a rough sketch of a python project that includes a test or two.  


initial setup after clone:
```
python3 -m venv .venv
source .venv/bin/activate
```
Add pytest
```
pip install pytest
```
or
```
pip3 install -r requirements.txt 
```

Run things:
```
./runner.py
```


# refactor_demo
To see normal output, use the -s flag to pytest:
```
pytest -s refactor_demo/start_test.py 
```