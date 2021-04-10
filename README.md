#   validCSV

A small and performance-oriented CSV header verifier / linter with no external Python package dependencies. Just simple.

##  1.	Usage

```python
CSVheader(validator: dict, default: dict = None, ordered = 0, case = 0):
```

-   `ordered`: set `1` if the header need to ordered as the same as your validator. Set `O` otherwise. 
-   `case`: set `0` if for ignoring the letter case. `1` otherwise.
-   `validator`: A dictionary with a key  `header`. The `header` should be a list that will represent your csv header (rule)

### 1.2.  	Verifier methods

```python
CSVheader.verify_header(file) # Uses all config combinations (ordered, case) used at instantiation;
```

```python
CSVheader.simple_verify_header(file,size = None, restrict: bool = True) # Simple leads to only check if the validator elements exists at CSV header; If size is defined, the verifier will check if the header have the length equal to size; restrict will invalidate headers with smaller lengths than your validator;
```

```python
CSVheader.simple_verify_optional_header(file,size = None, restrict: bool = False, options=[]) # It is similiar to simple_verify_header() but, have set optional header columns. If the header have the same validator elements and at least one optional element, the verifier will return true (passed);
```


### 1.3. 	Example	
```python

from validCSV import CSVheader

validHydroNodes = CSVheader(validator={'header': ["id","name","type","block","watersystem","tia","min_alt","max_alt"]})
if validHydroNodes.verify_header(files[filename]):
    # Do something
    print("Test 1 Passed!")

validQualityStations = CSVheader(validator={'header': ["id","snirh","latitude","longitude"]})
if validQualityStations.simple_verify_header(files[filename]):
    # Do something
    print("Test 2 Passed!")

validQualityData = CSVheader(validator={'header': ["date"]})
if validQualityData.simple_verify_optional_header(files[filename], options=['id','snirh']):
    # Do something
    print("Test 3 Passed!")

```

## 2.	Installation

` pip3 install validCSV `

### 2.1	Local installation

1. `git clone https://github.com/bmalbusca/validCSV.git`
2.  `cd validCSV`
3. `python3 setup.py bdist_wheel `
4. `pip3 install -e .  `

## 3.	 Dependencies

`python >= 3.0.0`

### 3.1	Install Dev Dependencies

```python
pip3 install twine 
pip3 install check-manifest
pip3 install setuptools 
```

## 4. 	Test

### 4.1 	`Setup.py`

- `python3 setup.py sdist `
- `check-manifest --create`

## 5.	 PyPi Upload 

**Pypi** url - `https://pypi.org/project/validCSV/`

1. `python3 setup.py sdist bdist_wheel  ` 
2. `twine upload dist/*  `