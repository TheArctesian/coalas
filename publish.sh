python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --upgrade twine
py -m twine upload --repository coalas dist/*
# this one might return an error, delete dist and do again 
