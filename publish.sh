python3 -m pip install --upgrade pip
rm -rf dist
python3 -m build
python3 -m pip install --upgrade twine
python3 -m twine upload --repository pypi dist/*
# this one might return an error, delete dist and do again 
