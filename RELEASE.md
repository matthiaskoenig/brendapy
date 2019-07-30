# Release info
Steps for release are

## github release
* github: close and update issues/milestone
* update version number in develop branch
* fix pep8 issues (`tox -e pep8`)
* make sure all tests run (`tox -e py36`, `tox -e py37`)
* add changes to README changelog section
* github: merge all develop changes to master via pull request
* github: create release from master branch

## pypi
* release on [pypi](https://pypi.python.org/pypi/brendapy)
```
git branch master
git pull
python setup.py sdist
twine upload dist/*
```
* test installation in virtualenv from pypi
```
mkvirtualenv test --python=python3.6
(test) pip install brendapy
```

## version bump
* switch to develop branch and increase version number