# Release info
Steps for release are

### update resources
* see `./src/brendapy/resources/README.md`

## make release
* update release notes in `release-notes` with commit
* make sure all tests run (`tox -p`)
* bump version (`bumpversion [major|minor|patch]`)
* `git push --tags` (triggers release)

* test installation in virtualenv from pypi
```
mkvirtualenv test --python=python3.9
(test) pip install brendapy
(test) python
from brendapy.examples import *
```
